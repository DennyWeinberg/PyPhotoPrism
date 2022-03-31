# PyPhotoPrism

Unofficial python client for the PhotoPrism API

## Install

```python
pip install git+https://github.com/PyPhotoPrism/PyPhotoPrism.git
```

## Usage

```python
from photoprism import Client

client = Client(username=None, password=None, domain='https://demo.photoprism.org', root='/api/v1')

# client...
```

```python
def get_albums(self, count=INFINITE, **params):
    """
    Search an album
    count, offset, category, type=album
    """

    pass

def create_album(self, title):
    """
    Create an album
    """

    pass

def add_photo_to_album(self, album_uid, photo_uid):
    """
    Add a photo to an album
    """

    pass

def get_photos(self, count=INFINITE, **params):
    """
    Search photos
    count, offset, merged, country, camera, lens, label, year, month, color, order, public, quality, q
    """

    pass

def get_photo(self, uid):
    """
    Get a photo by uid
    """

    pass

def add_label_to_photo(self, photo_uid, label_name, label_priority=10):
    """
    Add a label to a photo
    """

    pass

def upload_photo(self, name, bytes, mimetype='image/jpeg', import_afterwards=True, move=True, album_names=[]):
    """
    Upload a photo
    """

    pass

def _import_photo(self, event, move=True, album_names=[]):
    """
    Import a photo
    """

    pass

def update_photo(self, photo_uid, **params):
    """
    Update photo metdata
    Description DescriptionSrc
    """

    pass
```

Official PhotoPrism API doc: https://pkg.go.dev/github.com/photoprism/photoprism/internal/api
