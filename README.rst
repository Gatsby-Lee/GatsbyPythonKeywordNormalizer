Gatsby Normalizer
=================

.. image:: https://img.shields.io/badge/license-AGPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0

.. image:: https://img.shields.io/badge/version-1.0.3-green.svg?style=flat
   :target: https://pypi.org/project/gatsby-normalizer/
   
.. image:: https://img.shields.io/travis/Gatsby-Lee/GatsbyPythonNormalizer.svg
   :target: https://travis-ci.org/Gatsby-Lee/GatsbyPythonNormalizer

Installation
------------

To install gatsby-normalizer, simply:

.. code-block:: bash

    $ sudo pip install gatsby-normalizer

API References
--------------

normalize_searchterm
^^^^^^^^^^^^^^^^^^^^

1. remove special characters
2. Remove *tab*, *new line*
3. Lower cases

.. code-block:: python

    >>> from gatsby_normalizer import *
    >>> normalize_searchterm('HELLO+WORLD')
    'hello world'
