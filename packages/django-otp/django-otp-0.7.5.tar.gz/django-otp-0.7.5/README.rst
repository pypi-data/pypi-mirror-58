.. image:: https://img.shields.io/pypi/v/django-otp?color=blue
   :target: https://pypi.org/project/django-otp/
   :alt: PyPI
.. image:: https://img.shields.io/readthedocs/django-otp-official
   :target: https://django-otp-official.readthedocs.io/
   :alt: Documentation
.. image:: https://img.shields.io/badge/github-django--otp-green
   :target: https://github.com/django-otp/django-otp
   :alt: Source

This project makes it easy to add support for `one-time passwords
<http://en.wikipedia.org/wiki/One-time_password>`_ (OTPs) to Django. It can be
integrated at various levels, depending on how much customization is required.
It integrates with ``django.contrib.auth``, although it is not a Django
authentication backend. The primary target is developers wishing to incorporate
OTPs into their Django projects as a form of `two-factor authentication
<http://en.wikipedia.org/wiki/Two-factor_authentication>`_.

This project includes several simple OTP plugins and more are available
separately. This package also includes an implementation of OATH `HOTP
<http://tools.ietf.org/html/rfc4226>`_ and `TOTP
<http://tools.ietf.org/html/rfc6238>`_ for convenience, as these are standard
OTP algorithms used by multiple plugins.

.. _upgrade notes: https://django-otp-official.readthedocs.io/#upgrading
