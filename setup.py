#!/usr/bin/env python
from setuptools import setup

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

install_requires = ["Django>=1.11.20"]

tests_require = [
    "pysolr>=3.7.0",
    "whoosh>=2.5.4,<3.0",
    "python-dateutil",
    "geopy==2.0.0",
    "nose",
    "coverage",
    "requests",
]

setup(
    name="django-haystack",
    version="2.7.1",
    description="Pluggable search for Django.",
    author="Daniel Lindsley",
    author_email="daniel@toastdriven.com",
    long_description=open("README.rst", "r").read(),
    url="http://haystacksearch.org/",
    packages=[
        "haystack",
        "haystack.backends",
        "haystack.management",
        "haystack.management.commands",
        "haystack.templatetags",
        "haystack.utils",
    ],
    package_data={
        "haystack": ["templates/panels/*", "templates/search_configuration/*"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "elasticsearch": ["elasticsearch>=5,<6"],
    },
    test_suite="test_haystack.run_tests.run_all",
)
