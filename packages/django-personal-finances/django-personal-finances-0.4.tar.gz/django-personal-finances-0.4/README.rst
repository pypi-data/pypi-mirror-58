Personal Finance
================

Personal Finance is a Django app to keep track of your personal
finances. It allows users to set budgeting goals and track how 
they are doing over time.

Detailed documentation is in the "docs" directory.

Quick start
-----------

#. Add "finances" to your INSTALLED\_APPS setting like this:

.. code:: python

    INSTALLED_APPS = [
        ...
        'finances',
    ]

#. Include the polls URLconf in your project urls.py like this:

.. code:: python

    path('', include("finances.urls")),

#. Run ``python manage.py migrate`` to create the polls models.
