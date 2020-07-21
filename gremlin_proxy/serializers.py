

class GremlinResponseSerializer:

    @staticmethod
    def serialize_vertex(vtx):
        cleaned_data = {"properties": {}}
        for k, v in vtx.items():
            if str(k) == "T.id":
                cleaned_data['id'] = v.get('@value').strip("#") if type(v) is dict else v
            elif str(k) == "T.label":
                cleaned_data['label'] = v
            else:
                cleaned_data['properties'][k] = v[0]  # TODO - fix this.
        return cleaned_data

    @staticmethod
    def serialize_edge(edg):
        cleaned_data = {"properties": {}}
        for k, v in edg.items():
            if str(k) == "T.id":
                cleaned_data['id'] = v.get('@value', {}).get("relationId") if type(v) is dict else v
            elif str(k) == "T.label":
                cleaned_data['label'] = v
            else:
                cleaned_data['properties'][k] = v  # TODO - fix this.
        return cleaned_data

    def serializer_data(self, data):
        _serialized_data = []
        if isinstance(data, list):
            for datum in data:
                _ = self.serializer_data(datum)
                _serialized_data.extend(_)
        elif isinstance(data, dict):
            try:
                # TODO - use better logics to check if data is vertex or edge,
                # currently simple try except works.
                _serialized_data.append(self.serialize_vertex(data))
            except Exception as e:
                _serialized_data.append(self.serialize_edge(data))

        return _serialized_data
