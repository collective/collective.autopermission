from setuptools import setup, find_packages
import os

version = '1.0b3dev'

setup(name='collective.autopermission',
      version=version,
      description="Create permissions in Zope 2 on demand when a <permission /> directive is used",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope permission',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://pypi.python.org/pypi/collective.autopermission',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
