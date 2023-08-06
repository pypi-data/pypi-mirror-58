#!/usr/bin/env python3

from secobj import *
import unittest , os , glob

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.key = 'spam and eggs'
        self.enc = EncObject(self.key)
        self.filename = '/tmp/secobj.test'
        self.obj = [1 , 2 , 3 , 4]
        self._del_file()

    def test_file_obj_encrypt(self):
        fh = open(self.filename , 'wb')
        self.enc.encrypt_to_file(self.obj , fh)
        fh.close()
        fh = open(self.filename , 'rb')
        obj = self.enc.decrypt_from_file(fh , True)
        self.assertEqual(self.obj , obj)
        fh.close()
        self._del_file()

    def test_filename_encrypt(self):
        self.enc.encrypt_to_file(self.obj , self.filename)
        obj = self.enc.decrypt_from_file(self.filename , True)
        self.assertEqual(self.obj , obj)
        self._del_file()

    def test_string_encrypt(self):
        encStr , iv = self.enc.encrypt_to_str(self.obj)
        obj = self.enc.decrypt_from_str(encStr , iv)
        self.assertEqual(self.obj , obj)
        self._del_file()

    def test_filename_chg_key(self):
        new_key = 'monkeys are awesome'
        self.enc.encrypt_to_file(self.obj , self.filename)
        self.enc.chg_key_for_file(self.filename , self.key , new_key)
        self.enc.update_key(new_key)
        obj = self.enc.decrypt_from_file(self.filename , True)
        self.assertEqual(self.obj , obj)
        self._del_file()

    def test_file_obj_chg_key(self):
        new_key = 'monkeys are awesome'
        fh = open(self.filename , 'w+b')
        self.enc.encrypt_to_file(self.obj , fh)
        fh.seek(0)
        self.enc.chg_key_for_file(fh , self.key , new_key)
        fh.seek(0)
        self.enc.update_key(new_key)
        obj = self.enc.decrypt_from_file(fh , True)
        fh.close()
        self.assertEqual(self.obj , obj)
        self._del_file()

    def tearDown(self):
        for f in glob.glob('./*.pyc'):
            try:
                os.unlink(f)
            except:
                pass
        self._del_file()

    def _del_file(self):
        try:
            os.unlink(self.filename)
        except:
            pass


if __name__ == '__main__':
    unittest.main()
