#Single Login


Single login is a Django app that will restrict concurrent login.


**Quick start**


1. Add "singlelogin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'singlelogin',
    ]

2. Add "singlelogin.middleware.OneSessionPerUserMiddleware" to your MIDDLEWARE like this::

    MIDDLEWARE = [
        ...
        'singlelogin.middleware.OneSessionPerUserMiddleware',
    ]

3. Run `python manage.py migrate` to create the singlelogin models.

4. That is all.
