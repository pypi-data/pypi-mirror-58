from enum import Enum

ujson = False
try:
    import ujson as json
    ujson = True
except ImportError:
    import json


class Operation(Enum):
    INSERT = 'insert'
    DELETE = 'delete'


class Difference:
    def __init__(self):
        self.operations = []

    def to_json(self):
        return json.dumps(self.operations, ensure_ascii=not ujson)

    def add_delete(self, from_, to):
        operation = {
            'op': Operation.DELETE.value,
            'from': from_,
            'to': to
        }

        self.operations.append(operation)
        return self

    def add_insert(self, at, tracks: dict or list):
        if not isinstance(tracks, list):
            tracks = [tracks]

        operation = {
            'op': Operation.INSERT.value,
            'at': at,
            'tracks': []
        }

        for track in tracks:
            track = type('TrackId', (), track)  # TODO replace to normal TrackId object

            operation['tracks'].append(
                {
                    'id': track.id,
                    'albumId': track.album_id
                }
            )

        self.operations.append(operation)
        return self
