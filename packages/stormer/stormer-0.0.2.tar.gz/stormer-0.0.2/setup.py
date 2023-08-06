import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

DESCRIPTION = (
    'this is a requester'
)
CLASSIFIERS = [
    'Programming Language :: Python',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
]
KEYWORDS = (
    'stormer', 'requester', 'redis'
)

setup(
    name='stormer',
    version='0.0.2',
    maintainer='Murray',
    maintainer_email='murray.ma@qq.com',
    url='https://github.com/murray-ma/stormer/',
    download_url='https://github.com/murray-ma/stormer/',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT',
    platforms='Platform Independent',
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[
        'requests>=2.22.0',
        'redis>=3.3.11',
    ],
)
