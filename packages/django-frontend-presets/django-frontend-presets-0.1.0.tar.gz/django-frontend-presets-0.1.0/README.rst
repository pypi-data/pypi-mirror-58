=======================
Django Frontend Presets
=======================

Django frontend presets provide a command line that allow you to rapidly
swap the front-end scaffolding for the application.

**Choices are:**
    - reset (reset the inital structure)
    - bootstrap (Setup Bootstrap)
    - vue (Setup VueJs)
    - react (Setup React)

The first time you run the command, it will move templates, static and locale directory
to resources at the root of the project, setup the base structure, write your package.json and webpack.mix.js.

Quick start
-----------
1. Install python dependencies.
    `pip install django-frontend-presets --extra-index-url https://api.packagr.app/xKNhDZcWW/`

2. Add "django_frontend_presets" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_frontend_presets.apps.DjangoFrontendPresetsConfig',
    ]

3. Run the "preset" command to generate the base structure.
    `python manage.py preset [reset, bootstrap, vue, react]`

4. Install javascript dependencies.
    `npm install && npm run dev`

5. Update your Django settings::

    LOCALE_PATHS = [str(ROOT_DIR.path("resources", "locale"))]

    STATICFILES_DIRS = [str(ROOT_DIR.path("resources", "static"))]

    TEMPLATES[0]['DIRS'] = [str(ROOT_DIR.path("resources", "templates"))]

6. Enjoy :)

Credit
------
The webpack configuration used came from `Laravel Mix <https://github.com/JeffreyWay/laravel-mix>`_
made by `Jeffrey Way <https://laracasts.com/>`_.