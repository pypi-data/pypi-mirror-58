from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client, Track

from yandex_music import YandexMusicObject


class TrackWithAds(YandexMusicObject):
    def __init__(self,
                 type_: str,
                 track: Optional['Track'],
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.type = type_
        self.track = track

        self.client = client
        self._id_attrs = (self.type, self.track)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['TrackWithAds']:
        if not data:
            return None

        data = super(TrackWithAds, cls).de_json(data, client)
        from yandex_music import Track
        data['track'] = Track.de_json(data.get('track'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['TrackWithAds']:
        if not data:
            return []

        tracks_with_ads = list()
        for track_with_ads in data:
            tracks_with_ads.append(cls.de_json(track_with_ads, client))

        return tracks_with_ads
