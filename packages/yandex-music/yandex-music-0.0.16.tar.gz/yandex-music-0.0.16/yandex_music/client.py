import logging
import functools
from datetime import datetime
from typing import Callable, Union, List, Optional

from yandex_music import YandexMusicObject, Status, Settings, PermissionAlerts, Experiments, Artist, Album, Playlist, \
    TracksList, Track, AlbumsLikes, ArtistsLikes, PlaylistsLikes, Feed, PromoCodeStatus, DownloadInfo, Search, \
    Suggestions, Landing, Genre, Dashboard, StationResult, StationTracksResult, BriefInfo, Supplement, ArtistTracks, \
    ArtistAlbums
from yandex_music.utils.request import Request
from yandex_music.utils.difference import Difference
from yandex_music.exceptions import InvalidToken, Captcha

CLIENT_ID = '23cabbbdc6cd418abb4b39c32c41195d'
CLIENT_SECRET = '53bc75238f0c4d08a118e51fe9203300'

de_list = {
    'artist': Artist.de_list,
    'album': Album.de_list,
    'track': Track.de_list,
    'playlist': Playlist.de_list,
}

de_list_likes = {
    'artist': ArtistsLikes.de_list,
    'album': AlbumsLikes.de_list,
    'playlist': PlaylistsLikes.de_list,
}

logging.getLogger(__name__).addHandler(logging.NullHandler())


def log(method):
    logger = logging.getLogger(method.__module__)

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        logger.debug(f'Entering: {method.__name__}')

        result = method(*args, **kwargs)
        logger.debug(result)

        logger.debug(f'Exiting: {method.__name__}')

        return result

    return wrapper


