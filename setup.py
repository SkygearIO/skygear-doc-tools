from setuptools import setup, find_packages
import glob
import os


setup(
    name='skygear_doc_tools',
    version='0.0.1',
    zip_safe=False,
    include_package_data=True,
    install_requires=['click'],
    packages=find_packages(),
    scripts=['bin/create-docker-image',
             'bin/generate-js-doc',
             'bin/generate-ios-doc',
             'bin/generate-android-doc',
             'bin/publish-doc'],
)
