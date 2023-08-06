#!/usr/bin/env python

from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("HISTORY.md") as f:
    history = f.read().replace(".. :changelog:", "")

setup(
    name="maykin-django-better-admin-arrayfield",
    version="1.0.5",
    description="Better ArrayField widget for admin",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="Jakub Semik, Maykin Media",
    author_email="info@maykinmedia.nl",
    url="https://github.com/maykinmedia/django-better-admin-arrayfield",
    packages=["django_better_admin_arrayfield"],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords="django-better-admin-arrayfield",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
