#!/usr/bin/env python3
'''File object of RAO data'''

import os
import errno
import urllib
import hashlib
from dateutil import parser
from raodata import exceptions

class File():
    """

    File of RAO data

    """

    CACHE_PATH = os.path.expanduser('~') + "/.cache/raodata"

    def __init__(self, name, url, hash, date):
        """

        Initialisation

        """
        try:
            date = parser.parse(str(date))
        except ValueError:
            raise exceptions.InvalidDate("Date should be ISO 8601 format: '%Y-%m-%dT%H:%M:%S'")

        self.name = name
        self.url = url
        self.hash = hash
        self.date = date
        self.local_name = self.CACHE_PATH + "/" + hash
        self.downloaded = False


    def name(self):
        """

        Get file name

        """
        return self.name


    def hash(self):
        """

        Get file hash

        """
        return self.hash


    def url(self):
        """

        Get file url

        """
        return self.url


    def date(self):
        """

        Get file date

        """
        return self.date


    def download(self):
        """

        Downloads file. Save to cache folder

        """

        attempts = 0
        while True:
            try:
                if not os.path.exists(self.local_name):
                    _fp = urllib.request.urlopen(self.url)
                else:
                    _fp = open(self.local_name, "rb")

                content = _fp.read()
            except BaseException:
                raise exceptions.CannotDownloadFile("Cannot download file")

            try:
                md5 = hashlib.md5(content).hexdigest()
            except BaseException:
                md5 = ""

            if md5 != self.hash:
                if attempts <= 3:
                    attempts += 1
                else:
                    raise exceptions.InvalidFileHash("Invalid file hash")
            else:
                self._save_to_cache(content, self.local_name)
                break

        self.downloaded = True


    def _save_to_cache(self, content, path):
        """

        Save file to cache

        """
        if not os.path.exists(path):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError:
                pass

            with open(path, "wb") as _f:
                _f.write(content)

            _f.close()


    def handle(self):
        """

        Return file handler

        """
        if self.downloaded is False:
            self.download()

        return open(self.local_name, "rb")


    def contents(self):
        """

        Return file content

        """
        if self.downloaded is False:
            self.download()

        with open(self.local_name, "rb") as _f:
            _content = _f.read()

        _f.close()

        return _content


    def save_to(self, filepath):
        """

        Save file to

        """
        if self.downloaded is False:
            self.download()

        if not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise exceptions.CannotCreateDirectory("Can not create directory")

        with open(filepath, "wb") as _f:
            _f.write(self.contents())

        _f.close()
