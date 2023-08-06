"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qtfind',
    packages = ['qtfind'],
    version='1.0.3',
    description='graphical front-end for the linux find command',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amad3v/QtFind',
    author='Mohamed Jouini',
    author_email='amad3v@gmail.com', 
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    install_requires=['PyQt5'],
    include_package_data=True,
    # subfolder : relative path
    package_data={
        'qtfind': ['Icon.png'],
    },
    entry_points={
        'console_scripts': [
            'qtfind = qtfind.main:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/amad3v/QtFind/issues',
        'Releases': 'https://github.com/amad3v/QtFind/releases',
    },
)
