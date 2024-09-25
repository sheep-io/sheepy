.. _sheepy:

Sheepy: A Simple Python Unit Testing library

====================================================

Introduction
------------

Sheepy is a lightweight unit testing library designed for Python developers who value simplicity and ease of use. It provides a core set of components to write unit tests and generate basic test reports.
 

Installation
----------

To install Sheepy, simply:

``` bash

   pip install sheepy

``` 

Assert Methods Overview

```
+-----------------------+-------------------------------------------------------+
| Assertion Method       | Description                                           |
+-----------------------+-------------------------------------------------------+
| assertEqual(a, b)      | Checks if two values are equal.                       |
| assertNotEqual(a, b)   | Checks if two values are not equal.                   |
| assertTrue(expr)       | Verifies that the expression is True.                 |
| assertFalse(expr)      | Verifies that the expression is False.                |
| assertRaises(exc, fn)  | Asserts that a function raises a specific exception.  |
| assertStatusCode(resp) | Verifies if the response has the expected status code.|
| assertJsonResponse(resp)| Confirms the response is in JSON format.             |
| assertResponseContains(resp, key) | Ensures the response contains a given key. |
+-----------------------+-------------------------------------------------------+
```

Usage
-----

Here's a basic example of how to use Sheepy:

``` python

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


suite = TestSuite([ExampleTest])
runner = TestRunner(suite)
runner.run()

```
 

Output
-------

```
Test Results:
ExampleTest.test_error: FAIL - Forced error
ExampleTest.test_expected_failure: EXPECTED FAILURE
ExampleTest.test_failure: FAIL - 1 != 2
ExampleTest.test_skipped: SKIPPED -
ExampleTest.test_success: OK
```


Api test case
--------------

API testing in the Sheepy Test Framework is designed to be straightforward yet powerful, allowing testers to interact with APIs using common HTTP methods such as GET, POST, PUT, and DELETE. The framework provides a dedicated class, ApiRequests, to simplify sending requests and handling responses, with built-in error management via the HttpError exception class.

When testing an API, the test class inherits from SheepyTestCase, which is equipped with various assertion methods to verify the behavior of the API. These include assertStatusCode to validate HTTP status codes, assertJsonResponse to ensure the response is in JSON format, and assertResponseContains to check if specific keys exist in the response body.

For instance, the framework allows you to send a POST request to an API, verify that the status code matches the expected value, and assert that the JSON response contains the correct data. The API requests are handled through the ApiRequests class, which takes care of constructing and sending the requests, while error handling is streamlined by raising HTTP-specific errors when the server returns unexpected status codes.

By providing built-in assertions and error handling, the framework automates much of the repetitive tasks in API testing, ensuring both correctness and simplicity in writing tests. This system allows developers to focus on verifying API behavior and logic, making it an efficient tool for ensuring the reliability of API interactions.

``` Python
from sheepy.sheeptest import SheepyTestCase  

class TestHttpBinApi(SheepyTestCase):
    def __init__(self):
        
        super().__init__(base_url="https://httpbin.org")

    def test_get_status(self):
        
        response = self.api.get("/status/200")
        self.assertStatusCode(response, 200)  

    def test_get_json(self):
        
        response = self.api.get("/json")
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "slideshow")  

    def test_post_data(self):
        
        payload = {"name": "SheepyTest", "framework": "unittest"}
        response = self.api.post("/post", json=payload)
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "json") 
        self.assertEqual(response.json()["json"], payload)  

    def test_put_data(self):
        
        payload = {"key": "value"}
        response = self.api.put("/put", json=payload)
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "json")  
        self.assertEqual(response.json()["json"], payload)  

    def test_delete_resource(self):
        
        response = self.api.delete("/delete")
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
```

Output example
---------------

```
Test Results:
TestHttpBinApi.test_delete_resource: OK
TestHttpBinApi.test_get_json: OK
TestHttpBinApi.test_get_status: OK
TestHttpBinApi.test_post_data: OK
TestHttpBinApi.test_put_data: OK
```


Customization
-------------

Sheepy allows for customization in several ways:

```
+------------------+------------------------------------------------------------+
| Feature           | Description                                                |
+------------------+------------------------------------------------------------+
| Logging           | Customizable logging mechanisms for test results.          |
| Reporting         | Support for different reporting formats (e.g., JSON, XML). |
| Test Discovery    | Flexible discovery mechanisms for tests.                   |
+------------------+------------------------------------------------------------+
```

API Reference
-------------

.. automodule:: sheepy
   :members:
   :undoc-members:
   :show-inheritance:
