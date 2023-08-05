import re

from setuptools import setup

# get version without importing
with open("extra_views/__init__.py", "rb") as f:
    VERSION = str(re.search('__version__ = "(.+?)"', f.read().decode("utf-8")).group(1))

setup(
    name="django-extra-views",
    version=VERSION,
    url="https://github.com/AndrewIngram/django-extra-views",
    install_requires=["Django >=1.11", "six>=1.5.2"],
    description="Extra class-based views for Django",
    long_description=open("README.rst", "r").read(),
    license="MIT",
    author="Andrew Ingram",
    author_email="andy@andrewingram.net",
    packages=["extra_views", "extra_views.contrib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
