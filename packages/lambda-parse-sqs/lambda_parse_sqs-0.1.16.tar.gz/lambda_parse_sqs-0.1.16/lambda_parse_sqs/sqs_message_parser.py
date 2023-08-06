from enum import Enum
import json
from .utils import config_log
from .errors import *

logger = config_log()

def _parser_generic(record: dict) -> dict:
    return json.loads(record.get('body'))

def _parser_sns(record: dict) -> dict:
    return json.loads(json.loads(record.get('body')).get('Message'))

def _parser_sns_raw(record: dict) -> dict:
    return json.loads(record.get('body'))

class BaseProvider(Enum):
    GENERIC = "parser_generic"
    SNS = "parser_sns"
    SNS_RAW = "parser_sns_raw"

class Parser():

    def __init__(self, record: list, provider: str = "GENERIC"):

        # identifying parser from provider
        self.provider = self._identify_provider(provider)
        
        # Parse messages
        self.message = self._parse_message(record)

    def _identify_provider(self, provider):
        # Try to parse message using select parser provider
        logger.info("Selected provider: {}".format(provider))
        if provider is None:
            provider = "GENERIC"
        try:
            selected_provider = "_{}".format(BaseProvider[provider].value)
            logger.info("Parser to apply: {}".format(provider))
        except Exception as ex:
            raise ProviderSelectionException("Error parsing using provider: {}".format(ex))
        return selected_provider

    def _parse_message(self, record):
        # Try to parse message using select parser provider
        try:
            message = globals()[self.provider](record)
        except Exception as ex:
            raise Exception("Error parsing message: {}".format(ex))
        return message

    def message(self):
        return self.message


"""
    def _extract_records(self, record):
        sqs_records = record.get('Messages')
        if sqs_records is None:
            raise RecordsNotFoundException("SQS message list is empty.")
        return sqs_records
"""