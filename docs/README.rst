.. _sheepy:

Sheepy: A Simple Python Unit Testing Framework

====================================================

Introduction
------------

Sheepy is a lightweight unit testing framework designed for Python developers who value simplicity and ease of use. It provides a core set of components to write unit tests and generate basic test reports.

... 

Installation
----------

To install Sheepy, simply:

``` bash

   pip install sheepy

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
 

Customization
-------------

Sheepy allows for customization in several ways:

* **Logging:** ...
* **Reporting:** ...
* **Test discovery:** ...

... (continue with customization options)

API Reference
-------------

.. automodule:: sheepy
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`