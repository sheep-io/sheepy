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

.. code-block:: bash

   pip install sheepy

... 

Usage
-----

Here's a basic example of how to use Sheepy:

.. code-block:: python

   from sheepy import sheepy

   @sheepy
   def test_add():
       assert 2 + 2 == 4

   # ...

... 

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