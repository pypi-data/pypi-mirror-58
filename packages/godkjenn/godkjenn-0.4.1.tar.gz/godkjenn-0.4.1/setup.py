from pathlib import Path

from setuptools import find_packages, setup

setup(
    name='godkjenn',
    version='0.4.1',
    packages=find_packages('src'),

    author='Sixty North AS',
    author_email='austin@sixty-north.com',
    description='Approval testing for Python3',
    license='MIT',
    keywords='',
    url='http://bitbucket.org/sixty-north/godkjenn',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Pytest',
    ],
    platforms='any',
    include_package_data=True,
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'exit-codes',
        'stevedore',
        'toml',
    ],
    extras_require={
        'dev': ['bumpversion', 'twine'],
        'test': ['hypothesis', 'pytest'],
        'pytest-plugin': ['pytest'],
    },
    entry_points={
        'pytest11': [
            'godkjenn = godkjenn.integration.pytest_plugin',
        ],
        "godkjenn.vault": [
            'fs-vault = godkjenn.fs_vault:plugin',
        ],
        'console_scripts': [
            'godkjenn = godkjenn.cli:main',
        ]
    },
    long_description=Path('README.rst').read_text(encoding='utf-8'),
)
