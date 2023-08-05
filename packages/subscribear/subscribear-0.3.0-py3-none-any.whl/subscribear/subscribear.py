from typing import Optional, Union
import json
import logging

from boto3 import client, exceptions

logger = logging.getLogger(__name__)


class SnsSubscriBear:
    def __init__(self, *args, **kwargs):
        try:
            self.sns_client = client('sns')
        except exceptions.Boto3Error as ex:
            self.verbose = True
            self._log_if_verbose(logger.error, 'The AWS config is invalid, unable to use boto3.')
        self.verbose = kwargs.get('verbose') or False

    def _log_if_verbose(self, logger_method, message):
        if getattr(self, 'verbose', False):
            logger_method(f'\U0001F43B {self.__class__.__name__}: {message}')


class SlaveBear(SnsSubscriBear):
    """
    AWS-SNS Subscription client bear
    """
    def confirm_subscription(self, topic_arn: str,  token: str) -> bool:
        response = self.sns_client.confirm_subscription(
            TopicArn=topic_arn,
            Token=token,
        )
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return True
        self._log_if_verbose(logger.warning, f'Subscription confirmation failed with: {response}')
        return False

    def request_to_json(self, request) -> Union[dict, bool, None]:
        json_body = request.get_json(force=True, silent=True)
        if not json_body:
            self._log_if_verbose(logger.warning,
                                 'Expected json body, is this request really from aws-sns?')
            return None

        if json_body.get('Type') == 'Notification':
            self._log_if_verbose(logger.info,
                                 f'Received a notification message: {json_body.get("Message")}')
            return json_body
        elif json_body.get('Type') == 'SubscriptionConfirmation':
            success = self.confirm_subscription(json_body.get('TopicArn'), json_body.get('Token'))
            if success:
                self._log_if_verbose(logger.info,
                                     f'Confirmed a subscription for {request.base_url}')
            return True
        return False


