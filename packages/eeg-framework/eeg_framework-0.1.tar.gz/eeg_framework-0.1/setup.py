import os
from setuptools import setup
#from distutils.core import setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version_str = open(os.path.join('eeg_framework', '_version.txt'), 'r').read().strip()

setup(
    name='eeg_framework',
    version=version_str,
    packages=['eeg_framework'],

    author='Yeison Cardona',
    author_email='yeisoneng@gmail.com',
    maintainer='Yeison Cardona',
    maintainer_email='yeisoneng@gmail.com',

    # url='http://yeisoncardona.com/',
    download_url='https://bitbucket.org/gcpds/eeg_framework/downloads/',

    install_requires=[
        #'gym',
        # 'pyserial',
        # 'scipy>=1.3.1',
        # 'numpy',
        # 'psutil',
        # 'mne',
        # 'requests',
        # 'tornado',
        # 'systemd_service',
    ],

    include_package_data=True,
    license='BSD License',
    description="GCPDS: eeg_framework",
    #    long_description = README,

    classifiers=[

    ],

)
