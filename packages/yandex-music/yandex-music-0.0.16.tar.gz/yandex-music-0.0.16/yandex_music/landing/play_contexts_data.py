from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client, TrackShortOld

from yandex_music import YandexMusicObject


class PlayContextsData(YandexMusicObject):
    def __init__(self,
                 other_tracks: List['TrackShortOld'],
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.other_tracks = other_tracks

        self.client = client
        self._id_attrs = (self.other_tracks,)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['PlayContextsData']:
        if not data:
            return None

        data = super(PlayContextsData, cls).de_json(data, client)
        from yandex_music import TrackShortOld
        data['other_tracks'] = TrackShortOld.de_list(data.get('other_tracks'), client)

        return cls(client=client, **data)
