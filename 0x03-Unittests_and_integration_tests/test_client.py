#!/usr/bin/env python3

"""
Module containing tests for the GithubOrgClient class.

Verifies the correct behavior of GithubOrgClient's org property.
"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest.mock
from unittest.mock import patch, Mock
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.

    Attributes:
        ORG_URL (str): The base URL for Github organization API requests.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    @parameterized.expand([
        ('google'),  # Test with Google's Github organization
        ('abc')      # Test with a sample Github organization (abc)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Tests the org property of GithubOrgClient.

        Verifies that the org property returns the correct value and that
        the get_json method is called once with the expected URL.

        Args:
            org_name (str): The name of the Github organization to test.
            mock_get_json (Mock): The mocked get_json object.
        """
        # ALWAYS MAKE SURE THAT PATCH IS AFTER PARAMETERIZED
        # Create a GithubOrgClient instance for the given organization
        test_inst = GithubOrgClient(org_name)

        # Call the org method to trigger the get_json call
        test_inst.org()

        # Verify that get_json is called once with the expected URL
        mock_get_json.called_once_with(test_inst.ORG_URL.format(org=org_name))
