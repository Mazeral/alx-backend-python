#!/usr/bin/env python3
"""
Testing module for utils.access_nested_map.

This module contains unit tests for the access_nested_map function,
verifying its ability to retrieve values from nested maps.
"""

import unittest
import utils
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
        ({}, {"a", }, ),  # Empty map with non-existent key
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
    """
    Test case for the `get_json` function in the `utils` module.

    Verifies the correct behavior of `get_json` when fetching JSON data
    from URLs.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),  # Test with example URL
        # and payload
        ("http://holberton.io", {"payload": False})  # Test with Holberton URL
        # and no payload
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests the `get_json` function with mocked GET requests.

        Args:
            test_url (str): The URL to test with.
            test_payload (dict): The expected JSON payload.
            mock_get (Mock): The mocked `requests.get` object.

        Returns:
            None
        """
        # Configure the Mock
        # @patch('requests.get') ensures no actual GET requests are made
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        """
         Mocking the `requests.get` call:
         mock_get (requests.get) -> mock_response (response object)
                                |
                                |  test_url (argument)
                                v
          mock_get.assert_called_once_with(test_url)  # Correct assertion
        """
        mock_get.return_value = mock_response

        # Call the function being tested
        result = utils.get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)  # Verify the URL was
        # called once
        self.assertEqual(result, test_payload)  # Verify the returned payload
        # matches the expected payload


class TestMemoize(unittest.TestCase):
    """
    Test case for the `memoize` decorator in the `utils` module.

    Verifies the correct behavior of `memoize` in caching property values.
    """

    def test_memoize(self):
        """
        Tests the `memoize` decorator with a sample class and property.

        Ensures that the decorated property is only evaluated once and its
        value is cached for subsequent accesses.
        """
        # Define a test class with a method and a memoized property
        class TestClass:
            """
            A test class for demonstrating the `memoize` decorator.

            Attributes:
                a_method (method): A simple method returning a constant value.
                a_property (property): memoized property relying on `a_method`
            """

            def a_method(self):
                """
                A sample method returning a constant value.

                Returns:
                    int: The constant value 42.
                """
                return 42

            @utils.memoize
            def a_property(self):
                """
                A memoized property relying on `a_method`.

                Returns:
                    int: The cached result of `a_method`.
                """
                return self.a_method()

        # Create an instance of the test class for testing
        test_class = TestClass()

        # Use `patch.object` to mock the `a_method` for testing
        with patch.object(test_class, 'a_method') as mock_a_method:
            """
            Mock the `a_method` to control its return value and track its calls
            """
            # Set the mock return value
            mock_a_method.return_value = 42

            # Access the memoized property twice to test caching
            result1 = test_class.a_property
            result2 = test_class.a_property

            # Assertions
            # Verify the first access returns the expected value
            self.assertEqual(result1, 42)
            # Verify the second access returns the same value
            self.assertEqual(result2, 42)
            # Verify `a_method` was called only once
            mock_a_method.assert_called_once()
