from setuptools import setup

# 1. delete all build/generated files
# 2. python setup.py sdist bdist_wheel
# 3. twine upload dist/*

setup(name='generate_graphene',
      version='0.2.2',
      description='Generate Django-Graphene (graphql) queries and mutations for your Django models ',
      url='http://github.com/joeydebreuk/generate_graphene',
      author='Joey van Breukelen',
      author_email='jabreukelen@gmail.com',
      license='MIT',
      packages=['generate_graphene'],
      install_requires=[
          'graphene',
          'graphene-django',
          'graphene-django-extras',
          'graphql-core',
          'graphql-relay',
          'djangorestframework',
          'Django',
          'typedecorator'
      ],
      zip_safe=False
      )
