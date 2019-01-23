import pytest

from owslib.esgfapi import Variable
from owslib.esgfapi import Domain
from owslib.esgfapi import Dimension
from owslib.esgfapi import ParameterError


def test_variable():
    variable = Variable(var_name='tas', uri='http://data.demo/tas.nc', name='test')
    assert variable.var_name == 'tas'
    assert variable.uri == 'http://data.demo/tas.nc'
    assert variable.json['id'] == 'tas|test'
    assert variable.json['uri'] == 'http://data.demo/tas.nc'
    assert variable.value == '{"uri": "http://data.demo/tas.nc", "id": "tas|test"}'
    assert variable.__repr__() == "Variable(name='test', uri='http://data.demo/tas.nc', var_name='tas')"


def test_variable_from_json():
    variable = Variable.from_json({"id": "tas|test2", "uri": "http://data.demo/tas.nc"})
    assert variable.var_name == 'tas'
    assert variable.uri == 'http://data.demo/tas.nc'
    # check invalid json
    with pytest.raises(ParameterError):
        # id missing
        Variable.from_json({"uri": "http://data.demo/tas.nc"})


def test_dimension():
    dimension = Dimension('time', 227, 806)
    dimension = Dimension('lat', 0, 90)
    dimension = Dimension('lon', 180, 360)


def test_domain():
    domain = Domain(name='test')
