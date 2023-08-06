.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==================
rt.categorysupport
==================

.. image:: https://travis-ci.org/PloneGov-IT/rt.categorysupport.svg?branch=master
    :target: https://travis-ci.org/PloneGov-IT/rt.categorysupport

Plugin that add a new "Taxonomies" field to content-types.


Features
--------

- Fixed list of available taxonomies
- View for folder contents to show a list of contained objects' taxonomies


Available taxonomies
--------------------

There is a control panel (@@taxonomy-settings) where you can set available taxonomies that users can choose.

Examples
--------

This add-on can be seen in action at the following sites:

- `Emilia-Romagna Sociale`__

__ https://sociale.regione.emilia-romagna.it/documentazione


Translations
------------

This product has been translated into

- Italian


Installation
------------

Install rt.categorysupport by adding it to your buildout::

    [buildout]

    ...

    eggs =
        rt.categorysupport


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/PloneGov-IT/rt.categorysupport/issues
- Source Code: https://github.com/PloneGov-IT/rt.categorysupport


License
-------

The project is licensed under the GPLv2.
