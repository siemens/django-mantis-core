==================
Django Mantis Core
==================

**WARNING: Mantis is not maintained anymore: by now, the excellent MISP platform
(http://www.misp-project.org/)
offers all the functionality (and much more) that had been required when
MANTIS was created but could then not be found in any other tool.**



A wrapper around the Django Dingos application used by the Mantis
Cyber Threat Intelligence Management Framework. The rationale
for this wrapper is to provide a location for 
code specific to cyber threat intelligence management that
is to be added to the underlying models. Such code should
not be added to Dingos, because Dingos is a generic framework.

Please refer to the
documentation and developer guidelines of `Django Dingos`_ and `MANTIS`_.

The full documentation of the Mantis core module is at

http://django-mantis-core.readthedocs.org/en/latest/

.. _Django Dingos: http://django-dingos.readthedocs.org.
.. _MANTIS: http://django-mantis.readthedocs.org.


Acknowledgments
---------------


The basic layout for this Django app with out-of-the-box configuration of ``setup.py`` for
easy build, submission to PyPi, etc., and Sphinx documentation tree was generated with Audrey Roy's excellent `Cookiecutter`_
and Daniel Greenfield's `cookiecutter-djangopackage`_ template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter

.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage


