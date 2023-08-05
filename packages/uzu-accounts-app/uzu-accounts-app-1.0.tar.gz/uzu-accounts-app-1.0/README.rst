AccountsApp
===========

This is the official API documentation for the AccountsApp Django
Application.

AccountsApp is a generic django application tailored to Single Page
Applications that abstracts user authentication and verification from
the rest of your project.

AccountsApp will use the model set with ``AUTH_USER_MODEL`` in
settings.py of your django project or the default user model of
``django.contrib.auth``

Also note that AccountsApp requires that the authentication model used
has the following fields;

::

    first_name
    last_name
    email
    username
    password

AccountsApp also enforces a unique contraint on accounts' ``email``
fields.

Installation
------------

Add ``AccountsApp.urls`` to your project's URLConf

.. code:: python

    urlpatterns = [
        ...
        path("accounts/", include("AccountsApp.urls"))
    ]

Add the AccountsApp to your ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = [
        ...
        "AccountsApp.apps.AccountsappConfig"
    ]

Setup the ``ACCOUNTS_APP`` settings variable in settings.py

.. code:: python

    ACCOUNTS_APP = {
        "base_url": "",         # Base url pattern for the AccountsApp urls
        "redirect_link": "",    # Link redirected to after link verification 
        "code_length": 3,       # specifies the length of the verification code
        "sign_in_after_verification": False     # Specify if to sign in after verification is successful
    }

Then apply migrations

.. code:: bash

    python manage.py migrate

API
---

The app communicates with the client-side using basic api calls.

API responses have the following basic format:

.. code:: javascript

        {
            status: Boolean,         //  status of the API call
            data: Object,            //  payload
            error: String            //  error string in case an error occurs (status == False)
        }

API List
~~~~~~~~

NB: The illustrations below assume that the app's urls were mapped to
the ``accounts/`` path.

1. sign-in
^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/sign-in/", {
            username: "",           // this could be username or email
            password: "",
            keepSignedIn: true      // keeps the user signed in (optional)
        })

2. sign-up
^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/sign-up/", {
            username: "",
            email: "",
            first_name: "",
            last_name: "",
            password: "",
            keepSignedIn: true      // keeps the user signed in (optional)
        })

3. sign-out
^^^^^^^^^^^

.. code:: javascript

        axios.get("/accounts/sign-out/")

4. authenticate
^^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/authenticate/", {
            password: ""
        })

5. reset-password
^^^^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/reset-password/", {
            username: "",
            code: "",           // verification code. This comes from send-verification-code 
            newPassword: "",
        })

6. change-password
^^^^^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/change-password/", {
            newPassword: "",
            oldPassword: ""
        })

7. send-verification-code
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/send-verification-code/", {
            username: "",       // optional username (will use request.user.username if a user is signed in when this field is not specified. Fails otherwise)
            mode: "",           // (send || resend) optional mode (will use 'resend' by default, if set to 'send', the verification code is updated before sending) 
        })

8. send-verification-link
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/send-verification-code/", {
            username: "",       // optional username (will use request.user.username if a user is signed in when this field is not specified. Fails otherwise)
            mode: "",           // (send || resend) optional mode (will use 'resend' by default, if set to 'send', the verification code is updated before sending) 
        })

9. verify-code
^^^^^^^^^^^^^^

.. code:: javascript

        axios.post("/accounts/verify-code/", {
            username: "",       
            code: "",           
        })
