from owslib.wps import ComplexDataInput


class Variable(ComplexDataInput):
    def __init__(self, id=None, uri=None):
        super(Variable, self).__init__(
            value="{{'id': {}, 'uri': {}}}".format(id, uri),
            mimeType="application/json", encoding=None, schema=None)
        pass
