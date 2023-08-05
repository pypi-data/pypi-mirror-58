# countries-utils

Utils used by the dunning service wrapper. See <https://bitbucket.org/altf1be/dunningcashflow.git>

* Get the list of countries stored in the field "place" in transactions stored in twikey.
* The places are written either in FR, EN or NL.
* The method returns a List of places in English and a Set of those places if the places are using the above-mentioned languages

## usage

* install the package from the **test.pypi** : `pip install -i https://test.pypi.org/simple/ countries-utils`
## dependencies

* pycountry <https://pypi.org/project/pycountry>
* country_list <https://pypi.org/project/country_list>

## Build the package 

* `python setup.py sdist bdist_wheel`

* upload the library on **test.pypi** `python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*` 
    * Source : <https://test.pypi.org/project/countries-utils>


## test the library

* `pipenv run python countries_utils_unittest.py`

## Documentation

* Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>
* Managing Application Dependencies <https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies>
* Packaging and distributing projects <https://packaging.python.org/guides/distributing-packages-using-setuptools/#distributing-packages>

## License

Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.

Licensed under the EUPL License, Version 1.2. 
See LICENSE in the project root for license information.
