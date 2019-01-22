import pytest

from owslib.esgfapi import Variable
from owslib.esgfapi import ParameterError


def test_variable():
    variable = Variable(id='tas', uri='http://data.demo/tas.nc')
    assert variable.id == 'tas'
    assert variable.uri == 'http://data.demo/tas.nc'
    assert variable.json['id'] == 'tas'
    assert variable.json['uri'] == 'http://data.demo/tas.nc'
    assert variable.value == '{"id": "tas", "uri": "http://data.demo/tas.nc"}'
    assert variable.__repr__() == "Variable(name='tas', uri='http://data.demo/tas.nc')"


def test_variable_from_json():
    variable = Variable.from_json({"id": "tas", "uri": "http://data.demo/tas.nc"})
    assert variable.id == 'tas'
    assert variable.uri == 'http://data.demo/tas.nc'
    # check invalid json
    with pytest.raises(ParameterError):
        # id missing
        Variable.from_json({"uri": "http://data.demo/tas.nc"})
