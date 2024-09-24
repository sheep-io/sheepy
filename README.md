# sheepy 🐑 

![Python Version](https://img.shields.io/badge/python-v3.8%7C3.9%7C3.10%7C3.11%7C3.12-blue)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sheepy?color=blue)](https://pypi.org/project/sheepy/)
[![PyPI - Version](https://img.shields.io/pypi/v/sheepy?color=blue)](https://pypi.org/project/sheepy/)


Sheepy is a lightweight unit testing framework designed for Python developers who value simplicity and ease of use. It provides a core set of components to write unit tests and generate basic test reports.

![Logo](./img/logo.png)

### Features

* **Test decoration**: Using the @sheepy decorator to mark functions as test cases.
* **Test discovery**: Automatically finding test cases within a specified class.
* **Test runner**: Executing test cases and collecting results.
* **Basic reporting**: Generating a simple pass/fail report.
* **Logging**: Providing a mechanism for logging test execution details.

### Installation

``` bash
pip install sheepy
```

### Usage

Here's a basic example of how to use Sheepy:

``` Python
from sheepy.sheeptest import SheepyTestCase

class ExampleTest(SheepyTestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_failure(self):
        self.assertEqual(1, 2)

    def test_error(self):
        raise Exception("Forced error")

    @SheepyTestCase.skip("Reason to ignore")
    def test_skipped(self):
        pass

    @SheepyTestCase.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)

```

### Example output

```
Test Results:
ExampleTest.test_error: FAIL - Forced error
ExampleTest.test_expected_failure: EXPECTED FAILURE
ExampleTest.test_failure: FAIL - 1 != 2
ExampleTest.test_skipped: SKIPPED -
ExampleTest.test_success: OK
```

### Api test case

API testing in the Sheepy Test Framework is designed to be straightforward yet powerful, allowing testers to interact with APIs using common HTTP methods such as GET, POST, PUT, and DELETE. The framework provides a dedicated class, ApiRequests, to simplify sending requests and handling responses, with built-in error management via the HttpError exception class.

When testing an API, the test class inherits from SheepyTestCase, which is equipped with various assertion methods to verify the behavior of the API. These include assertStatusCode to validate HTTP status codes, assertJsonResponse to ensure the response is in JSON format, and assertResponseContains to check if specific keys exist in the response body.

For instance, the framework allows you to send a POST request to an API, verify that the status code matches the expected value, and assert that the JSON response contains the correct data. The API requests are handled through the ApiRequests class, which takes care of constructing and sending the requests, while error handling is streamlined by raising HTTP-specific errors when the server returns unexpected status codes.

By providing built-in assertions and error handling, the framework automates much of the repetitive tasks in API testing, ensuring both correctness and simplicity in writing tests. This system allows developers to focus on verifying API behavior and logic, making it an efficient tool for ensuring the reliability of API interactions.

``` Python
from sheepy.sheeptest import SheepyTestCase  

class TestHttpBinApi(SheepyTestCase):
    def __init__(self):
        # Passing the base_url of the httpbin.org API to the test class
        super().__init__(base_url="https://httpbin.org")

    def test_get_status(self):
        """Testing the GET /status/200 endpoint"""
        response = self.api.get("/status/200")
        self.assertStatusCode(response, 200)  # Check if the status code is 200

    def test_get_json(self):
        """Testing the GET /json endpoint to validate the JSON response"""
        response = self.api.get("/json")
        self.assertStatusCode(response, 200)  # Check if the status code is 200
        self.assertJsonResponse(response)  # Check if the response is JSON
        self.assertResponseContains(response, "slideshow")  # Verify if the key "slideshow" exists in the response

    def test_post_data(self):
        """Testing the POST /post endpoint by sending data in the body"""
        payload = {"name": "SheepyTest", "framework": "unittest"}
        response = self.api.post("/post", json=payload)
        self.assertStatusCode(response, 200)  # Check if the status code is 200
        self.assertJsonResponse(response)  # Check if the response is JSON
        self.assertResponseContains(response, "json")  # Verify if the response contains the "json" key
        self.assertEqual(response.json()["json"], payload)  # Ensure the sent data matches the received data

    def test_put_data(self):
        """Testing the PUT /put endpoint by sending data"""
        payload = {"key": "value"}
        response = self.api.put("/put", json=payload)
        self.assertStatusCode(response, 200)  # Check if the status code is 200
        self.assertJsonResponse(response)  # Check if the response is JSON
        self.assertResponseContains(response, "json")  # Verify if the response contains the "json" key
        self.assertEqual(response.json()["json"], payload)  # Ensure the sent data matches the received data

    def test_delete_resource(self):
        """Testing the DELETE /delete endpoint"""
        response = self.api.delete("/delete")
        self.assertStatusCode(response, 200)  # Check if the status code is 200
        self.assertJsonResponse(response)  # Check if the response is JSON
```

### Output example

```
Test Results:
TestHttpBinApi.test_delete_resource: OK
TestHttpBinApi.test_get_json: OK
TestHttpBinApi.test_get_status: OK
TestHttpBinApi.test_post_data: OK
TestHttpBinApi.test_put_data: OK
```

### Customization

Sheepy allows for customization in several ways:

* **Logging:** 
* **Reporting:** 
* **Test discovery:** 
