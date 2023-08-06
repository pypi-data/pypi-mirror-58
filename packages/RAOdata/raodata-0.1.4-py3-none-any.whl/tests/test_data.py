import pytest
import types

from raodata import exceptions
from raodata.Data import Data
from zeep import Client

class TestData:

    def test_connection_exception_exception(self):
        Data.SERVICE_URL = "localhost"
        with pytest.raises(exceptions.CannotConnect) as excinfo:
            Data().get_instruments()

        Data.SERVICE_URL = "127.0.0.1"
        with pytest.raises(exceptions.CannotConnect) as excinfo:
            Data().get_instruments()

        Data.SERVICE_URL = "data.rao.istp.ac.ru/test.wsdl"
        with pytest.raises(exceptions.CannotConnect) as excinfo:
            Data().get_instruments()

        Data.SERVICE_URL = "data.rao.istp.ac.ru/Access.wsdl"


    def test_check_arguments(self):
        assert Data()._check_arguments("SRH", "fits", "2019-08-08", "") == True
        assert Data()._check_arguments("SRH", "fits", "2019-08-08", "2019-08-08") == True
        assert Data()._check_arguments("SRH", "fits", "2019-08-08T20:11:11", "2019-08-08") == True
        assert Data()._check_arguments("SRH", "fits", "2019-08-08T20:11:11", "2019-08-08T20:11:11") == True
        assert Data()._check_arguments("SRH", "fits", "2019-08-08", "2019-08-08T20:11:11") == True


    def test_check_arguments_exceptions(self):

        with pytest.raises(exceptions.InstrumentNotString) as excinfo:
            Data()._check_arguments(1, "fits", "2019-08-08", "2019-08-08")

        with pytest.raises(exceptions.FiletypeNotString) as excinfo:
            Data()._check_arguments("SRH", 1, "2019-08-08", "2019-08-08")

        with pytest.raises(exceptions.InvalidDate) as excinfo:
            Data()._check_arguments("SRH", "fits", "D", "2019-08-08")

        with pytest.raises(exceptions.InvalidDate) as excinfo:
            Data()._check_arguments("SRH", "fits", "2019-08-08", "D")


    def test_get_instruments(self):

        instruments = Data().get_instruments()
        for instrument in instruments:
            assert type(instrument) is str


    def test_get_file_types(self):

        instruments = Data().get_instruments()
        for instrument in instruments:
            types = Data().get_file_types(instrument)
            for tp in types:
                assert type(tp) is str


    def test_get_types_by_instruments(self):

        instruments = Data().get_types_by_instruments()
        for instrument in instruments:
            assert type(instrument["instrument"]) is str
            for tp in instrument["types"]["type"]:
                assert type(tp) is str


    def test_get_files(self):

        files = Data().get_files("SRH", "cp", "2019-08-08")
        assert isinstance(files, types.GeneratorType) == True
        list(files)


    def test_get_files_exceotion(self):

#if you dont try get files. it is not returned exception
        with pytest.raises(exceptions.NoDataDuringThisPeriod) as excinfo:
            files = Data().get_files("SRH", "cp", "2019-08-08T11:11:11")
            list(files)