class Client(YandexMusicObject):
    """Класс представляющий клиент Yandex Music.

    При `fetch_account_status = False` многие сокращения перестанут работать в связи с тем, что неоткуда будет взять
    uid аккаунта для отправки запроса. Так же в большинстве методов придётся передавать uid явно.

    Attributes:
        logger (:obj:`logging.Logger`): Объект логера.
        token (:obj:`str`): Уникальный ключ для аутентификации.
        base_url (:obj:`str`): Ссылка на API Yandex Music.
        oauth_url (:obj:`str`): Ссылка на OAuth Yandex Music.
        me (:obj:`yandex_music.Status`): Объект класса :class:`yandex_music.Status` предоставляющего основную
            информацию об аккаунте.

    Args:
        token (:obj:`str`, optional): Уникальный ключ для аутентификации.
        fetch_account_status (:obj:`bool`, optional): Получить ли информацию об аккаунте при инициализации объекта.
        base_url (:obj:`str`, optional): Ссылка на API Yandex Music.
        oauth_url (:obj:`str`, optional): Ссылка на OAuth Yandex Music.
        request (:obj:`yandex_music.utils.request.Request`, optional): Пре-инициализация
            :class:`yandex_music.utils.request.Request`.
    """

    def __init__(self, token: str = None, fetch_account_status: bool = True, base_url: str = None,
                 oauth_url: str = None, request: Request = None) -> None:
        self.logger = logging.getLogger(__name__)
        self.token = token

        if base_url is None:
            base_url = 'https://api.music.yandex.net'
        if oauth_url is None:
            oauth_url = 'https://oauth.yandex.ru'

        self.base_url = base_url
        self.oauth_url = oauth_url

        if request:
            self._request = request
            self._request.set_and_return_client(self)
        else:
            self._request = Request(self)

        self.me = None
        if fetch_account_status:
            self.me = self.account_status()

    @classmethod
    def from_credentials(cls, username: str, password: str, x_captcha_answer: str = None, x_captcha_key: str = None,
                         captcha_callback: Callable[[Captcha], str] = None, *args, **kwargs) -> 'Client':
        """Инициализция клиента по логину и паролю.

        Note:
            Данный метод получает токен каждый раз при вызове. Рекомендуется сгенерировать его самостоятельно, сохранить
            и использовать при следующих инициализациях клиента. Не храните логины и пароли!

        Args:
            username (:obj:`str`): Логин клиента (идентификатор).
            password (:obj:`str`): Пароль клиента (аутентификатор).
            x_captcha_answer (:obj:`str`, optional): Ответ на капчу (цифры с картинки).
            x_captcha_key (:obj:`str`, optional): Уникальный ключ капчи.
            captcha_callback (:obj:`function`, optional): Функция обратного вызова для обработки капчи, должна
                принимать объект класса :class:`yandex_music.exceptions.Captcha` и возвращать проверочный код.
            **kwargs (:obj:`dict`, optional): Аргументы для конструктора клиента.

        Returns:
            :obj:`yandex_music.Client`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        token = None
        while not token:
            try:
                token = cls(*args, **kwargs).generate_token_by_username_and_password(username, password,
                                                                                     x_captcha_answer=x_captcha_answer,
                                                                                     x_captcha_key=x_captcha_key)
            except Captcha as e:
                if not captcha_callback:
                    raise e

                x_captcha_answer = captcha_callback(e.captcha)
                x_captcha_key = e.captcha.x_captcha_key

        return cls(token, *args, **kwargs)

    @classmethod
    def from_token(cls, token: str, *args, **kwargs) -> 'Client':
        """Инициализция клиента по токену.

        Ничем не отличается от Client(token). Так исторически сложилось.

        Args:
            token (:obj:`str`, optional): Уникальный ключ для аутентификации.
            **kwargs (:obj:`dict`, optional): Аргументы для конструктора клиента.

        Returns:
            :obj:`yandex_music.Client`.
        """

        return cls(token, *args, **kwargs)

    @log
    def generate_token_by_username_and_password(self, username: str, password: str, grant_type: str = 'password',
                                                x_captcha_answer: str = None, x_captcha_key: str = None,
                                                timeout: Union[int, float] = None, *args, **kwargs) -> str:
        """Метод получения OAuth токена по логину и паролю.

        Args:
            username (:obj:`str`): Логин клиента (идентификатор).
            password (:obj:`str`): Пароль клиента (аутентификатор).
            grant_type (:obj:`str`, optional): Тип разрешения OAuth.
            x_captcha_answer (:obj:`str`, optional): Ответ на капчу (цифры с картинки).
            x_captcha_key (:obj:`str`, optional): Уникальный ключ капчи.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`str`: OAuth токен.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.oauth_url}/token'

        data = {
            'grant_type': grant_type,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'username': username,
            'password': password
        }

        if x_captcha_answer and x_captcha_key:
            data.update({'x_captcha_answer': x_captcha_answer, 'x_captcha_key': x_captcha_key})

        result = self._request.post(url, data, timeout=timeout, *args, **kwargs)

        return result.get('access_token')

    @staticmethod
    def _validate_token(token: str) -> str:
        """Примитивная валидация токена.

        Args:
            token (:obj:`str`): токен для проверки

        Returns:
            :obj:`str`: Токен.

        Raises:
            :class:`yandex_music.exceptions.InvalidToken`: Если токен недействителен.
        """

        if any(x.isspace() for x in token):
            raise InvalidToken()

        if len(token) != 39:
            raise InvalidToken()

        return token

    @property
    def request(self) -> Request:
        """:obj:`yandex_music.utils.request.Request`: Объект вспомогательного класса для отправки запросов."""
        return self._request

    @log
    def account_status(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Status]:
        """Получение статуса аккаунта. Нет обязательных параметров.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Status`: Объекта класса :class:`yandex_music.Status` предоставляющий информацию об
            аккаунте если валиден, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/account/status'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Status.de_json(result, self)

    @log
    def settings(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Settings]:
        """Получение предложений по покупке. Нет обязательных параметров.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Settings`: Объекта класса :class:`yandex_music.Settings` предоставляющий информацию о
            предлагаемых продуктах, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/settings'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Settings.de_json(result, self)

    @log
    def permission_alerts(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[PermissionAlerts]:
        """Получение оповещений. Нет обязательных параметров.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.PermissionAlerts`: Объекта класса :class:`yandex_music.PermissionAlerts`
            представляющий оповещения, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/permission-alerts'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return PermissionAlerts.de_json(result, self)

    @log
    def account_experiments(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Experiments]:
        """Получение значений экспериментальных функций аккаунта.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Experiments`: Объекта класса :class:`yandex_music.Experiments`
            представляющий состояния экспериментальных функций, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/account/experiments'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Experiments.de_json(result, self)

    @log
    def consume_promo_code(self, code: str, language: str = 'en', timeout: Union[int, float] = None,
                           *args, **kwargs) -> Optional[PromoCodeStatus]:
        """Активация промо-кода.

        Args:
            code (:obj:`str`): Промо-код.
            language (:obj:`str`, optional): Язык ответа API в ISO 639-1.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.PromoCodeStatus`: Объекта класса :class:`yandex_music.PromoCodeStatus`
            представляющий информацию об активации промо-кода, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/account/consume-promo-code'

        result = self._request.post(url, {'code': code, 'language': language}, timeout=timeout, *args, **kwargs)

        return PromoCodeStatus.de_json(result, self)

    @log
    def feed(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Feed]:
        """Получение потока информации (фида) подобранного под пользователя. Содержит умные плейлисты.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Feed`: Объекта класса :class:`yandex_music.Feed`
            представляющий умные плейлисты пользователя, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/feed'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Feed.de_json(result, self)

    @log
    def feed_wizard_is_passed(self, timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        url = f'{self.base_url}/feed/wizard/is-passed'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return result.get('is_wizard_passed') or False

    @log
    def landing(self, blocks: Union[str, List[str]], timeout: Union[int, float] = None,
                *args, **kwargs) -> Optional[Landing]:
        """Получение лендинг-страницы содержащий блоки с новыми релизами, чартами, плейлистами с новинками и т.д.

        Поддерживаемые типы блоков: personalplaylists, promotions, new-releases, new-playlists, mixes,c hart, artists,
        albums, playlists, play_contexts.

        Args:
            blocks (:obj:`str` | :obj:`list` из :obj:`str`): Блок или список блоков необходимых для выдачи.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Landing`: Объекта класса :class:`yandex_music.Landing`
            представляющий лендинг-страницу, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/landing3'

        result = self._request.get(url, {'blocks': blocks}, timeout=timeout, *args, **kwargs)

        return Landing.de_json(result, self)

    @log
    def genres(self, timeout: Union[int, float] = None, *args, **kwargs) -> List[Genre]:
        """Получение жанров музыки.

        Args:
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`list` из :obj:`yandex_music.Genre`: Список объектов класса :class:`yandex_music.Genre`
            представляющих жанры музыки, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/genres'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Genre.de_list(result, self)

    @log
    def tracks_download_info(self, track_id: Union[str, int], get_direct_links: bool = False,
                             timeout: Union[int, float] = None, *args, **kwargs) -> List[DownloadInfo]:
        """Получение информации о доступных вариантах загрузки трека.

        Args:
            track_id (:obj:`str` | :obj:`list` из :obj:`str`): Уникальный идентификатор трека или треков.
            get_direct_links (:obj:`bool`, optional): Получить ли при вызове метода прямую ссылку на загрузку.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`list` из :obj:`yandex_music.DownloadInfo`: Список объектов класса :class:`yandex_music.DownloadInfo`
            представляющих варианты загрузки трека, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/tracks/{track_id}/download-info'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return DownloadInfo.de_list(result, self, get_direct_links)

    @log
    def track_supplement(self, track_id: Union[str, int], timeout: Union[int, float] = None,
                         *args, **kwargs) -> Optional[Supplement]:
        """Получение дополнительной информации о треке.

        Args:
            track_id (:obj:`str`): Уникальный идентификатор трека.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Supplement`: Объект класса `yandex_music.Supplement` представляющий дополнительную
                информацию о треке.

        """

        url = f'{self.base_url}/tracks/{track_id}/supplement'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Supplement.de_json(result, self)

    @log
    def play_audio(self,
                   track_id: Union[str, int],
                   from_: str,
                   album_id: Union[str, int],
                   playlist_id: str = None,
                   from_cache: bool = False,
                   play_id: str = None,
                   uid: int = None,
                   timestamp: str = None,
                   track_length_seconds: int = 0,
                   total_played_seconds: int = 0,
                   end_position_seconds: int = 0,
                   client_now: str = None,
                   timeout: Union[int, float] = None,
                   *args, **kwargs) -> bool:
        """Метод для отправки текущего состояния прослушиваемого трека.

        Args:
            track_id (:obj:`str` | :obj:`int`): Уникальный идентификатор трека.
            from_ (:obj:`str`): Наименования клиента с которого происходит прослушивание.
            album_id (:obj:`str` | :obj:`int`): Уникальный идентификатор альбома.
            playlist_id (:obj:`str`, optional): Уникальный идентификатор плейлиста, если таковой прослушивается.
            from_cache (:obj:`bool`, optional): Проигрывается ли трек с кеша.
            play_id (:obj:`str`, optional): Уникальный идентификатор проигрывания.
            uid (:obj:`int`, optional): Уникальный идентификатор пользователя.
            timestamp (:obj:`str`, optional): Текущая дата и время в ISO.
            track_length_seconds (:obj:`int`, optional): Продолжительность трека в секундах.
            total_played_seconds (:obj:`int`, optional): Сколько было всего воспроизведено трека в секундах.
            end_position_seconds (:obj:`int`, optional): Окончательное значение воспроизведенных секунд.
            client_now (:obj:`str`, optional): Текущая дата и время клиента в ISO.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`bool`: :obj:`True` при успешном выполнении запроса, иначе :obj:`False`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if uid is None and self.me is not None:
            uid = self.me.account.uid

        url = f'{self.base_url}/play-audio'

        data = {
            'track-id': track_id,
            'from-cache': from_cache,
            'from': from_,
            'play-id': play_id or '',
            'uid': uid,
            'timestamp': timestamp or f'{datetime.now().isoformat()}Z',
            'track-length-seconds': track_length_seconds,
            'total-played-seconds': total_played_seconds,
            'end-position-seconds': end_position_seconds,
            'album-id': album_id,
            'playlist-id': playlist_id,
            'client-now': client_now or f'{datetime.now().isoformat()}Z'
        }

        result = self._request.post(url, data, timeout=timeout, *args, **kwargs)

        return result == 'ok'

    def albums_with_tracks(self, album_id: Union[str, int], timeout: Union[int, float] = None,
                           *args, **kwargs) -> Optional[Album]:
        """Получение альбома по его уникальному идентификатору вместе с треками.

        Args:
            album_id (:obj:`str` | :obj:`int`): Уникальный идентификатор альбома.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`list` из :obj:`yandex_music.Album`: Объект класса :class:`yandex_music.Album` представляющий альбом,
            иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/albums/{album_id}/with-tracks'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Album.de_json(result, self)

    @log
    def search(self,
               text: str,
               nocorrect: bool = False,
               type_: str = 'all',
               page: int = 0,
               playlist_in_best: bool = True,
               timeout: Union[int, float] = None,
               *args, **kwargs) -> Optional[Search]:
        """Осуществление поиска по запросу и типу, получение результатов.

        Args:
            text (:obj:`str`): Текст запроса.
            nocorrect (:obj:`bool`): Без исправлений ли TODO.
            type_ (:obj:`str`): Среди какого типа искать (трек, плейлист, альбом, исполнитель).
            page (:obj:`int`): Номер страницы.
            playlist_in_best (:obj:`bool`): Выдавать ли плейлисты лучшим вариантом поиска.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Search`: Объекта класса :class:`yandex_music.Search`
            представляющий результаты поиска, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/search'

        params = {
            'text': text,
            'nocorrect': nocorrect,
            'type': type_,
            'page': page,
            'playlist-in-best': playlist_in_best,
        }

        result = self._request.get(url, params, timeout=timeout, *args, **kwargs)

        return Search.de_json(result, self)

    @log
    def search_suggest(self, part: str, timeout: Union[int, float] = None,
                       *args, **kwargs) -> Optional[Suggestions]:
        """Получение подсказок по введенной части поискового запроса.

        Args:
            part (:obj:`str`): Часть поискового запроса.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Suggestions`: Объекта класса :class:`yandex_music.Suggestions`
            представляющий подсказки для запроса, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/search/suggest'

        result = self._request.get(url, {'part': part}, timeout=timeout, *args, **kwargs)

        return Suggestions.de_json(result, self)

    @log
    def users_playlists(self, kind: Union[List[Union[str, int]], str, int], user_id: str = None,
                        timeout: Union[int, float] = None,  *args, **kwargs) -> List[Playlist]:
        """Получение плейлиста или списка плейлистов по уникальным идентификаторам.

        Args:
            kind (:obj:`str` | :obj:`int` | :obj:`list` из :obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста
                или их список.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`list` из :obj:`yandex_music.Playlist`: Список объектов класса :class:`yandex_music.Playlist`
            представляющих плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists'

        data = {
            'kinds': kind
        }

        result = self._request.post(url, data, timeout=timeout, *args, **kwargs)

        return Playlist.de_list(result, self)

    @log
    def users_playlists_create(self, title: str, visibility: str = 'public', user_id: str = None,
                               timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Playlist]:
        """Создание плейлиста.

        Args:
            title (:obj:`str`): Название.
            visibility (:obj:`str`, optional): Модификатор доступа.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Playlist`: Объекта класса :class:`yandex_music.Playlist`
            представляющий созданный плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists/create'

        data = {
            'title': title,
            'visibility': visibility
        }

        result = self._request.post(url, data, timeout=timeout, *args, **kwargs)

        return Playlist.de_json(result, self)

    @log
    def users_playlists_delete(self, kind: Union[str, int], user_id: str = None,
                               timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        """Удаление плейлиста.

        Args:
            kind (:obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`bool`: :obj:`True` при успешном выполнении запроса, иначе :obj:`False`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists/{kind}/delete'

        result = self._request.post(url, timeout=timeout, *args, **kwargs)

        return result == 'ok'

    @log
    def users_playlists_name(self, kind: Union[str, int], name: str, user_id: str = None,
                             timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Playlist]:
        """Изменение названия плейлиста.

        Args:
            kind (:obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста.
            name (:obj:`str`): Новое название.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Playlist`: Объекта класса :class:`yandex_music.Playlist`
            представляющий изменённый плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists/{kind}/name'

        result = self._request.post(url, {'value': name}, timeout=timeout, *args, **kwargs)

        return Playlist.de_json(result, self)

    @log
    def users_playlists_change(self, kind: Union[str, int], diff: str, revision: int = 1, user_id: str = None,
                               timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Playlist]:
        """Изменение плейлиста.

        Для получения отличий есть вспомогательный класс :class:`from yandex_music.utils.difference.Difference`.
        Так же существуют уже готовые методы-обёртки над операциями.

        Args:
            kind (:obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста.
            revision (:obj:`int`): TODO.
            diff (:obj:`str`): JSON представления отличий старого и нового плейлиста.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Playlist`: Объекта класса :class:`yandex_music.Playlist`
            представляющий изменённый плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists/{kind}/change'

        data = {
            'kind': kind,
            'revision': revision,
            'diff': diff
        }

        result = self._request.post(url, data, timeout=timeout, *args, **kwargs)

        return Playlist.de_json(result, self)

    @log
    def users_playlists_insert_track(self, kind: Union[str, int], track_id: Union[str, int], album_id: Union[str, int],
                                     at: int = 0, revision: int = 1, user_id: str = None,
                                     timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Playlist]:
        """Добавление трека в плейлист.

        Трек можно вставить с любое место плейлиста задав индекс вставки (аргумент at).

        Args:
            kind (:obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста.
            track_id (:obj:`str` | :obj:`int`): Уникальный идентификатор трека.
            album_id (:obj:`str` | :obj:`int`): Уникальный идентификатор альбома.
            at (:obj:`int`): Индекс для вставки.
            revision (:obj:`int`): TODO.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Playlist`: Объекта класса :class:`yandex_music.Playlist`
            представляющий изменённый плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        diff = Difference().add_insert(at, {'id': track_id, 'album_id': album_id})

        return self.users_playlists_change(kind, diff.to_json(), revision, user_id, timeout, *args, **kwargs)

    @log
    def users_playlists_delete_track(self, kind: Union[str, int], from_: int, to: int, revision: int = 1,
                                     user_id: str = None, timeout: Union[int, float] = None,
                                     *args, **kwargs) -> Optional[Playlist]:
        """Удаление треков из плейлиста.

        Для удаление необходимо указать границы с какого по какой элемент (трек) удалить.

        Args:
            kind (:obj:`str` | :obj:`int`): Уникальный идентификатор плейлиста.
            from_ (:obj:`int`): С какого индекса.
            to (:obj:`int`): По какой индекс.
            revision (:obj:`int`): TODO.
            user_id: (:obj:`int`, optional): Уникальный идентификатор пользователя владеющим плейлистом.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.Playlist`: Объекта класса :class:`yandex_music.Playlist`
            представляющий изменённый плейлист, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        diff = Difference().add_delete(from_, to)

        return self.users_playlists_change(kind, diff.to_json(), revision, user_id, timeout, *args, **kwargs)

    @log
    def rotor_account_status(self, timeout: Union[int, float] = None, *args, **kwargs) -> Optional[Status]:
        url = f'{self.base_url}/rotor/account/status'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Status.de_json(result, self)

    @log
    def rotor_stations_dashboard(self, timeout: Union[int, float] = None,
                                 *args, **kwargs) -> Optional[Dashboard]:
        url = f'{self.base_url}/rotor/stations/dashboard'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Dashboard.de_json(result, self)

    @log
    def rotor_stations_list(self, language: str = 'en', timeout: Union[int, float] = None,
                            *args, **kwargs) -> List[StationResult]:
        url = f'{self.base_url}/rotor/stations/list'

        result = self._request.get(url, {'language': language}, timeout=timeout, *args, **kwargs)

        return StationResult.de_list(result, self)

    @log
    def rotor_station_genre_feedback(self, genre: str, type_: str, timestamp: int = None,
                                     from_: str = None, batch_id: Union[str, int] = None,
                                     track_id: str = None, timeout: Union[int, float] = None,
                                     *args, **kwargs) -> bool:
        if timestamp is None:
            timestamp = datetime.now().timestamp()

        url = f'{self.base_url}/rotor/station/genre:{genre}/feedback'

        params = {}
        data = {
            'type': type_,
            'timestamp': timestamp
        }

        if batch_id and track_id:
            data.update({'trackId': track_id})
            params = {'batch-id': batch_id}

        if from_:
            data.update({'from': from_})

        result = self._request.post(url, params=params, json=data, timeout=timeout, *args, **kwargs)

        return result == 'ok'

    @log
    def rotor_station_genre_feedback_radio_started(self, genre: str, from_: str, timestamp: int = None,
                                                   timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self.rotor_station_genre_feedback(genre, 'radioStarted', timestamp, from_, timeout, *args, **kwargs)

    @log
    def rotor_station_genre_feedback_track_started(self, genre: str, track_id: str, batch_id: Union[str, int],
                                                   timestamp: int = None, timeout: Union[int, float] = None,
                                                   *args, **kwargs) -> bool:
        return self.rotor_station_genre_feedback(genre, 'trackStarted', timestamp, track_id=track_id, batch_id=batch_id,
                                                 timeout=timeout, *args, **kwargs)

    @log
    def rotor_station_genre_info(self, genre: str, timeout: Union[int, float] = None,
                                 *args, **kwargs) -> List[StationResult]:
        url = f'{self.base_url}/rotor/station/genre:{genre}/info'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return StationResult.de_list(result, self)

    @log
    def rotor_station_genre_tracks(self, genre: str, timeout: Union[int, float] = None,
                                   *args, **kwargs) -> Optional[StationTracksResult]:
        url = f'{self.base_url}/rotor/station/genre:{genre}/tracks'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return StationTracksResult.de_json(result, self)

    @log
    def artists_brief_info(self, artist_id: Union[str, int], timeout: Union[int, float] = None,
                           *args, **kwargs) -> Optional[BriefInfo]:
        url = f'{self.base_url}/artists/{artist_id}/brief-info'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return BriefInfo.de_json(result, self)

    @log
    def artists_tracks(self, artist_id: Union[str, int], page: int = 0, page_size: int = 20,
                       timeout: Union[int, float] = None, *args, **kwargs) -> Optional[ArtistTracks]:
        """Получение треков артиста.

        Args:
            artist_id (:obj:`str` | :obj:`int`): Уникальный идентификатор артиста.
            page (:obj:`int`, optional): Номер страницы.
            page_size (:obj:`int`, optional): Количество треков на странице.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.ArtistsTracks`: Объекта класса :class:`yandex_music.ArtistsTracks`
            представляющий страницу списка треков артиста, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/artists/{artist_id}/tracks'

        params = {
            'page': page,
            'page-size': page_size
        }

        result = self._request.get(url, params, timeout=timeout, *args, **kwargs)

        return ArtistTracks.de_json(result, self)

    @log
    def artists_direct_albums(self, artist_id: Union[str, int], page: int = 0, page_size: int = 20,
                              sort_by: str = 'year', timeout: Union[int, float] = None,
                              *args, **kwargs) -> Optional[ArtistAlbums]:
        """Получение альбомов артиста.

        Известные значения для sort_by: year, rating.

        Args:
            artist_id (:obj:`str` | :obj:`int`): Уникальный идентификатор артиста.
            page (:obj:`int`, optional): Номер страницы.
            page_size (:obj:`int`, optional): Количество альбомов на странице.
            sort_by (:obj:`str`, optional): Параметр для сортировки.
            timeout (:obj:`int` | :obj:`float`, optional): Если это значение указано, используется как время ожидания
                ответа от сервера вместо указанного при создании пула.
            **kwargs (:obj:`dict`, optional): Произвольные аргументы (будут переданы в запрос).

        Returns:
            :obj:`yandex_music.ArtistAlbums`: Объекта класса :class:`yandex_music.ArtistsTracks`
                представляющий страницу списка альбомов артиста, иначе :obj:`None`.

        Raises:
            :class:`yandex_music.YandexMusicError`
        """

        url = f'{self.base_url}/artists/{artist_id}/direct-albums'

        params = {
            'sort-by': sort_by,
            'page': page,
            'page-size': page_size
        }

        result = self._request.get(url, params, timeout=timeout, *args, **kwargs)

        return ArtistAlbums.de_json(result, self)

    def _like_action(self, object_type: str, ids: Union[List[Union[str, int]], str, int], remove: bool = False,
                     user_id: Union[str, int] = None, timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        action = 'remove' if remove else 'add-multiple'
        url = f'{self.base_url}/users/{user_id}/likes/{object_type}s/{action}'

        result = self._request.post(url, {f'{object_type}-ids': ids}, timeout=timeout, *args, **kwargs)

        if object_type == 'track':
            return 'revision' in result

        return result == 'ok'

    @log
    def users_likes_tracks_add(self, track_ids: Union[List[Union[str, int]], str, int], user_id: Union[str, int] = None,
                               timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('track', track_ids, False, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_tracks_remove(self, track_ids: Union[List[Union[str, int]], str, int],
                                  user_id: Union[str, int] = None,
                                  timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('track', track_ids, True, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_artists_add(self, artist_ids: Union[List[Union[str, int]], str, int],
                                user_id: Union[str, int] = None,
                                timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('artist', artist_ids, False, user_id, timeout, *args, **kwargs)

    def users_likes_artists_remove(self, artist_ids: Union[List[Union[str, int]], str, int],
                                   user_id: Union[str, int] = None,
                                   timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('artist', artist_ids, True, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_playlists_add(self, playlist_ids: Union[List[Union[str, int]], str, int],
                                  user_id: Union[str, int] = None,
                                  timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('playlist', playlist_ids, False, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_playlists_remove(self, playlist_ids: Union[List[Union[str, int]], str, int],
                                     user_id: Union[str, int] = None,
                                     timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('playlist', playlist_ids, True, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_albums_add(self, album_ids: Union[List[Union[str, int]], str, int], user_id: Union[str, int] = None,
                               timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('album', album_ids, False, user_id, timeout, *args, **kwargs)

    @log
    def users_likes_albums_remove(self, album_ids: Union[List[Union[str, int]], str, int],
                                  user_id: Union[str, int] = None,
                                  timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._like_action('album', album_ids, True, user_id, timeout, *args, **kwargs)

    def _get_list(self, object_type: str, ids: Union[List[Union[str, int]], int, str],
                  params: dict = None, timeout: Union[int, float] = None,
                  *args, **kwargs) -> List[Union[Artist, Album, Track, Playlist]]:
        if params is None:
            params = {}
        params.update({f'{object_type}-ids': ids})

        url = f'{self.base_url}/{object_type}s' + ('/list' if object_type == 'playlist' else '')

        result = self._request.post(url, params, timeout=timeout, *args, **kwargs)

        return de_list.get(object_type)(result, self)

    @log
    def artists(self, artist_ids: Union[List[Union[str, int]], int, str], timeout: Union[int, float] = None,
                *args, **kwargs) -> List[Artist]:
        return self._get_list('artist', artist_ids, timeout=timeout, *args, **kwargs)

    @log
    def albums(self, album_ids: Union[List[Union[str, int]], int, str], timeout: Union[int, float] = None,
               *args, **kwargs) -> List[Album]:
        return self._get_list('album', album_ids, timeout=timeout, *args, **kwargs)

    @log
    def tracks(self, track_ids: Union[List[Union[str, int]], int, str], with_positions: bool = True,
               timeout: Union[int, float] = None, *args, **kwargs) -> List[Track]:
        return self._get_list('track', track_ids, {'with-positions': with_positions}, timeout, *args, **kwargs)

    @log
    def playlists_list(self, playlist_ids: Union[List[Union[str, int]], int, str], timeout: Union[int, float] = None,
                       *args, **kwargs) -> List[Playlist]:
        return self._get_list('playlist', playlist_ids, timeout=timeout, *args, **kwargs)

    @log
    def users_playlists_list(self, user_id: Union[str, int] = None, timeout: Union[int, float] = None,
                             *args, **kwargs) -> List[Playlist]:
        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/playlists/list'

        result = self._request.get(url, timeout=timeout, *args, **kwargs)

        return Playlist.de_list(result, self)

    def _get_likes(self, object_type: str, user_id: Union[str, int] = None, params: dict = None,
                   timeout: Union[int, float] = None, *args, **kwargs) \
            -> Union[List[ArtistsLikes], List[AlbumsLikes], List[PlaylistsLikes], Optional[TracksList]]:
        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/likes/{object_type}s'

        result = self._request.get(url, params, timeout=timeout, *args, **kwargs)

        if object_type == 'track':
            return TracksList.de_json(result.get('library'), self)

        return de_list_likes.get(object_type)(result, self)

    @log
    def users_likes_tracks(self, user_id: Union[str, int] = None, if_modified_since_revision: int = 0,
                           timeout: Union[int, float] = None, *args, **kwargs) -> Optional[TracksList]:
        return self._get_likes('track', user_id, {'if-modified-since-revision': if_modified_since_revision}, timeout,
                               *args, **kwargs)

    @log
    def users_likes_albums(self, user_id: Union[str, int] = None, rich: bool = True, timeout: Union[int, float] = None,
                           *args, **kwargs) -> List[AlbumsLikes]:
        return self._get_likes('album', user_id, {'rich': rich}, timeout, *args, **kwargs)

    @log
    def users_likes_artists(self, user_id: Union[str, int] = None, with_timestamps: bool = True,
                            timeout: Union[int, float] = None, *args, **kwargs) -> List[ArtistsLikes]:
        return self._get_likes('artist', user_id, {'with-timestamps': with_timestamps}, timeout, *args, **kwargs)

    @log
    def users_likes_playlists(self, user_id: Union[str, int] = None, timeout: Union[int, float] = None,
                              *args, **kwargs) -> List[PlaylistsLikes]:
        return self._get_likes('playlist', user_id, timeout=timeout, *args, **kwargs)

    @log
    def users_dislikes_tracks(self, user_id: Union[str, int] = None, if_modified_since_revision: int = 0,
                              timeout: Union[int, float] = None, *args, **kwargs) -> Optional[TracksList]:
        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        url = f'{self.base_url}/users/{user_id}/dislikes/tracks'

        result = self._request.get(url, {'if_modified_since_revision': if_modified_since_revision},
                                   timeout=timeout, *args, **kwargs)

        return TracksList.de_json(result.get('library'), self)

    def _dislike_action(self, ids: Union[List[Union[str, int]], str, int], remove: bool = False,
                        user_id: Union[str, int] = None, timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        if user_id is None and self.me is not None:
            user_id = self.me.account.uid

        action = 'remove' if remove else 'add-multiple'
        url = f'{self.base_url}/users/{user_id}/dislikes/tracks/{action}'

        result = self._request.post(url, {f'track-ids': ids}, timeout=timeout, *args, **kwargs)

        return 'revision' in result

    @log
    def users_dislikes_tracks_add(self, track_ids: Union[List[Union[str, int]], str, int],
                                  user_id: Union[str, int] = None,
                                  timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._dislike_action(track_ids, False, user_id, timeout, *args, **kwargs)

    @log
    def users_dislikes_tracks_remove(self, track_ids: Union[List[Union[str, int]], str, int],
                                     user_id: Union[str, int] = None,
                                     timeout: Union[int, float] = None, *args, **kwargs) -> bool:
        return self._dislike_action(track_ids, True, user_id, timeout, *args, **kwargs)

    # camelCase псевдонимы

    #: Псевдоним для :attr:`from_credentials`
    fromCredentials = from_credentials
    #: Псевдоним для :attr:`from_token`
    fromToken = from_token
    #: Псевдоним для :attr:`generate_token_by_username_and_password`
    generateTokenByUsernameAndPassword = generate_token_by_username_and_password
    #: Псевдоним для :attr:`account_status`
    accountStatus = account_status
    #: Псевдоним для :attr:`permission_alerts`
    permissionAlerts = permission_alerts
    #: Псевдоним для :attr:`account_experiments`
    accountExperiments = account_experiments
    #: Псевдоним для :attr:`consume_promo_code`
    consumePromoCode = consume_promo_code
    #: Псевдоним для :attr:`feed_wizard_is_passed`
    feedWizardIsPassed = feed_wizard_is_passed
    #: Псевдоним для :attr:`tracks_download_info`
    tracksDownloadInfo = tracks_download_info
    #: Псевдоним для :attr:`track_supplement`
    trackSupplement = track_supplement
    #: Псевдоним для :attr:`play_audio`
    playAudio = play_audio
    #: Псевдоним для :attr:`albums_with_tracks`
    albumsWithTracks = albums_with_tracks
    #: Псевдоним для :attr:`search_suggest`
    searchSuggest = search_suggest
    #: Псевдоним для :attr:`users_playlists`
    usersPlaylists = users_playlists
    #: Псевдоним для :attr:`users_playlists_create`
    usersPlaylistsCreate = users_playlists_create
    #: Псевдоним для :attr:`users_playlists_delete`
    usersPlaylistsDelete = users_playlists_delete
    #: Псевдоним для :attr:`users_playlists_name`
    usersPlaylistsName = users_playlists_name
    #: Псевдоним для :attr:`users_playlists_change`
    usersPlaylistsChange = users_playlists_change
    #: Псевдоним для :attr:`users_playlists_insert_track`
    usersPlaylistsInsertTrack = users_playlists_insert_track
    #: Псевдоним для :attr:`users_playlists_delete_track`
    usersPlaylistsDeleteTrack = users_playlists_delete_track
    #: Псевдоним для :attr:`rotor_account_status`
    rotorAccountStatus = rotor_account_status
    #: Псевдоним для :attr:`rotor_stations_dashboard`
    rotorStationsDashboard = rotor_stations_dashboard
    #: Псевдоним для :attr:`rotor_stations_list`
    rotorStationsList = rotor_stations_list
    #: Псевдоним для :attr:`rotor_station_genre_feedback`
    rotorStationGenreFeedback = rotor_station_genre_feedback
    #: Псевдоним для :attr:`rotor_station_genre_feedback_radio_started`
    rotorStationGenreFeedbackRadioStarted = rotor_station_genre_feedback_radio_started
    #: Псевдоним для :attr:`rotor_station_genre_feedback_track_started`
    rotorStationGenreFeedbackTrackStarted = rotor_station_genre_feedback_track_started
    #: Псевдоним для :attr:`rotor_station_genre_info`
    rotorStationGenreInfo = rotor_station_genre_info
    #: Псевдоним для :attr:`rotor_station_genre_tracks`
    rotorStationGenreTracks = rotor_station_genre_tracks
    #: Псевдоним для :attr:`artists_brief_info`
    artistsBriefInfo = artists_brief_info
    #: Псевдоним для :attr:`artists_tracks`
    artistsTracks = artists_tracks
    #: Псевдоним для :attr:`artists_direct_albums`
    artistsDirectAlbums = artists_direct_albums
    #: Псевдоним для :attr:`users_likes_tracks_add`
    usersLikesTracksAdd = users_likes_tracks_add
    #: Псевдоним для :attr:`users_likes_tracks_remove`
    usersLikesTracksRemove = users_likes_tracks_remove
    #: Псевдоним для :attr:`users_likes_artists_add`
    usersLikesArtistsAdd = users_likes_artists_add
    #: Псевдоним для :attr:`users_likes_artists_remove`
    usersLikesArtistsRemove = users_likes_artists_remove
    #: Псевдоним для :attr:`users_likes_playlists_add`
    usersLikesPlaylistsAdd = users_likes_playlists_add
    #: Псевдоним для :attr:`users_likes_playlists_remove`
    usersLikesPlaylistsRemove = users_likes_playlists_remove
    #: Псевдоним для :attr:`users_likes_albums_add`
    usersLikesAlbumsAdd = users_likes_albums_add
    #: Псевдоним для :attr:`users_likes_albums_remove`
    usersLikesAlbumsRemove = users_likes_albums_remove
    #: Псевдоним для :attr:`playlists_list`
    playlistsList = playlists_list
    #: Псевдоним для :attr:`users_playlists_list`
    usersPlaylistsList = users_playlists_list
    #: Псевдоним для :attr:`users_likes_tracks`
    usersLikesTracks = users_likes_tracks
    #: Псевдоним для :attr:`users_likes_albums`
    usersLikesAlbums = users_likes_albums
    #: Псевдоним для :attr:`users_likes_artists`
    usersLikesArtists = users_likes_artists
    #: Псевдоним для :attr:`users_likes_playlists`
    usersLikesPlaylists = users_likes_playlists
    #: Псевдоним для :attr:`users_dislikes_tracks`
    usersDislikesTracks = users_dislikes_tracks
    #: Псевдоним для :attr:`users_dislikes_tracks_add`
    usersDislikesTracksAdd = users_dislikes_tracks_add
    #: Псевдоним для :attr:`users_dislikes_tracks_remove`
    usersDislikesTracksRemove = users_dislikes_tracks_remove
