.. poplar_isocc documentation master file, created by
   sphinx-quickstart on Mon Dec 16 15:43:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

poplar_isocc - Enforce ISO-3166-1 Country Code in Sage 300
==========================================================

This package enforces the use of `ISO-3166-1`_ compliant country codes in any
field in the Sage Desktop.  It contains validation code as well as unit and 
acceptance tests.

.. _ISO-3166-1: https://en.wikipedia.org/wiki/ISO_3166-1

.. toctree::
   :maxdepth: 2

   src/poplar_isocc
   src/tests

``poplar_isocc`` part of a general demonstration of how Python Packaging can be
used with `Orchid Extender`_.  Best consumed with the accompanying
presentation, `Python Packaging for Extender - ISO Country Codes`_ and a cold
beer.

.. _Orchid Extender: https://www.orchid.systems/product/extender
.. _Python Packaging for Extender - ISO Country Codes: https://docs.google.com/presentation/d/1bwtmR2UUGauErDNydI7NCbm0VllSqzt8GJ7aXWfNBsA/

The code in this package is very simple, relying on the `iso3166`_ package for
reference data and performing only a simple validation.  It demonstrates the
key concepts in improving code reuse and distribution for Extender, including:

- leveraging the `extools`_ library for testing
- inclusion of unit and acceptance testing using `ExTestCase`_
- how packaging can make installation, upgrade, and backport a breeze

.. _iso3166: https://pypi.org/project/iso3166/
.. _extools: https://extools.rtfd.io
.. _ExTestCase: https://extools.readthedocs.io/en/latest/src/extest/extest.html#extools.extest.ExTestCase

This package can be used to demonstrate the upgrade and feature backport.
The relevant versions are:

- `v0.1.3`_: enforces two character ISO country codes on A/R Customer Country
- `v0.2.0`_: enforces three character ISO country codes on A/R Customer Country
- `v0.3.7`_: enforces three character ISO country codes on A/R Customer Country
  with fuzzy matching and recommendatons on invalid code.

.. _v0.1.3: https://bitbucket.org/cbinckly/poplar_isocc/src/v0.1.3/
.. _v0.2.0: https://bitbucket.org/cbinckly/poplar_isocc/src/v0.2.0/
.. _v0.3.7: https://bitbucket.org/cbinckly/poplar_isocc/src/v0.3.7/

To demo with this package:

1. Install ``expip``, the Package Manager for Orchid Extender.
2. Open A/R Customers, input the value "CDN" into a new Customer Record.
    
    - The put is successful.

3. Open ``expip`` and install ``poplar_isocc==0.1.3``. This version 
   enforces two character country codes.

4. Open A/R Customers, input the value "CDN" into a new Customer Record.
    
    - The put fails with a message to the user.

5. Input the value "CA" into the new Customer Record.
    
    - The put succeeds silently.

6. Open ``expip`` and install ``poplar_isocc==0.2.0``. This version 
   enforces three character country codes.

7. Open A/R Customers, input the value "CA" into a new Customer Record.
    
    - The put fails with a message to the user.

8. Input the value "CAN" into the new Customer Record.
    
    - The put succeeds silently.

9. Open ``expip``, select ``poplar_isocc`` from the drop-down, and click
   ``Upgrade``. This will install the latest version, which includes fuzzy
   matching to make recommendations on invalid input.

10. Open A/R Customers, input the value "CDN" into a new Customer Record.
    
    - The put fails with a message to the user recommending "CAN"

11. Input the value "CAN" into the new Customer Record.
    
    - The put succeeds silently.

Done.

This package, the `Python Package Manager for Orchid Extender`_, and the 
`extools`_ library were created and are maintained by `2665093 Ontario Inc`_.
Comments and quesions are always welcome, `send an email`_.

.. _Python Package Manager for Orchid Extender: https://2665093.ca/#extender-package-manager
.. _2665093 Ontario Inc: https://2665093.ca
.. _send an email: contact@2665093.ca

