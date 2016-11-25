# -*- coding: utf-8 -*-
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import settings


class S3(object):

    def __init__(self, *args, **kwargs):
        super(S3, self).__init__(*args, **kwargs)
        self._tmp = None
        self._conexao = None
        self._balde = None

    @property
    def conexao(self):
        if not self._conexao:
            self._conexao = S3Connection(
                settings.AWS_ACCESS_KEY_ID,
                settings.AWS_SECRET_ACCESS_KEY
            )
        return self._conexao

    @property
    def balde(self):
        if not self._balde:
            self._balde = self.conexao.get_bucket(
                settings.AWS_STORAGE_BUCKET_NAME
            )
        return self._balde

    def caminho(self, *args):
        return os.path.join(*args)

    def get_all_keys(self, prefix):
        return self.balde.get_all_keys(prefix=prefix)

    def existe_no_s3(self, caminho_s3):
        chave_s3 = self.balde.get_key(caminho_s3)
        if chave_s3:
            return True
        return False

    def enviar(self, caminho_arquivo_local, caminho_s3):
        chave_s3 = Key(self.balde)
        chave_s3.key = caminho_s3
        chave_s3.set_contents_from_filename(caminho_arquivo_local)
        chave_s3.set_acl('private')

    def obter(self, caminho_arquivo_local, caminho_s3=None, key_s3=None):
        if key_s3:
            chave_s3 = key_s3
        elif caminho_s3:
            chave_s3 = self.balde.get_key(caminho_s3)
        arquivo = os.path.basename(chave_s3.name)
        with open(caminho_arquivo_local, 'w+') as arquivo:
            chave_s3.get_file(arquivo)
