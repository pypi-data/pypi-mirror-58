==============
Glitter Events
==============

Django glitter events for Django.


Installation
============


Getting the code
----------------

You can get **django-glitter-events** by using **pip**:

.. code-block:: console

    $ pip install django-glitter-events

Prerequisites
-------------

Make sure you add ``'glitter_events'``, ``'taggit'`` and ``'adminsortable'`` to your
``INSTALLED_APPS`` setting:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'glitter_events',
        'taggit',
        'adminsortable',
        # ...
    ]

URLconf
-------

Add the Glitter Events URLs to your project’s URLconf as follows:


.. code-block:: python

    url(r'^events/', include('glitter_events.urls', namespace='glitter-events'))



Releasing
---------

Releasing a new version of the project to PyPi is fairly straight forward.

First, make sure you have the correct credentials for PyPi correctly configued on your machine.

Update and commit the Version History in the README.

Then, use ``bumpversion`` to increment the version numbers in the project. This will also create a
commit and a tag automatically for the new version. For example, to increment the version numbers
for a 'patch' release:

.. code-block:: console

    $ bumpversion patch
    $ git push --tags origin master

``bumpversion`` can increment 'patch', 'minor' or 'major' version numbers:

.. code-block:: console

    $ bumpversion [patch | minor | major]

Then release the new version to PyPi:

.. code-block:: console

    $ make release
