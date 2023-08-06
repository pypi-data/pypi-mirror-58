from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client, Best

from yandex_music import YandexMusicObject


class Suggestions(YandexMusicObject):
    def __init__(self,
                 best: Optional['Best'],
                 suggestions: List[str],
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.best = best
        self.suggestions = suggestions

        self.client = client
        self._id_attrs = (self.best, self.suggestions)

    def __getitem__(self, item):
        return self.suggestions[item]

    def __iter__(self):
        return iter(self.suggestions)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Suggestions']:
        if not data:
            return None

        data = super(Suggestions, cls).de_json(data, client)
        from yandex_music import Best
        data['best'] = Best.de_json(data.get('best'), client)

        return cls(client=client, **data)

