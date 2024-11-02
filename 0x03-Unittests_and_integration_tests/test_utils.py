#!/usr/bin/env python3
"""
Testing module for utils.access_nested_map.

This module contains unit tests for the access_nested_map function,
verifying its ability to retrieve values from nested maps.
"""

import unittest, utils
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for utils.access_nested_map.

    Contains a parameterized test method to validate the function's
    behavior with various input scenarios.
    """

    # The decoration here is to make the unit test multiple inputs
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),  # Simple key-value pair
            ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Nested map with single key
            ({"a": {"b": 2}}, ("a", "b"), 2)  # Nested map with multiple keys
                        ])
    def test_access_nested_map(self, nested_map: dict,
                               path: tuple, expected_result: any) -> None:
        """
        Tests utils.access_nested_map with various input scenarios.

        Args:
            nested_map (dict): The input nested map.
            path (tuple): The key path to the desired value.
            expected_result (any): The expected result from the function.

        Returns:
            None
        """
        self.assertEqual(utils.access_nested_map(nested_map, path),
                         expected_result)

    # When expecting an error, we don't pass expected results
    @parameterized.expand([
        ({}, {"a",}, ),  # Empty map with non-existent key
        ({"a": 1}, {"a", "b"}, )  # Map with single key,
        # attempting to access non-existent nested key
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: set) -> None:
        """
        Tests that utils.access_nested_map raises a KeyError for invalid paths.

        Args:
            nested_map (dict): The input nested map.
            path (set): The key path that is expected to raise a KeyError.

        Returns:
            None
        """
        with self.assertRaises(KeyError):
            # Attempt to access the nested map with the given path,
            # expecting a KeyError
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
                          ])
    @patch('requests.get') # to make sure that no get requests are actually made
    def test_get_json(self, test_url, test_payload, mock_get):
        # Configure the Mock
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # We got this from the @patch('requests.get')
        mock_get.return_value = mock_response

        # Call the function being tested
        result = utils.get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
