=============================
django-colorinput
=============================

Color fields for forms and models using HTML5's native input element of type color.


Quickstart
----------

Install `django-colorinput` and add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        …
        'colorinput.apps.ColorInputConfig',
        …
    )

Now you can use `ColorField` in your models:

.. code-block:: python

    from django.db import models

    from colorinput.models import ColorField

    class MyModel(models.Model):
        …
        color = ColorField(default="d0d0d0")
	…

In forms, the color field will be displayed using HTML5's native color type
input element. In your own templates, you could use the value stored in the
field like this:

.. code-block:: HTML

    <span style="color: #{{ object.color }}">

… or however you want, really. Just keep in mind that the value is stored as
RGB in triple HEX format *without* the leading "#" (hash symbol).
