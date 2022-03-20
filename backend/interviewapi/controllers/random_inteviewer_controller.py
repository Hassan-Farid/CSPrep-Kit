# -*- coding: utf-8 -*-

"""
interviewapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from interviewapi.api_helper import APIHelper
from interviewapi.configuration import Server
from interviewapi.controllers.base_controller import BaseController


class RandomInteviewerController(BaseController):

    """A Controller to access Endpoints in the interviewapi API."""
    def __init__(self, config):
        super(RandomInteviewerController, self).__init__(config)

    def interview(self):
        """Does a GET request to /questions.json.

        Generates a random interview question from collection of questions

        Returns:
            string: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/questions.json'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded