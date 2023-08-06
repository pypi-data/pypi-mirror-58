[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# pydatacleaner

pydatacleaner is a Python library to standardize data and to flexibly render them into the most correct datatypes. It was originally a significant part of the matrixb project to handle errors and inconsistencies when reading in data files.

The core DataCleaner class is a general base class and has functions primarily designed to look at text values and convert them to numbers, dates, booleans, etc, as appropriate. The *convert_{datatype}* properties indicate which types should be investigated, which triggers the *parse_{datatype}* as eligible.

Subclasses of datacleaner include SnakeCase and CamelCase, and as suggested, will convert strings to their snake or camel versions, and can translate between each other via the *tokenize()* and *join()* functions, which are abstract in the DataCleaner baseclass.

## Distribution

* [PyPI Distribution Page](https://pypi.org/project/pydatacleaner)
* [GitLab Project](https://gitlab.com/krcrouse/datacleaner)
* [Read the Docs Full API Documentation](https://datacleaner.readthedocs.io)

## Project Status

Currently, pydatacleaner is functional but shallowly vetted condition and should be considered **beta** software. Your mileage may vary. In particular, some of the non-default features, such as required typecasting, are slated to be refactored and haven't been examined thoroughly in a while.

Code comments of *NOTE* and *TODO* indicate known shortcomings that may be useful to you. The interface will likely change in future versions.

If you wish to rely on features of this package, I am likely more than willing to accommodate and to incorporate sensible design improvements or, in some cases, changes.

### Limitations and Future Directions

The clean function is relatively slow, especially when considering all data translations for large datasets of many millions of cells. I plan to build in eventual performance improvements by writing many of the core data processing in C instead of using the pure-python version, but I don't have a specific timeline for this.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pydatacleaner.

```bash
pip install pydatacleaner
```

## Usage

Many examples of usage are available in the main test files included in the t/ subdirectory.

```python
import datacleaner

#
# Auto-translating various null values to None
#

default_null_values = ['NA', 'na', 'N/A', 'n/a', 'NULL', 'null', 'None', 'none', 'nan', 'NaN', '#N/A']

cleaner = datacleaner.DataCleaner(
    null_values = default_null_values,
)

for ok in ('a','123', 123, 15.0, 2.66, -3.55, datetime.date(2017,3,5)):
    val = cleaner.clean(ok)
    assert ok is not None

for nullable in default_null_values:
    assert nullable is not None
    assert cleaner.clean(nullable) is None

additional = ['Toothpaste', -999, 0, 15.2, 'Woof', 'foo bar']
for ok in additional:
    val = cleaner.clean(ok)
    assert ok is not None

cleaner.add_null_values(additional)
for nullable in additional:
    assert nullable is not None
    assert cleaner.clean(nullable) is None

assert cleaner.clean(None) is None

#
# Examples of using translations
#

initial_translations = {
    -999:None,
    888:'Missing',
    '-999': 'N/A',
    '888': 5,
    None: 0,
    '777': 'INVALID string num not converting to num first',
    777: 'num convert is accurate',
    'xxx': 0,
}

cleaner = datacleaner.DataCleaner(
    translations = initial_translations
)
# this verifies the expected cases that types are converted before translations,
# so -999 and '-999' should relate to the same output (though we also dont trust order for hashes)
assert cleaner.clean('777') == 'num convert is accurate'
assert cleaner.clean(-999) == None
assert cleaner.clean('-999') == None
assert cleaner.clean(888) == 'Missing'
assert cleaner.clean('888') == 'Missing'
assert cleaner.clean(None) == 0
assert cleaner.clean('xxx') == 0

#
# test that adding translations after initialization works
assert cleaner.clean(999) == 999
cleaner.add_translations({999:None})
assert cleaner.clean(999) == None

basic_transliterations = [
    ('a','X'),
    [' ','_']
]
cleaner = datacleaner.DataCleaner(
    transliterations= basic_transliterations,
)

assert cleaner.clean('aaa') == 'XXX'
assert cleaner.clean('woof and bark') == 'woof_Xnd_bXrk'

#
# Time processing, requiring that the string ends up as a time object.
# Setting data_type means that the values are required to be None or time,
# and an error is thrown otherwise.  
#
cleaner = datacleaner.DataCleaner( data_type=datetime.time )

times = {
    '15:00': datetime.time(15,0),
    '2:00 pm': datetime.time(14,0),
    '2:00': datetime.time(2,0),
    '2:00PM': datetime.time(14,0),
    '0:00': datetime.time(0,0),
    '12:00': datetime.time(12,0),
    '12:00pm': datetime.time(12,0),
    '12:00 a.m.': datetime.time(0,0),
    '18:55:30.35': datetime.time(18,55,30, 350000),
    '18:55:30': datetime.time(18,55,30),
    '6:55:30 pm': datetime.time(18,55,30),
}

for raw, test in times.items():
    assert cleaner.clean(raw) == test


#
# Dates
#

dates = {
    '03-Aug-06': datetime.date(2006,8,3),
    '03-Aug-2006': datetime.date(2006,8,3),
    '3-Aug-06': datetime.date(2006,8,3),
    '3-Aug-2006': datetime.date(2006,8,3),
    '3-August-06': datetime.date(2006,8,3),
    '3-August-2006': datetime.date(2006,8,3),
    'Aug-03-06': datetime.date(2006,8,3),
    'Aug-03-2006': datetime.date(2006,8,3),
    'Monday, 3 of August 2006': datetime.date(2006,8,3),
    '03Aug06': datetime.date(2006,8,3),
    '03Aug2006': datetime.date(2006,8,3),
    '2006-08-03': datetime.date(2006,8,3),
    '20060803': datetime.date(2006,8,3),
    20060803: datetime.date(2006,8,3),
    '2006/08/03': datetime.date(2006,8,3),
    # month - day - year
    '08/03/06': datetime.date(2006,8,3),
    '08/03/2006': datetime.date(2006,8,3),
    '8/3/06': datetime.date(2006,8,3),
    '8/3/2006': datetime.date(2006,8,3),
    '12.18.97': datetime.date(1997,12,18),
    '12.25.2006': datetime.date(2006,12,25),
    '7-5-2000': datetime.date(2000,7,5),
}

cleaner.data_type = datetime.date
for raw, test in dates.items():
    assert cleaner.clean(raw) == test

datetimes = {
    '1994-11-05T08:15:30-05:00': datetime.datetime(
        1994, 11, 5, 8, 15, 30,
        tzinfo= datetime.timezone(datetime.timedelta(hours=-5))),
    '1994-11-05T13:15:30Z':datetime.datetime(
        1994, 11, 5, 13, 15, 30,
        tzinfo= datetime.timezone(datetime.timedelta(hours=0))),
    '1994-11-05T08:03:30-05:00': datetime.datetime(
        1994, 11, 5, 8, 3, 30,
        tzinfo= datetime.timezone(datetime.timedelta(hours=-5))),
    '1994-11-05T13:03:30Z':datetime.datetime(
        1994, 11, 5, 13, 3, 30,
        tzinfo= datetime.timezone(datetime.timedelta(hours=0))),
    '2006-08-03 18:55:30': datetime.datetime(2006,8,3,18,55,30),
    '03-Aug-2006 6:55:30 pm': datetime.datetime(2006,8,3,18,55,30),
}

cleaner.data_type = datetime.datetime
for raw, test in dates.items():
    assert cleaner.clean(raw) == test


```

## Contributing
Contributions are collaboration is welcome. For major changes, please contact me in advance to discuss.

Please make sure to update tests for any contribution, as appropriate.

## Author

[Kevin Crouse](mailto:krcrouse@gmail.com). Copyright, 2019.

## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
