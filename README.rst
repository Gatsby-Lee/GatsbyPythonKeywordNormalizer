Keyword Normalizer
===================

API References
--------------

normalize_searchterm
^^^^^^^^^^^^

1. remove special characters
2. Remove *tab*, *new line*
3. Lower cases

.. code-block:: python

    >>> from gatsby_normalizer import *
    >>> normalize_searchterm('HELLO+WORLD')
    'hello world'
