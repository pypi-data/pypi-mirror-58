#!/usr/bin/env python3
'''This script allows get inforamation for RAO data'''

from datetime import datetime
from raodata.File import File
from raodata import exceptions
from dateutil import parser
import zeep
from zeep import Client
import requests


class Data():
    '''
    This class allows get information for RAO data
    '''

    SERVICE_URL = "data.rao.istp.ac.ru/Access.wsdl"

    def get_instruments(self):
        """
        Retrun list of avalible instruments
        """

        client = self._connect()
        return client.service.instrumentsList()


    def get_file_types(self, instrument):
        """
        Retrun list of types for instrument
        """

        client = self._connect()
        return client.service.instrumentFileTypes(instrument)


    def get_types_by_instruments(self):
        """
        Retrun list of instruments with avalible types
        """

        client = self._connect()
        return client.service.typesByInstrumentsList()


    def get_files(self, instrument, type, datefrom, dateto=""):
        """
        Retrun list of files in period
        """

        self._check_arguments(instrument, type, datefrom, dateto)

        datefrom = parser.parse(datefrom)
        if dateto == "":
            dateto = datefrom
            dateto = dateto.replace(hour=23, minute=59, second=59)
            dateto = datetime.strftime(dateto, "%Y-%m-%dT%H:%M:%S")

        client = self._connect()

        try:
            files = client.service.getFiles(instrument, type, datefrom, dateto)
        except zeep.exceptions.Fault as error:
            if error.code == "INVALIDINSTRUMENTORTYPE":
                raise exceptions.InvalidInstrumentOrType("Invalid instrument or type")
            elif error.code == "INVALIDDATE":
                raise exceptions.InvalidDate("Date should be ISO 8601 format: '%Y-%m-%dT%H:%M:%S'")
            else:
                raise Exception(error.message)

        if not files:
            raise exceptions.NoDataDuringThisPeriod("No avalible data during this period")
        for _f in files:
            file = File(_f.filename, _f.URL, _f.hash, _f.date)
            yield file


    def _check_arguments(self, instrument, filetype, datefrom, dateto):
        """
        Validate the inputs arguments
        """
        if isinstance(instrument, str) != True:
            raise exceptions.InstrumentNotString("Instrument should be a string")

        if isinstance(filetype, str) != True:
            raise exceptions.FiletypeNotString("File type should be a string")

        try:
            datefrom = parser.parse(datefrom)
            if dateto != "":
                dateto = parser.parse(dateto)
        except ValueError:
            raise exceptions.InvalidDate("Date should be ISO 8601 format: '%Y-%m-%dT%H:%M:%S'")

        return True


    def _connect(self):
        """
        Set connection to the SOAP server
        """
        protocol = "http://"
        try:
            request = requests.get(protocol + self.SERVICE_URL, allow_redirects=False)
            if request.status_code == 301:
                protocol = "https://"
            client = Client(protocol + self.SERVICE_URL)
        except:
            raise exceptions.CannotConnect("Cannot connect to the service")

        return client
