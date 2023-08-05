from setuptools import setup, find_packages

setup(name='djangorestfilemanager',
      version='0.3.5',
      description='Django REST File Manager',
      url='https://gitlab.com/kas-factory/packages/django-rest-file-manager',
      author='Avelino @ KF',
      author_email='avelino@kasfactory.net',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      package_data={
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
      },
      install_requires=[
            'boto3>=1.10.35',
            'Django>=2.0',
            'djangorestframework>=3.0',
            'django-filter>=2.2.0',
            'django-storages>=1.8',
            'PyJWT>=1.7.1',
            'pytest-django>=3.7.0'
      ],
      zip_safe=False
      )
