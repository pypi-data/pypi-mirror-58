Reference
=========

Settings
--------

django-auto-webassets provides the following Django_ settings:

WEBASSETS_JS_FOLDER
    Standard folder for the javascript files of the views. Default: :code:`js_for_views`

WEBASSETS_PATH_TO_REQUIREJS
    The full relative path to :code:`requirejs.js` relative to one place that Django_'s staticfile finder algorithm searches. Default: :code:`requirejs/require.js`

WEBASSETS_PATH_TO_REQUIREJS_CFG
    The full relative path to :code:`requirejs.cfg.js` relative to one place that Django_'s staticfile finder algorithm searches. Default: :code:`requirejs_cfg.js`

WEBASSETS_SCRAMBLE_OUT_JS
    By default, the name of the generated javascript file contains the full
    module path of the view. This should not lead to any security risks
    because the code of the web application should not be accessible anyhow
    to the user. Anyhow, if you want uuid names, set this to true.
    Default: :code:`False`.

WEBASSETS_R_JS
    The full relative path to :code:`r.js` relative to one place that Django_'s staticfile finder algorithm searches. Default: :code:`node_modules/.bin/r.js`

WEBASSETS_OPTIMIZE
    If this is set to true, standard optimizations (minifying etc.) are run
    on the resulting javascript file. Default: :code:`True`.

Template Tags
-------------

django-auto-webassets provides one template tag to include the generated bundle
in a template.

webassets_js
    You should put this tag somewhere in your template where javascript is
    expected. Please refer to the :doc:`main documentation <index>`.

Mixins
------

.. automodule:: django_auto_webassets.views.mixins
    :members: AutoWebassetsJSMixin

Commands
--------

webassetsrequirejs
    Build assets defined by the :class:`django_auto_webassets.views.mixins.AutoWebassetsJSMixin` mixin.

.. include:: links.rst