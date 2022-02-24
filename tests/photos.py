import unittest

from photoprism import Client


class TestClass(unittest.TestCase):
    def test_upload():
        client = Client()
        client.upload_photo('20210104_223259.jpg', b'TODO', album_names=['Test Album'])
