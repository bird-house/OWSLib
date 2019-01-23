import json
from uuid import uuid1

from owslib.wps import ComplexDataInput


class ParameterError(Exception):
    pass


class Parameter(ComplexDataInput):
    def __init__(self, name=None):
        super(Parameter, self).__init__(
            value=None,
            mimeType="application/json",
            encoding=None,
            schema=None)
        self._data = {}
        self._data['name'] = name or uuid1().hex

    @property
    def name(self):
        return self._data['name']

    @property
    def json(self):
        return self._data

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    @property
    def value(self):
        return json.dumps(self.json)

    @value.setter
    def value(self, value):
        if value:
            self.from_json(json.loads(value))


class Variable(Parameter):
    def __init__(self, uri, var_name=None, id=None, name=None):
        super(Variable, self).__init__(name)
        self._data['uri'] = uri

        if id:
            self._data['id'] = id
            if '|' in id:
                var_name, name = id.split('|')
            else:
                raise ParameterError('Variable id must contain a variable name and id.')
        if var_name:
            self._data['var_name'] = var_name
            if not id:
                self._data['id'] = '{}|{}'.format(var_name, self.name)

        if 'id' not in self._data:
            raise ParameterError('Variable must have an id.')
        if 'var_name' not in self._data:
            raise ParameterError('Variable must have a var_name.')

    @property
    def id(self):
        return self._data['id']

    @property
    def var_name(self):
        return self._data['var_name']

    @property
    def uri(self):
        return self._data['uri']

    def __repr__(self):
        return "Variable(name='{}', uri='{}', var_name='{}')".format(
            self.name, self.uri, self.var_name)


class Dimension(Parameter):
    def __init__(self, name=None, start=None, end=None):
        super(Dimension, self).__init__(name)
        self._data['start'] = start
        self._data['end'] = end
        self._data['step'] = 1

    @property
    def start(self):
        return self._data['start']

    @property
    def end(self):
        return self._data['end']

    @property
    def step(self):
        return self._data['step']

    def __repr__(self):
        return "Dimension(name={}, start={}, end={})".format(
            self.name,
            self.start,
            self.end)


class Domain(Parameter):
    def __init__(self, dimensions=None, mask=None, name=None):
        super(Domain, self).__init__(name)
        self._dimensions = dimensions or []
        self._mask = mask

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def mask(self):
        return self._mask

    def __repr__(self):
        return "Domain(dimensions='{}', mask='{}', name='{}')".format(
            self.dimensions, self.mask, self.name)
