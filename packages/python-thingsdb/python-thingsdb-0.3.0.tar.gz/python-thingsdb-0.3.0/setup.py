from setuptools import setup, find_packages
from thingsdb import __version__

long_description = '''
The ThingsDB connector can be used to communicate with ThingsDB.

Besides a connector it also contains an ORM layer which can be used for
creating models and subscribing to things within a collection.
'''.strip()

setup(
    name='python-thingsdb',
    version=__version__,
    description='ThingsDB Connector',
    long_description=long_description,
    url='https://github.com/thingsdb/python-thingsdb',
    author='Jeroen van der Heijden',
    author_email='jeroen@transceptor.technology',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='database connector orm',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
