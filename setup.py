import codecs
import os

from setuptools import setup, find_packages

def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = read('README.md')

setup(
    name='renfe-cli',
    version='1.0.0',
    description='Get faster RENFE Spanish Trains timetables in your terminal',
    long_description=long_description,
    keywords='Get faster RENFE Spanish Trains timetables terminal',
    author='Gerard Castillo',
    author_email='gerardcl@gmail.com',
    url='https://github.com/gerardcl/renfe-cli',
    license='BSD',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=[
        'setuptools', 'lxml', 'numpy', 'pandas', 'python-dateutil', 'pytz', 'six'
    ],
    entry_points="""
        [console_scripts]
        renfe-cli = renfe.cli:main
        """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Users',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Terminal :: Tools',
    ],
    tests_require=['nose'],
    test_suite = 'nose.collector',
)
