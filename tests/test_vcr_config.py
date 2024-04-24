import os
import socket
import unittest

# Block network access
# Comment out the following code block if you want to run the tests with real network access
def guard(*args, **kwargs):
    raise Exception("Blocked network access. Use VCR cassettes instead.")
socket.socket = guard

import vcr
import json

headers_to_filter = ['Nel', 'Reporting-Endpoints', 'Report-To']

def response_filter():
    def before_record_response(response):
        # remove unwanted headers
        for header in headers_to_filter:
            if header in response['headers']:
                del response['headers'][header]
        
        # format the JSON string to JSON object
        if 'body' not in response:
            return response
        
        # if 'object' key already exists, skip
        if 'object' in response['body']:
            return response
        
        json_data = json.loads(response['body']['string'])
        response['body']['object'] = json_data
        
        return response

    return before_record_response

def vcr_setup():
    return vcr.VCR(
        cassette_library_dir='tests/fixtures',
        record_mode='once',
        match_on=['method', 'host', 'path', 'query'],
        filter_query_parameters=['auth_token'],
        decode_compressed_response=True,
        before_record_response=response_filter(),
        serializer='json',
    )

class TestCaseWithAPIKey(unittest.TestCase):
    """Unit Test Case with API key
    This class is used to test the ButterCMS API with VCR

    This class leverages VCR to record HTTP responses and replay them for future tests, minimizing network calls. VCR supports various recording modes such as 'once', 'new_episodes', 'none', and 'all', detailed at: https://vcrpy.readthedocs.io/en/latest/usage.html#record-modes

    Initially, tests must run with actual network access to create these recordings. Subsequently, VCR can replay responses from these recordings, even without network access. Despite utilizing an API key (DEMO_TOKEN), the key itself is not retained in the VCR cassettes. 

    The DEMO_TOKEN's value (or lack thereof) does not affect how VCR replays a response as it filters out the API key from the query parameters. Thus, VCR cannot distinguish between valid or invalid API keys when matching requests to their respective recordings. It matches requests based on the path, method, host, and other non-sensitive query parameters, ensuring the recordings are environment-agnostic.

    To update or add new recordings, utilize the 'new_episodes' mode or remove the cassette file, allowing VCR to capture fresh responses under the default 'once' mode. This approach ensures that changes in the API or its usage can be integrated into the test suite efficiently.

    Note: If authentication details such as DEMO_TOKEN change and you wish to reflect this in tests, a new recording session must be initiated as VCR does not capture authentication data directly due to our filtration of sensitive information.
    """

    def setUp(self):
        self.token = os.getenv('DEMO_TOKEN')