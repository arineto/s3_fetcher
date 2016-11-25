# -*- coding: utf-8 -*-
from s3 import S3
import os

__all__ = ['Connection']


class Connection(object):

    def __init__(self):
        self.s3 = S3()

    def ensure_dir(self, local_path):
        local_dir = os.path.join(*local_path.split('/')[:-1])
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

    def build_path(self, *args):
        return self.s3.caminho(*args)

    def get_all_keys(self, prefix):
        return self.s3.get_all_keys(prefix)

    def file_exists_on_s3(self, s3_path):
        return self.s3.existe_no_s3(s3_path)

    def send_to_s3(self, local_path, s3_path):
        if not self.exists_on_s3(s3_path):
            self.s3.enviar(local_path, s3_path)

    def retrieve_from_s3(self, local_path, s3_path=None, key_s3=None):
        self.ensure_dir(local_path)
        if key_s3:
            s3_path = key_s3.name
        if not self.file_exists_on_s3(s3_path):
            raise Exception('File not found on S3')
        self.s3.obter(local_path, s3_path, key_s3)
