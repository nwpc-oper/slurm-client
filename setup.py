from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slurm-client',

    version='1.0.0',

    description='Slurm Client',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/perillaroc/nwpc-nost',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='GPL-3.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='nwpc slurm client',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    include_package_data=True,

    package_data={
        'slurm_client': ['conf/*.config']
    },

    install_requires=[
        'pyyaml',
        'click',
        'nwpc-hpc-model'
    ],

    extras_require={
        'pyslurm': [
            'cython',
            'pyslurm'
        ],
    },

    entry_points={
        'console_scripts': [
            'slclient=slurm_client.slclient:cli'
        ]
    }
)
