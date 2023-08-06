.. django-auto-webassets documentation master file, created by
   sphinx-quickstart on Sun Feb 17 10:08:00 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-auto-webassets's documentation!
=================================================

django-auto-webassets is a Django_ app that automates the creation of webassets_/django-assets_ bundles. Besides these python libraries, it makes heavy use of requirejs_.

The library was written for one particular use-case in mind which will be described here. Contributions are always welcome!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference

Quickstart
----------

Prerequisites
_____________

I assume that you have nodejs_ including npm installed. I also assume that the required javascript packages are declared in the :code:`package.json` file and :code:`npm update` installs these in a folder called :code:`node_modules`. Most importantly, requirejs_ must be one of the required javascript packages.

I also assume that one :code:`.js` file exists that configures requirejs_. Here is an example:

.. code-block:: javascript

   require.config({
       "baseUrl": "/static",

       "nodeRequire": "require",

       "shim": {
           "bootstrap": {"deps": ["jquery"]},
       },

       "paths": {
           "jquery": "jquery/dist/jquery",
           "bootstrap": "bootstrap-sass/assets/javascripts/bootstrap",
       },
   });

Install
_______
.. code::

   pip install django-auto-webassets

This will also install django-assets_ and all necessary dependencies.

Configure
_________

Next, include django-assets_ and django-auto-webassets in the :code:`INSTALLED_APPS` section of the Django_ :code:`settings.py`:

.. code-block:: python

   INSTALLED_APPS = [
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'django_assets',
       'django_auto_webassets'
       ]

And also make sure to include :code:`django_assets.finders.AssetsFinder` in :code:`STATICFILES_FINDERS`:

.. code-block:: python

   STATICFILES_FINDERS = (
       'django.contrib.staticfiles.finders.FileSystemFinder',
       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
       'django_assets.finders.AssetsFinder',
   )

Next, make sure that the :code:`node_modules` folder is included in the :code:`STATICFILES_DIRS`. If the :code:`node_modules` folder is in the base folder of your project, this would look like this:

.. code-block:: python

   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'node_modules'),
       ...
   ]

Also, make sure to the django-auto-webassets where it finds the configuration
file for requirejs_:

.. code-block:: python

   WEBASSETS_PATH_TO_REQUIREJS_CFG = 'requirejs_cfg.js'

For now, I recommend that you turn off optimization and turn on assets debugging:

.. code-block:: python

   WEBASSETS_OPTIMIZE = False
   ASSETS_DEBUG = False

The use case
____________

The use case for this library is that your templates and views are hierarchical and reusable.
You basically have one :code:`base.html` template that basically defines your theme.
Then you extend this template to create one template that displays lists and maybe
another one that displays and processes forms.

As each child-template becomes more specialized, so does the javascript. There is
some javascript that you need on any given page. A page that displays a list might need
the general purpose javascript plus some list-displaying specifics. A specific
view might then need to add the specific javascript for that view but might be
able to use the generic list-displaying template.

django-auto-webassets in conjunction with requirejs_ makes it really easy to
do this adhering to the DRY principle.

Setting up the base template
____________________________

Assuming you have a javascript file called :code:`init_general.js` that does the
general javascript stuff for your pages, add this to your base template:

.. code-block:: html

   {% load auto_webassets %}

   {% block javascript %}
      {% webassets_js "init_general.js" %}
   {% endblock %}

The :code:`webassets` tag automatically adds requirejs_, the requirejs configuration
file you defined above and :code:`init_general.js` to the html output.

Depending on the configuration, it also applies optimization (e.g., bundling...)
and adds the resulting file to the html output.

If you want to use a different javascript file in a child-template, just override
the :code:`javascript` block.

Using a different javascript file in a view
___________________________________________

You can use :class:`django_auto_webassets.views.mixins.AutoWebassetsJSMixin`
to specify a different javascript file for that specific view.

.. attention:: Always include mixins **before** the view class!

.. code-block:: python

   from django_auto_webassets.views.mixins import AutoWebassetsJSMixin
   from django.views.generic import TemplateView

   class MyView(AutoWebassetsJSMixin, TemplateView):
      template_name = 'generic.html'
      webasset_js_file = 'specific_javascript.js'

Now :code:`specific_javascript.js` is used instead of the javascript file
specified in the template.

Build assets by command
_______________________

When optimization is turned on by setting :code:`WEBASSETS_OPTIMIZE = True` in
the :code:`settings.py`, webassets_ needs to build and optimize the javascript
for the website. It normally does that when the specific page is requested
for the first time. However, this takes a few seconds which is not good for
the user experience.

Instead, you can use the management command that comes with django-auto-webassets
to pre-build all bundles:

.. code-block:: bash

   python manage.py webassetsrequirejs

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. include:: links.rst
