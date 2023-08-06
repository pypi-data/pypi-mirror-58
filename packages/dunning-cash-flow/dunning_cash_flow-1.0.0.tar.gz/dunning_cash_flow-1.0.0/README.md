# dunning-cash-flow

Dunning cash flow is wrapper for Twikey REST APIs : Automatic payments for recurring customers.

Dunning cash flow is part of another project aiming at providing Dunning services.

*Dunning services is subscription Analytics and Insights: One click and you get hundreds of valuable metrics and business insights for Twikey.*

* ALT-F1 SPRL <http://www.alt-f1.be>
* Twikey <https://www.twikey.com>

## usage

* install the package from the **pypi.org** : 
    * install : `pip install dunning-cash-flow`
    * upgrade : `pip install dunning-cash-flow --upgrade`


* install the package from the **test.pypi.org** : 
    * install : `pip install -i https://test.pypi.org/simple/ dunning-cash-flow`
    * upgrade : `pip install -i https://test.pypi.org/simple/ dunning-cash-flow --upgrade`


## dependencies

* countries_utils : <https://pypi.org/project/countries_utils>
* requests : <https://pypi.org/project/requests>


## Build the package 

* build the setup.py
    * `python setup.py sdist bdist_wheel`

* upload the library on TEST **pypi.org** 
    * `python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*` 
    * Source : <https://test.pypi.org/project/dunning-cash-flow>

* upload the library on PROD **pypi.org** 
    * `python -m twine upload dist/*` 
    * Source : <https://pypi.org/project/dunning-cash-flow>

## test the library

* set the environment variable with yout Twikey Token `set TwikeyApiToken=<40 chars>`
* `cd dunning_cash_flow`
* `pipenv install`
* `pipenv run python dunning_cash_flow_unittest.py`

* locate the package 
    * `python -c "import dunning_cash_flow as _; print(_.__path__)"`
* list functions inside the module
    *  the package `python -c "import dunning_cash_flow as _; print(dir(_))"`


## Documentation

* Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>
* Managing Application Dependencies <https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies>
* Packaging and distributing projects <https://packaging.python.org/guides/distributing-packages-using-setuptools/#distributing-packages>

## License

Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.

Licensed under the EUPL License, Version 1.2.

See LICENSE in the project root for license information.
