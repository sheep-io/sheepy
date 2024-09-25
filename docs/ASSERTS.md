## SHEEPY DOCUMENTATION

### AssertMethods Class Documentation

### Purpose:

The AssertMethods class provides a collection of assertion methods used in unit testing to verify the correctness of code. These methods are designed to raise AssertionError exceptions when expected conditions are not met, making it easier to identify and debug issues in the tested code.

### Methods:

* assertEqual(first, second, msg=None)
* * Purpose: Asserts that two values are equal.

* Parameters:
* * first: The first value to compare.
* * second: The second value to compare.
* * msg: An optional message to include in the AssertionError if the values are not equal.
* Raises:
* * AssertionError: If first is not equal to second.
* * assertNotEqual(first, second, msg=None)
* Purpose: Asserts that two values are not equal.

* Parameters:
* * first: The first value to compare.
* * second: The second value to compare.
* * msg: An optional message to include in the AssertionError if the values are equal.
* Raises:
* * AssertionError: If first is equal to second.
* * assertTrue(expr, msg=None)
* Purpose: Asserts that an expression is true.

* Parameters:
* * expr: The expression to evaluate.
* * msg: An optional message to include in the AssertionError if the expression is not true.
* Raises:
* * AssertionError: If expr is not true.
* * assertFalse(expr, msg=None)
* Purpose: Asserts that an expression is false.

* Parameters:
* * expr: The expression to evaluate.
* * msg: An optional message to include in the AssertionError if the expression is not false.
* Raises:
* * AssertionError: If expr is true.
* * assertRaises(exception, func, *args, **kwargs)
* Purpose: Asserts that a specific exception is raised when a function is called.

* Parameters:
* * exception: The expected exception class.
* * func: The function to call.
* * args: Positional arguments to pass to the function.
* * kwargs: Keyword arguments to pass to the function.   
* Raises:
* * AssertionError: If the expected exception is not raised, or if an unexpected exception is raised.
* * assertStatusCode(response, expected_code)
* Purpose: Asserts that the status code of a HTTP response is as expected.

* Parameters:
* * response: The HTTP response object.
* * expected_code: The expected status code.
* Raises:
* * AssertionError: If the status code is not as expected.
* * assertResponseContains(response, key)
* Purpose: Asserts that a JSON response contains a specific key.

* Parameters:
* * response: The HTTP response object.
* * key: The expected key in the JSON response.
* Raises:
* * AssertionError: If the key is not found in the JSON response.
* * assertJsonResponse(response)
* Purpose: Asserts that a HTTP response is a JSON response.

* Parameters:
* * response: The HTTP response object.
* Raises:
* * AssertionError: If the response content type is not application/json.