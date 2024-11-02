#!/usr/bin/env python3
"""
Testing module for utils.access_nested_map.

This module contains unit tests for the access_nested_map function,
verifying its ability to retrieve values from nested maps.
"""

import unittest
import utils
from parameterized import parameterized


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
