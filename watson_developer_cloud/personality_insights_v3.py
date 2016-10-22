# Copyright 2016 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The v3 Personality Insights service
(https://www.ibm.com/watson/developercloud/personality-insights.html)
"""

import json
from .watson_developer_cloud_service import WatsonDeveloperCloudService

class PersonalityInsightsV3(WatsonDeveloperCloudService):

    """Wrapper for the Personality Insights service"""
    default_url = 'https://gateway.watsonplatform.net/personality-insights/api'
    default_version = '2016-10-20'

    def __init__(self, version=default_version, url=default_url, **kwargs):
        """
        Constructs an instance of the service. Fetches service parameters
        from VCAP_SERVICES runtime variable for Bluemix or defaults to local
        URLs.
        :param version: The version of the API to be used in YYYY-MM-DD format (for example, '2016-10-20')
        """

        WatsonDeveloperCloudService.__init__(
            self, 'personality_insights', url, **kwargs)
        self.version = version

    def profile(self, text, content_type=None, content_language=None,
                accept=None, accept_language=None, raw_scores=None,
                consumption_preferences=None, csv_headers=None):

        """
        Returns a personality profile with normalized percentile scores
        given at least 100 words of input text. Content type is detected
        automatically.
        :param text: The input text to be analyzed
        :param content_type: Type of the input text: 'text/plain' (default), 'text/html', or 'application/json'; for plain text or HTML, include the charset parameter to indicate the character encoding
        :param content_language: Language of the input text: 'ar', 'en' (default), 'es', or 'ja'
        :param accept: Type of the response: 'application/json' (default) or 'text/csv'
        :param accept_language: Language of the response: 'ar', 'de', 'en' (default), 'es', 'fr', 'it', 'ja', 'ko', 'pt-br', 'zh-cn', or 'zh-tw'
        :param raw_scores: If True, returns percentage scores not compared with a sample population in addition to normalized scores
        :param consumption_preferences: If True, returns consumption preferences in addition to normalized scores
        :param csv_headers: If True, returns a row of headers for CSV output
        """

        if content_type == 'application/json' and isinstance(text, dict):
            text = json.dumps(text)

        headers = {
            'content-type': content_type,
            'content-language': content_language,
            'accept': accept,
            'accept-language': accept_language
        }

        params = {'version': self.version}

        if raw_scores:
            params['raw_scores'] = 'true'

        if consumption_preferences:
            params['consumption_preferences'] = 'true'

        if csv_headers:
            params['csv_headers'] = 'true'

        response = self.request(
            method='POST', url='/v3/profile', data=text,
            params=params, headers=headers
        )

        if accept == 'test/csv':
            return response.text
        else:
            return response.json()
