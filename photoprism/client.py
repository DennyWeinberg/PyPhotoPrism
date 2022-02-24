import json
from functools import wraps
import time

import requests


INFINITE = 2**31-1


def check_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        
        if not response.ok:
            try:
                print(response.json())
            except ValueError:
                pass

        response.raise_for_status()

        return response.json()

    return wrapper


class Client:
    """
    API doc:
    https://pkg.go.dev/github.com/photoprism/photoprism/internal/api
    """

    default_domain = 'https://demo.photoprism.org'
    default_root = '/api/v1'

    def __init__(self, username=None, password=None, domain=default_domain, root=default_root):
        self.base_url = domain + root
        self.session = requests.Session()
        if username:
            session_data = self._create_session(username=username, password=password)
            self.session.headers['X-Session-ID'] = session_data['id']

    def _create_session(self, username, password):
        return self._post(
            '/session', {
                'username': username,
                'password': password
            }
        )

    @check_response
    def _get(self, url_path, params=None):
        return self.session.get(self.base_url + url_path, params=params)

    @check_response
    def _post(self, url_path, json=None, files=None):
        return self.session.post(
            self.base_url + url_path,
            json=json,
            files=files
        )

    @check_response
    def _put(self, url_path, json=None, files=None):
        return self.session.put(
            self.base_url + url_path,
            json=json,
            files=files
        )

    def get_albums(self, count=INFINITE, **params):
        """
        Search an album
        count, offset, category, type=album
        """

        params['count'] = count
        return self._get('/albums', params)

    def create_album(self, title):
        """
        Create an album
        """

        return self._post('/albums', json={'Title': title})

    def add_photo_to_album(self, album_uid, photo_uid):
        """
        Add a photo to an album
        """

        return self._post(
            f'/albums/{album_uid}/photos',
            json={'photos': [photo_uid]}
        )

    def get_photos(self, count=INFINITE, **params):
        """
        Search photos
        count, offset, merged, country, camera, lens, label, year, month, color, order, public, quality, q
        """

        params['count'] = count
        return self._get('/photos', params)

    def get_photo(self, uid):
        """
        Get a photo by uid
        """

        return self._get('/photos/' + uid)

    def add_label_to_photo(self, photo_uid, label_name, label_priority=10):
        """
        Add a label to a photo
        """

        return self._post(
            f'/photos/{photo_uid}/label',
            json={
                'Name': label_name,
                'Priority': label_priority
            }
        )

    def upload_photo(self, name, bytes, mimetype='image/jpeg', import_afterwards=True, move=True, album_names=[]):
        """
        Upload a photo
        """

        event = int(time.time())
        files = {'files': (name, bytes, mimetype)}

        self._post(
            f'/upload/{event}',
            json={},
            files=files
        )

        if import_afterwards:
            self._import_photo(move=move, album_names=album_names)

        return event

    def _import_photo(self, event, move=True, album_names=[]):
        """
        Import a photo
        """

        self._post(
            f'/import/upload/{event}',
            json={'move': move, 'albums': album_names},
        )

    def update_photo(self, photo_uid, **params):
        """
        Update photo metdata
        Description DescriptionSrc
        """

        return self._put(
            f'/photos/{photo_uid}',
            json=params
        )
