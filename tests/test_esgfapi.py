import pytest

from owslib.esgfapi import Variable
from owslib.esgfapi import Domain
from owslib.esgfapi import Dimension
from owslib.esgfapi import ParameterError


def test_variable():
    variable = Variable(var_name='tas', uri='http://data.demo/tas.nc', name='test')
    assert variable.var_name == 'tas'
    assert variable.uri == 'http://data.demo/tas.nc'
    assert variable.id == 'tas|test'
    assert variable.json == {'name': 'test', 'uri': 'http://data.demo/tas.nc', 'var_name': 'tas', 'id': 'tas|test'}
    assert variable.value == '{"name": "test", "uri": "http://data.demo/tas.nc", "var_name": "tas", "id": "tas|test"}'
    assert variable.__repr__() == "Variable(name='test', uri='http://data.demo/tas.nc', var_name='tas', id='tas|test')"


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
    assert dimension.name == 'time'
    assert dimension.start == 227
    assert dimension.end == 806
    assert dimension.json == {'end': 806, 'name': 'time', 'start': 227, 'step': 1}
    assert dimension.__repr__() == "Dimension(name='time', start='227', end='806', step='1')"
    dimension = Dimension('lat', 0, 90)
    assert dimension.name == 'lat'
    assert dimension.start == 0
    assert dimension.end == 90
    assert dimension.json == {'end': 90, 'name': 'lat', 'start': 0, 'step': 1}
    dimension = Dimension('lon', 180, 360)
    assert dimension.name == 'lon'
    assert dimension.start == 180
    assert dimension.end == 360
    assert dimension.json == {'end': 360, 'name': 'lon', 'start': 180, 'step': 1}


def test_domain():
    domain = Domain(name='test')
