import sys
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()

install_requires = []
if sys.version_info < (2, 7, 9):
    raise Exception('ButterCMS uses the requests library to securely talk to https://buttercms.com '
        'which requires Python 2.7.9 or later.\n'
        'Please take a few seconds to upgrade to Python 2.7.9 and try again.\n'
        'https://www.python.org/downloads/')
    # TODO: Add support for < Python 2.7.9
    # install_requires.append('requests[security]')
else:
    install_requires.append('requests')

package_root = os.path.abspath(os.path.dirname(__file__))
version = {}

with open(os.path.join(package_root, "buttercms-python-testing-fork/version.py")) as fp:
    exec(fp.read(), version)

version = version["__version__"]


setup(
    name = 'buttercms-python-testing-fork',
    packages=find_packages(),
    version=version,
    description = 'API First Blogging and CMS platform built for developers',
    long_description=readme,
    long_description_content_type="text/markdown",
    author = 'Martin Albert',
    author_email = 'martin.albert.187@gmail.com',
    url = 'https://github.com/martinalbert/buttercms-python',
    download_url = 'https://github.com/martinalbert/buttercms-python/tarball/0.1',
    install_requires=install_requires,
    keywords = ['buttercms', 'sdk', 'cms', 'api', 'blogging'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ]
)
