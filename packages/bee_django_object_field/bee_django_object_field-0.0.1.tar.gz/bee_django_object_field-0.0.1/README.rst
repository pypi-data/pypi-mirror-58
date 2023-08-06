========================
bee_django_object_field
========================

Quick start
-----------

1. Add "message" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'bee_django_object_field.apps.BeeDjangoObjectFieldConfig',
    )

2. Include the crm URLconf in your project urls.py like this::

    from django.conf.urls import include, url
    ...
    url(r'^bee_django_object_field/', include('bee_django_object_field.urls')),


3. Run `python manage.py makemigrations`,`python manage.py migrate` to create the bee_django_object_field models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a message (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/bee_django_object_field/ to participate in the message.

6. Use
from bee_django_object_field.custom_fields import DictField,ListField
dict_field = DictField()
list_field = ListField()