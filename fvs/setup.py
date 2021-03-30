import os
import glob
import re
import sys

from setuptools.command.test import test as TestCommand
from setuptools.command.install import install
from setuptools import setup, find_packages


metadata = dict(
    re.findall("__([a-z]+)__ = '([^']+)'", open('fvs/__init__.py').read()))


requirements = [
    x.strip() for x
    in open('requirements.txt').readlines() if not x.startswith('#')]


description = "Python FVS"


py_modules = ['fvs', 'fvs/common', 'fvs/common/utils', 'fvs/db', 'fvs/app']


class Install(install):
    def run(self):
        install.run(self)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='fvs',
    version=metadata['version'],
    author='caibo',
    author_email='caibo@senguo.cc',
    url='https://littlesky-01.coding.net/p/fvs/d/fvs/git',
    license='MIT',
    packages=find_packages(exclude=["test", "vevn"]),
    description=description,
    py_modules=py_modules,
    install_requires=requirements,
    extras_require={
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest,
              'install': Install},
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)