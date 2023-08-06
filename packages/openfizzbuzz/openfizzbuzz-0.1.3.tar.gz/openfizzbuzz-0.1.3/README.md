# openfizzbuzz

[![Build Status](https://travis-ci.com/Haytek/openfizzbuzz.svg?branch=master)](https://travis-ci.com/Haytek/openfizzbuzz)

Open minded Python FizzBuzz

````shell script
pip install -i https://test.pypi.org/simple/ openfizzbuzz
pip install -r requirements.txt
python3.7 -m openfizzbuzz
````

> FizzBuzz original question  
>
> Write a program that prints the numbers from 1 to 100. For multiples
> of three print "Fizz" instead of the number, and for the multiples of
> five print "Buzz". For numbers which are multiples of both tree and
> five print "FizzBuzz".



## Ideas

- Classes and functions
- Module structuration
- lambda
- logging
- some tests
- new dataclasses
- list comprehension
- coverage
- pypi setup
- factory (& others patterns ?)


## More ideas

- MRO manipulation
- Dynamic method binding
- Exec / Compile text
- Internal python integer manipulation (ctypes)
- pyc / pyo


## Notes

### Ideolog log format:

Message Pattern : `^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3})\s*::\s*(\S*)\s*::\s*(\S*)\s*::\s*(.+)$`

Time Format : `yyyy-MM-dd HH:mm:ss,SSS`

Time Capture Group : `1`

Severity Capture Group : `2`

Category Capture Group : `3`

### test.pypi.org

`````shell script
pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
`````

### pypi
*untested*
````shell script
pip install --upgrade setuptools wheel twine
python setup.py register
python setup.py sdist upload
````
