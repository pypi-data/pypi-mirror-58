# -*- coding: utf-8 -*-

# Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.
# Licensed under the EUPL License, Version 1.2.
# See LICENSE in the project root for license information.

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='countries-utils',
    version='0.0.0',
    author='Abdelkrim Boujraf',
    author_email='abo+pypi@alt-f1.be',
    description='Utils to deal with pycountry and country_list packages.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.org/altf1be/dunningcashflow.git',
    packages=setuptools.find_packages('src'),
    package_data={
        # If any package contains *.txt files, include them:
        # '': ['*.txt'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'src': ['data/*.csv'],
    },
    keywords='library pycountry country_list dunning_service',

    # Find the list of classifiers : https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.5',

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},  # Optional

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://bitbucket.org/altf1be/countries-utils/issues?status=new&status=open',
        'Company behind the library': 'http://www.alt-f1.be',
        'Source': 'https://bitbucket.org/altf1be/countries-utils',
    },

)
