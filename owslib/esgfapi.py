import json

from owslib.wps import ComplexDataInput


class ParameterError(Exception):
    pass


class Variable(ComplexDataInput):
    def __init__(self, id=None, uri=None):
        self._id = id
        self._uri = uri
        super(Variable, self).__init__(
            value=json.dumps(self.json),
            mimeType="application/json", encoding=None, schema=None)

    @property
    def name(self):
        return self.id

    @property
    def id(self):
        return self._id

    @property
    def uri(self):
        return self._uri

    @property
    def json(self):
        return {'id': self.id, 'uri': self.uri}

    @classmethod
    def from_json(cls, data):
        uri = None
        id = None

        if 'uri' in data:
            uri = data['uri']
        else:
            raise ParameterError('Variable must provide a uri.')

        if 'id' in data:
            id = data['id']
        else:
            raise ParameterError('Variable must provide a id.')

        return cls(uri=uri, id=id)

    def __repr__(self):
        return ('Variable(name=%r, uri=%r)' % (self.name, self.uri))