class MasterBear(SnsSubscriBear):
    """
    AWS-SNS controller bear
    """
    def __init__(self, *args, **kwargs):
        config = kwargs.get('config')
        if not (config and config.get('topic_arn') and config.get('default_message_attributes')):
            self.verbose = True
            self._log_if_verbose(
                logger.error, 'MasterBear expects a "config" kwarg dict with '
                              '{"topic_arn": "...", "default_message_attributes": "..."}')
        super().__init__(*args, **kwargs)
        self.topic_arn = config.get('topic_arn')
        self.default_message_attributes = config.get('default_message_attributes')

    def _update_subscription_filter_policy(
            self, subscription_arn: str, attributes: dict, ) -> bool:
        response = self.sns_client.set_subscription_attributes(
            SubscriptionArn=subscription_arn,
            AttributeName='FilterPolicy',
            AttributeValue=json.dumps(attributes)
        )
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return True
        self._log_if_verbose(logger.warning,
                             f'Update subscription arn={subscription_arn} attributes failed with '
                             f'response: {response}')
        return False

    def _create_subscription_with_filter_policy(
            self, webhook_url: str, resource_types: list, verbose: bool = True) -> bool:
        response = self.sns_client.subscribe(
            TopicArn=self.topic_arn,
            Protocol='https',
            Endpoint=webhook_url,
            Attributes={'FilterPolicy': json.dumps({'resource_type': resource_types})},
        )
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return True
        if verbose:
            logger.warning(f'SNS: create subscription failed with response: {response}')
        return False

    def get_active_subscriptions(self, webhook_url: str, topic_arn: str = None) -> Optional[str]:
        """
        Returns the active subscription matching a certain webhook_url.
        Since webhook_url must be unique for a topic (there cannot be two active subscriptions for
         the same topic with the same webhook_url )
        """
        topic_arn = topic_arn or self.topic_arn
        sns_response = self.sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)
        if sns_response \
                and sns_response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200 \
                and sns_response.get('Subscriptions'):
            for s in sns_response['Subscriptions']:
                if s['SubscriptionArn'] != 'PendingConfirmation' and s['Endpoint'] == webhook_url:
                    return s['SubscriptionArn']
        self._log_if_verbose(logger.warning, f'No active subscriptions matching {webhook_url}')
        return None

    def get_subscription_attributes(
            self, subscription_arn: str, verbose: bool = True) -> Optional[dict]:
        response = self.sns_client.get_subscription_attributes(SubscriptionArn=subscription_arn)
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return response
        self._log_if_verbose(logger.warning,
                             f'SNS No attributes found for subscription arn={subscription_arn}')
        return None

    def remove_subscription(self, subscription_arn) -> bool:
        response = self.sns_client.unsubscribe(SubscriptionArn=subscription_arn)
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return True
        self._log_if_verbose(logger.warning,
                             f'Subscription unsubscribe failed with response: {response}')
        return False

    def create_subscription(self, resource_types: list, webhook_url: str) -> bool:
        """
       :param resource_types: list with strings from config.API_RESOURCE_TYPES
       :param webhook_url: one endpoint to witch the subscription should start sending notifications
       :return:
       """
        _verbose = self.verbose
        self.verbose = False  # force false verbose for this method call
        arn_to_update = self.get_active_subscriptions(webhook_url)
        self.verbose = _verbose

        if not arn_to_update:
            return self._create_subscription_with_filter_policy(webhook_url, resource_types)
        # subscription found, look for attributes
        existing_sub = self.get_subscription_attributes(arn_to_update)
        if not existing_sub:
            return False
        # subscription attributes found, update (add)
        old_filter_policy = json.loads(existing_sub['Attributes']['FilterPolicy'])
        new_filter_policy = {
            'resource_type': list(set(old_filter_policy['resource_type']) | set(resource_types))
        }
        if set(old_filter_policy['resource_type']) == set(new_filter_policy['resource_type']):
            # all resource_types to be updated were already on the subscription -> nothing to do
            return True
        return self._update_subscription_filter_policy(arn_to_update, new_filter_policy)

    def delete_subscription(self, resource_types: list, webhook_url: str) -> bool:
        """
        :param resource_types: list with strings from config.API_RESOURCE_TYPES; if a subscription
        has as filter policy multiple resource_types, only those provided in this parameter will be
        removed (attribute update)
        :param webhook_url: one endpoint which the subscription is currently notifying
        :return:
        """
        arn_to_delete = self.get_active_subscriptions(webhook_url)
        if not arn_to_delete:
            # todo shouldn't raise here, find a better way to handle this
            raise ValueError(f'No subscription available for {resource_types} and {webhook_url}')
        # subscription found, looking for attributes to update (remove)
        existing_sub = self.get_subscription_attributes(arn_to_delete)
        if not existing_sub:
            return False
        # subscription attributes found, update the policy or remove it entirely
        old_filter_policy = json.loads(existing_sub['Attributes']['FilterPolicy'])
        new_filter_policy = {
            'resource_type': list(set(old_filter_policy['resource_type']) - set(resource_types))
        }
        if new_filter_policy['resource_type']:
            # delete the subscription for SOME of the filter_policies -> attrib. update
            return self._update_subscription_filter_policy(arn_to_delete, new_filter_policy)
        # delete subscription for ALL the filter_policies available-> actual delete
        return self.remove_subscription(arn_to_delete)

    def send_message(
            self, resource_type: str, message: dict, attributes: Optional[dict] = None) -> bool:
        try:
            message_string = json.dumps(message)
        except Exception as ex:
            self._log_if_verbose(logger.warning,
                                 f'Attempted to send a non json message - failed with: {ex}')
            return False
        response = self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message_string,
            MessageAttributes={
                **{
                    key: {
                        'DataType': 'String',
                        'StringValue': val
                    } for key, val in
                    {**self.default_message_attributes, **(attributes or {})}.items()
                },
                'resource_type': {
                    'DataType': 'String',
                    'StringValue': resource_type,
                },
            },
        )
        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return True
        self._log_if_verbose(
            logger.warning,
            f'Sending a message ({message_string}) for {resource_type} failed with: {response}'
        )
        return False
