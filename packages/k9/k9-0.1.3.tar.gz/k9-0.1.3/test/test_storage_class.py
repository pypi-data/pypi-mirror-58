from unittest import TestCase
from k9.storage import *

class TestStorage(TestCase):
    def test_create_storage_class(self):
        name = 'aws-storage-class'
        create_storage_class('storage.yml')

        self.assertTrue(storage_class_exists(name))

        delete_storage_class(name)

        self.assertFalse(storage_class_exists(name))
