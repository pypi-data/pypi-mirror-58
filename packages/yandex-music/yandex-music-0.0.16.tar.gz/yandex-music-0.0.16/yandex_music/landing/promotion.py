from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client

from yandex_music import YandexMusicObject


class Promotion(YandexMusicObject):
    def __init__(self,
                 promo_id: str,
                 title: str,
                 subtitle: str,
                 heading: str,
                 url: str,
                 url_scheme: str,
                 text_color: str,
                 gradient: str,
                 image: str,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.promo_id = promo_id
        self.title = title
        self.subtitle = subtitle
        self.heading = heading
        self.url = url
        self.url_scheme = url_scheme
        self.text_color = text_color
        self.gradient = gradient
        self.image = image

        self.client = client
        self._id_attrs = (self.promo_id, self.title, self.subtitle, self.heading,
                          self.url, self.url_scheme, self.text_color, self.gradient, self.image)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Promotion']:
        if not data:
            return None

        data = super(Promotion, cls).de_json(data, client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['Promotion']:
        if not data:
            return []

        promotions = list()
        for promotion in data:
            promotions.append(cls.de_json(promotion, client))

        return promotions
