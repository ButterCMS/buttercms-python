import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()

install_requires = ['requests']
package_root = os.path.abspath(os.path.dirname(__file__))
version = {}

with open(os.path.join(package_root, "butter_cms/version.py")) as fp:
    exec(fp.read(), version)

version = version["__version__"]

setup(
    name = 'buttercms-python',
    packages = find_packages(),
    version = version,
    description = 'API First Blogging and CMS platform built for developers',
    long_description=readme,
    long_description_content_type="text/markdown",
    author = 'ButterCMS',
    author_email = 'support@buttercms.com',
    url = 'https://github.com/buttercms/buttercms-python',
    download_url = 'https://github.com/buttercms/buttercms-python/tarball/0.1',
    py_modules=['butter_cms'],
    install_requires=install_requires,
    keywords = ['buttercms', 'sdk', 'cms', 'api'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ]
)
