from setuptools import setup

setup(package_data={
    'djangorestfilemanager': ['djangorestfilemanager/*',
                              'djangorestfilemanager/migrations/*',
                              'djangorestfilemanager/locale/*',
                              'djangorestfilemanager/locale/es/*',
                              'djangorestfilemanager/locale/en/*',
                              'djangorestfilemanager/locale/en/LC_MESSAGES/*',
                              'djangorestfilemanager/locale/es/LC_MESSAGES/*',
                              'djangorestfilemanager/locale/en/LC_MESSAGES/django.po',
                              'djangorestfilemanager/locale/es/LC_MESSAGES/django.po',
                              'djangorestfilemanager/locale/en/LC_MESSAGES/django.mo',
                              'djangorestfilemanager/locale/es/LC_MESSAGES/django.mo',
                              'djangorestfilemanager/test/*'
                              ]
}, )
