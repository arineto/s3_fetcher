# -*- coding: utf-8 -*-
from connection import Connection
import settings
import re


class S3Fetcher(object):

    def __init__(self):
        self.numbers = self.get_numbers()
        self.connection = Connection()

    def get_numbers(self):
        numbers = []
        with open(settings.FILE_PATH, 'r') as numbers_file:
            for row in numbers_file:
                numbers.append(u''.join(re.findall(r'\d+', row)))
        return numbers

    def download_files(self, numbers, keys):
        for key in keys:
            local_path = self.connection.build_path(
                settings.DOWNLOAD_PATH, key.name
            )
            self.connection.retrieve_from_s3(local_path=local_path, key_s3=key)

    def execute(self):
        not_found = []
        for number in self.numbers:
            s3_path = self.connection.build_path(
                settings.AWS_SEARCH_DIR, number
            )

            keys = self.connection.get_all_keys(s3_path)
            if not keys:
                not_found.append(number)

            print number, 'Found' if keys else 'Not Found'
            self.download_files(number, keys)

        print u'\nProcessos não encontrados:'
        print not_found


if __name__ == '__main__':
    fetcher = S3Fetcher()
    fetcher.execute()
