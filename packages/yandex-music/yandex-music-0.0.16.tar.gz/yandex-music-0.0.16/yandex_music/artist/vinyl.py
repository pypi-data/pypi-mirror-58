from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client

from yandex_music import YandexMusicObject


class Vinyl(YandexMusicObject):
    def __init__(self,
                 url: str,
                 picture: str,
                 title: str,
                 year: int,
                 price: int,
                 media: str,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.url = url
        self.picture = picture
        self.title = title
        self.year = year
        self.price = price
        self.media = media

        self.client = client
        self._id_attrs = (self.title, self.price, self.year, self.url, self.price, self.media)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Vinyl']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client` представляющий клиент Yandex
                Music.

        Returns:
            :obj:`yandex_music.Vinyl`: Объект класса :class:`yandex_music.Vinyl`.
        """

        if not data:
            return None

        data = super(Vinyl, cls).de_json(data, client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['Vinyl']:
        """Десериализация списка объектов.

        Args:
            data (:obj:`list`): Список словарей с полями и значениями десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client` представляющий клиент Yandex
                Music.

        Returns:
            :obj:`list` из :obj:`yandex_music.Vinyl`: Список объектов класса :class:`yandex_music.Vinyl`.
        """
        if not data:
            return []

        vinyls = list()
        for vinyl in data:
            vinyls.append(cls.de_json(vinyl, client))

        return vinyls
