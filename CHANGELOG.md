## Changelog

Sheepy is a lightweight unit testing framework designed for Python developers who value simplicity and ease of use. It provides a core set of components to write unit tests and generate basic test reports.

### v0.0.4 09/24/2024

### Added

* Added full support for API testing in the Sheepy test framework.
* Implemented `ApiRequests` module for handling HTTP requests (GET, POST, PUT, DELETE) in API tests.
* Introduced new assert methods: `assertStatusCode`, `assertJsonResponse`, and `assertResponseContains` to validate HTTP responses.
* Provided built-in HTTP error handling via the `HttpError` exception class.


### v0.0.3 09/22/2024

### Added

* SheepyTestCase: Implementation of the class that automatically registers and runs tests when inheriting.
* TestOutputFormatter: Module created to format test results, providing a clear and consistent view of the outputs.
* Assertions Module: Creation of a separate module (asserts.py) that includes assertion methods such as assertEqual, assertTrue, assertFalse, and assertRaises.

### Changed

* Test Execution: Modification of the logic in the SheepyTestCase class to run tests when registering subclasses.
* Output Formats: Updated the _output_results method to use TestOutputFormatter, improving the presentation of test results.
* Code Structure: Removed assertion methods from the SheepyTestCase class to centralize the assertion logic in the new module.

### Fixed
* Error Messages: Improvements in error messages for expected failures and tests.

### v0.0.2 09/21/2024

changing the entire project structure, reorganizing and changing use cases. Improving to increasingly optimize unit tests.


### Initial relase 

### Features 

* **Test decoration**: Using the @sheepy decorator to mark functions as test cases.
* **Test discovery**: Automatically finding test cases within a specified class.
* **Test runner**: Executing test cases and collecting results.
* **Basic reporting**: Generating a simple pass/fail report.
* **Logging**: Providing a mechanism for logging test execution details.

