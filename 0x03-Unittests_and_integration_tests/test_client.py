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
from fixtures import TEST_LOAD


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

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """
        Tests the `public_repos` method of `GithubOrgClient`.

        Verifies that the method returns a list of public repository names and
        that the `_public_repos_url` property and `get_json` function are
        called correctly.

        Args:
            mock_get_json (Mock): The mocked `get_json` function.
        """
        # Mocking get_json with a list of repository payloads
        payloads = [
            {"id": 1, "name": "repo1", "license": {"key": "MIT"}},
            {"id": 2, "name": "repo2", "license": {"key": "Apache-2.0"}},
            {"id": 3, "name": "repo3", "license": {"key": "MIT"}},
            {"id": 4, "name": "repo4", "license": {"key": "GPL-3.0"}},
        ]
        # Sample repository payloads with id, name, and license information.
        mock_get_json.return_value = payloads
        # Set the return value of the mocked get_json function to the sample
        # payloads.

        # Mocking the _public_repos_url property with a custom URL
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            # Mock the _public_repos_url property to control its return value.
            mock_public_repos_url.return_value = "https://api.github.com/repos"
            # Set the return value of the mocked _public_repos_url property
            # to a custom URL.

            # Create a GithubOrgClient instance for the given organization
            test_insta = client.GithubOrgClient('test')
            # Initialize a GithubOrgClient instance for testing with the
            # 'test-org' organization.

            # Call the public_repos method and store the result
            actual_result = test_insta.public_repos()
            # Retrieve the list of public repository names for the test
            # organization.

            # Define the expected result based on the mock payloads
            expected_result = [payload["name"] for payload in payloads]
            # Extract the repository names from the mock payloads for
            # comparison.

            # Assertions
            self.assertEqual(expected_result, actual_result)
            # Verify that the actual result matches the expected list of
            # repository names.

            mock_public_repos_url.assert_called_once()

            # Verify that the _public_repos_url property was called once
            # during the test.

            mock_get_json.assert_called_once()

            # Verify that the get_json function was called once during
            # the test.

    @parameterized.expand([
        # Test case with matching license key
        ({"license": {"key": "my_license"}}, "my_license"),
        # Test case with non-matching license key
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, repo, license_key):
        """
        Test the has_license method of GithubOrgClient.

        Args:
            repo (dict): A dictionary representing a repository.
            license_key (str): The license key to check for.

        Returns:
            None
        """
        # Calculate the expected result
        expected_value = repo['license']['key'] == license_key
        # Get the actual result from the has_license method
        actual_value = GithubOrgClient.has_license(repo, license_key)
        # Assert that the expected and actual results are equal
        self.assertEqual(expected_value, actual_value)


"""
        When you assign the dictionary to mock_get.return_value,
        you're essentially creating a shared state across all test
        class instances. This means that:

        Every time requests.get() is called, it will return the same
        dictionary, which contains all the fixtures.
        The dictionary is not magically updated to reflect the specific
        instance attributes (self.org_payload, etc.) of each test class
        instance.
"""
# WONT WORK!!!
# mock_get.return_value = {"org_payload": self.org_payload,
# "repos_payload": self.repos_payload,
# "expected_repos": self.expected_repos,
# "apache2_repos": self.apache2_repos}
# starting the patcher of requests.get


@parameterized_class(["org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    def setUpClass(self):
        get_patcher = patch('requests.get')

        def get_payload_for_url(url):
            get_patcher.start()
            get_patcher.side_effect = []

    def tearDownClass(self, patcher):
        patcher.stop()
