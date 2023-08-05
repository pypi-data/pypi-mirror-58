import requests
import os
import json
import sys
from time import sleep
from onnlogger import Loggers

GET_ALL_THRESHOLD = 500
MAX_ALLOWED_REQS_ERROR = -4290001
API_MAX_RETRIES = 3
API_RETRY_SLEEP = 30


class Cas:
    def __init__(self, api_version='v1', app_name='', console_logger=False, print_logger=False, log_level='INFO',
                 log_file_path=''):
        self.logger = Loggers(logger_name=app_name, console_logger=console_logger, print_logger=print_logger,
                              log_level=log_level, log_file_path=log_file_path)

        get_cas_url = os.getenv('CAS_URL', 'https://api.tmcas.trendmicro.com')
        self.cas_url = f'{get_cas_url}/{api_version}'
        self.logger.entry('info', f'Using CAS URL: {get_cas_url}')
        self.logger.entry('info', 'Obtaining CAS API key')
        cas_key = os.environ.get('CAS_KEY')

        if not cas_key:
            msg = '"CAS_KEY" environment variable must be specified'
            self.logger.entry('critical', msg)
            sys.exit(1)

        self.header = {'Authorization': 'Bearer ' + cas_key}

    def _api_call(self, url, params='None', required_params=None, api_verb='get'):
        """Makes API call

        Args:
            url (str): URL to send call to
            params (dict): User provided parameters
            required_params (list): Parameters required by the API endpoint
            limit (int): Limit to add to the payload
            api_verb (str): POST, GET, etc

        Examples:

            {
                'value': [{
                    'mail_message_sender': 'accountspay@example.com',
                    'mail_message_recipient': ['leland@example.com],
                    'mail_message_subject': 'Annual Salary Review Process',
                    'mailbox': 'leland@example.com',
                    ...

        """

        # confirm all params have been provided
        if required_params:
            if not params:
                joined_params = ', '.join(required_params)
                msg = f'No parameters were provided. Required parameters are: {joined_params}'
                self.logger.entry('critical', msg)
                sys.exit(msg)

            get_params = params[0] if isinstance(params, list) else params
            params_list = list(get_params.keys())
            missing_params = list(set(required_params) - set(params_list))

            if missing_params:
                joined_missing_list = ', '.join(missing_params)
                msg = f'Required parameter(s) missing: {joined_missing_list}'
                self.logger.entry('critical', msg)
                sys.exit(msg)

        # `request_verb` becomes requests.get, requests.put, etc
        request_verb = getattr(requests, api_verb)

        if isinstance(params, dict):
            r = request_verb(url, headers=self.header, params=params)

        elif isinstance(params, list):
            r = request_verb(url, headers=self.header, json=params)

        else:
            r = request_verb(url, headers=self.header)
        output = json.loads(r.text)

        return output

    def _retry_api_call(self, url, params, required_params, api_verb, max_retries=API_MAX_RETRIES,
                        retry_sleep=API_RETRY_SLEEP):
        """Retries an API call when the CAS max request limit is reached

        Args:
            url (str): URL to send call to
            params (dict): User provided parameters
            required_params (list): Parameters required by the API endpoint
            api_verb (str): POST, GET, etc
            max_retries (int): Maximum number of retries
            retry_sleep (int): Seconds to wait before retrying

        Examples:

            {
                'value': [{
                    'mail_message_sender': 'accountspay@example.com',
                    'mail_message_recipient': ['leland@example.com],
                    'mail_message_subject': 'Annual Salary Review Process',
                    'mailbox': 'leland@example.com',
                    ...

        """
        retry_count = 1

        while max_retries >= retry_count:
            self.logger.entry('info', f'Maximum allowed requests exceeded. Waiting {retry_sleep} seconds '
                                      f'before trying again. (Attempt {retry_count}/{max_retries})')
            retry_count += 1
            sleep(retry_sleep)

            output = self._api_call(url, params, required_params, api_verb)
            api_exceeded = self._check_api_exceeded(output)

            if not api_exceeded:
                return output

        msg = output['msg']
        self.logger.entry('critical', msg)
        sys.exit(msg)

    def _check_api_exceeded(self, output, max_reqs_error_code=MAX_ALLOWED_REQS_ERROR) -> bool:
        """Checks if the CAS max request limit has been reached reached

        Args:
            output: API call output
            max_reqs_error_code (int): Error code

        Returns:
            bool

        """
        code = output.get('code')
        if code == max_reqs_error_code:
            return True

        else:
            return False

    def _get_results(self, url, params, required_params=False, get_all=True, api_verb='get') -> dict:
        """Obtains results from API call

        `entries` contains a list of results, while `api` contains information which can be used for troubleshooting
        the API and/or tracking API calls (e.g `batch_id`). Note that `api` will be empty at times.

        Args:
            url (str): URL to send call to
            params (list or dict): User provided parameters
            required_params (list): Parameters required by the API endpoint
            get_all (bool): Retrieve all results or not
            api_verb (str): POST, GET, etc

        Returns:
            dict

        """
        if isinstance(params, dict):
            if params['limit'] < GET_ALL_THRESHOLD and get_all:
                get_all = False
                self.logger.entry('info', f'Limit is set under {GET_ALL_THRESHOLD}. Turning "get all" flag OFF')

        output = {
            'entries': [],
            'api': dict()
        }

        while True:
            self.logger.entry('info', f'Calling {api_verb.upper()} {url}\nUsing parameters: {params}')
            api_output = self._api_call(url, params, required_params, api_verb)
            retry_required = self._check_api_exceeded(api_output)

            if retry_required:
                api_output = self._retry_api_call(url, params, required_params, api_verb)

            code = api_output.get('code')

            if code == 0:
                self.logger.entry('info', 'Call completed successfully')
                output['api'] = api_output

                break

            self.logger.entry('debug', f'Output:\n{api_output}')
            value = api_output['value']

            for entry in value:
                self.logger.entry('debug', f'Adding following entry to "output":\n{entry}')
                output['entries'].append(entry)

            if 'next_link' in api_output and get_all:
                url = api_output['next_link']

                # prevent `limit` and other params from being added multiple times
                params = None

            else:
                break

        self.logger.entry('debug', f'All entries obtained:\n{output}')
        return output

    def _add_limit_param(self, params=None, limit=0) -> dict:
        """Convenience method for adding `limit` parameter

        Performs one of the following actions:
            * If no parameters have been set, set the `limit` parameter
            * If the `limit` parameter HAS NOT been set by the user, set it
            * If the `limit` parameter is already set by the user, don't modify it

        Args:
            params: User provided parameters
            limit: Limit to add to the payload

        Examples:
            {'subject': '"Salary Review"', 'lastndays': 1, 'limit': 1000}

        Returns:
            dict: Parameters
        """

        if 'limit' in params:
            pass

        elif not params and limit > 0:
            params = {'limit': limit}

        elif limit > 0:
            params['limit'] = limit

        return params

    def sweep_emails(self, params=None, limit=1000, get_all=True) -> dict:
        """Performs an email sweep

        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-investigation/sweep-for-email-mess.aspx

        Args:
            params: User provided parameters
            limit: Limit to add to the payload
            get_all (bool): Retrieve all results or not

        Examples:

            {
                'entries': [{
                    'mail_message_sender': 'accountspay@example.com',
                    'mail_message_recipient': ['leland@example.com'],
                    'mail_message_subject': 'Annual Salary Review Process',
                    'mailbox': 'leland@example.com',
                    ...
            }

        Returns:
            dict

        """
        self.logger.entry('info', f'Running sweep call...')
        updated_params = self._add_limit_param(params, limit)
        url = f'{self.cas_url}/sweeping/mails'
        output = self._get_results(url, updated_params, get_all=get_all)

        return output

    def get_security_logs(self, params=None, limit=500, get_all=True):
        """Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/log-retrieval-api/get-security-logs.aspx

        Args:
            params (dict): User provided parameters
            limit (int): Limit to add to the payload
            get_all (bool): Retrieve all results or not
        """

        required_params = ['service', 'event']

        updated_params = self._add_limit_param(params, limit)
        url = f'{self.cas_url}/siem/security_events'
        output = self._get_results(url, updated_params, required_params, get_all=get_all)

        return output

    def get_user_mitigation(self, params=None, limit=500, get_all=True):
        """Get user mitigation status

        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-mitigation-ap/query-action-results.aspx

        Args:
            params (dict): User provided parameters
            limit (int): Limit to add to the payload
            get_all (bool): Retrieve all results or not
        """

        updated_params = self._add_limit_param(params, limit)
        url = f'{self.cas_url}/mitigation/accounts'
        output = self._get_results(url, updated_params, get_all=get_all)

        return output

    def get_email_mitigation(self, params=None, limit=500,  get_all=True):
        """Get email mitigation status

        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-mitigation-ap/query-action-results.aspx

        Args:
            params (dict): User provided parameters
            limit (int): Limit to add to the payload
            get_all (bool): Retrieve all results or not
        """

        updated_params = self._add_limit_param(params, limit)
        url = f'{self.cas_url}/mitigation/mails'
        output = self._get_results(url, updated_params, get_all=get_all)

        return output

    def set_user_mitigation(self, entries):
        """Set user mitigations

        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-mitigation-ap/take-actions-on-user.aspx

        Args:
            entries:

        Returns:

        """

        required_params = ['action_type', 'service', 'account_provider', 'account_user_email']

        url = f'{self.cas_url}/mitigation/accounts'
        output = self._get_results(url, entries, required_params, api_verb='post')

        return output

    def set_email_mitigation(self, entries):
        """Set email mitigations

                Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-mitigation-ap/take-actions-on-emai.aspx

        Args:
            entries:

        Returns:

        """

        url = f'{self.cas_url}/mitigation/mails'
        output = self._get_results(url, entries,  api_verb='post')

        return output

    def get_blocked_lists(self, params=None):
        """
        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-remediation-a/update-blocked-lists.aspx
        """

        updated_params = self._add_limit_param(params)
        url = f'{self.cas_url}/remediation/mails'
        output = self._get_results(url, updated_params)

        return output

    def update_blocked_lists(self, params=None):
        """
        Docs: http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-remediation-a/update-blocked-lists.aspx
        """

        required_params = ['action_type', 'rules']

        updated_params = self._add_limit_param(params)
        url = f'{self.cas_url}/remediation/mails'
        output = self._get_results(url, updated_params, required_params, api_verb='post')

        return output
