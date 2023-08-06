#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup_requirements = []

test_requirements = []

# print(find_packages(include=['tage'], exclude=["examples*", "tests*"]))

KEYWORDS = [
    'nodedge',
    'editor',
    'graphical-programming',
    'simulation',
    'physical-modeling',
    'control-systems',
    'dynamic-systems',
    'python3',
    'qt5',
    'pyqt5',
    'platform-indenpendent',
    'windows',
    'linux',
    'macos'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.6',
]

PLATFORMS = [
    "Windows",
    "Linux",
    "Mac OS-X",
    "Unix"
]

setup(
    name='nodedge',
    keywords=KEYWORDS,
    description="Graphical editor for physical modeling and simulation.",
    url='https://www.nodedge.io',
    version='0.2.0',
    license="GNU General Public License v3",
    author="Anthony De Bortoli",
    author_email='anthony.debortoli@protonmail.com',
    python_requires='>=3.6',
    classifiers=CLASSIFIERS,
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    platforms=PLATFORMS,
    packages=find_packages(include="nodedge*", exclude=["tes"]),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
