from setuptools import setup, find_packages

requirements = [
    "pytest",
    "requests",
    "gunicorn",
    "django"
]

setup(
    name="tinkerhub-portal",
    version="0.0.1",
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements)
