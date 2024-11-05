# README

## Project Overview

This project contains a collection of unit tests for various Python modules. The tests are designed to ensure the correctness and reliability of the modules.

## Author

Mohammad Omar Siddiq

## Modules and Tests

### 1. `test_utils.py`

This module contains tests for the `utils` module.

#### Tests

* `TestAccessNestedMap`: Tests the `access_nested_map` function.
	+ `test_access_nested_map`: Tests the function with various inputs.
	+ `test_access_nested_map_exception`: Tests the function with inputs that raise a `KeyError`.
* `TestGetJson`: Tests the `get_json` function.
	+ `test_get_json`: Tests the function with various inputs.
* `TestMemoize`: Tests the `memoize` decorator.
	+ `test_memoize`: Tests the decorator with a simple class.

### 2. `test_client.py`

This module contains tests for the `client` module.

#### Tests

* `TestGithubOrgClient`: Tests the `GithubOrgClient` class.
	+ `test_org`: Tests the `org` property.
	+ `test_public_repos_url`: Tests the `_public_repos_url` property.
	+ `test_public_repos`: Tests the `public_repos` property.
	+ `test_has_license`: Tests the `has_license` method.

## Running the Tests

To run the tests, use the following command:

```bash
python -m unittest discover
```

This will discover and run all tests in the `test_utils.py` and `test_client.py` modules.

## Requirements

* Python 3.6+
* `unittest` module
* `parameterized` module
* `requests` module (for `test_utils.py`)
* `client` module (for `test_client.py`)

## Notes

* The tests are designed to be independent and can be run in any order.
* The tests use the `unittest` framework and the `parameterized` module for parameterized testing.
* The tests use the `requests` module for mocking HTTP requests.
* The tests use the `client` module for testing the `GithubOrgClient` class.
