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
        self._name = name or uuid1().hex

    @classmethod
    def from_json(cls, data):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

    @property
    def json(self):
        raise NotImplementedError

    @property
    def value(self):
        return json.dumps(self.json)

    @value.setter
    def value(self, value):
        if value:
            self.from_json(json.loads(value))


class Variable(Parameter):
    def __init__(self, uri, var_name, name=None):
        super(Variable, self).__init__(name)
        self._uri = uri
        self._var_name = var_name

    @property
    def var_name(self):
        return self._var_name

    @property
    def uri(self):
        return self._uri

    @property
    def json(self):
        params = {
            'uri': self.uri,
            'id': self.var_name,
        }
        if self.var_name:
            params['id'] = '{}|{}'.format(params['id'], self.name)
        return params

    @classmethod
    def from_json(cls, data):
        uri = None
        id = None

        if 'uri' in data:
            uri = data['uri']
        else:
            raise ParameterError('Variable must provide a uri.')

        name = None
        var_name = None

        if 'id' in data:
            if '|' in data['id']:
                var_name, name = data['id'].split('|')
            else:
                raise ParameterError('Variable id must contain a variable name and id.')
        else:
            raise ParameterError('Variable must provide an id.')

        return cls(uri=uri, var_name=var_name, name=name)

    def __repr__(self):
        return "Variable(name='{}', uri='{}', var_name='{}')".format(
            self.name, self.uri, self.var_name)


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
