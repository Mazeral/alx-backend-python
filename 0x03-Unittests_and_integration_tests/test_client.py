#!/usr/bin/env python3

"""
Module containing tests for the GithubOrgClient class.

Verifies the correct behavior of GithubOrgClient's org property.
"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest.mock
from unittest.mock import patch, Mock, PropertyMock
import requests
import client


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

    @parameterized.expand([
        ('google'),  # Test with Google's Github organization
        ('abc')      # Test with a sample Github organization (abc)
    ])
    def test_public_repos_url(self, org_name):
        """
        Tests the `_public_repos_url` property of `GithubOrgClient`.

        Verifies that the property returns the expected URL for the given
        organization.

        Args:
            org_name (str): The name of the Github organization to test.
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            """
            Mock the `_public_repos_url` property to control its return value.

            :param mock_public_repos_url: The mocked property object.
            """
            # Create a GithubOrgClient instance for the given organization
            test_insta = client.GithubOrgClient(org_name)

            # Define the expected URL based on the organization name
            expected_url = f'https://api.github.com/orgs/{org_name}/repos'
            """
            In testing, we define the result which we want, and compare it
            To the test we actually get from the functions, methods and other
            Things to know if they are actually working as intended

            In the case of mocks:
            Mocks being the values we create and make it (how it should work)
            The original methods, functions and test it (how it actually works)
            """

            # Set the return value of the mocked property
            mock_public_repos_url.return_value = expected_url

            # Assert that the property returns the expected URL
            self.assertEqual(test_insta._public_repos_url, expected_url)
