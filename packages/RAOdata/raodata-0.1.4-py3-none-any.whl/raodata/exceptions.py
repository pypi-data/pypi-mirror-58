#!/usr/bin/env python3
'''RAO data exceptions'''


class CannotConnect(Exception):
    '''
    Connect to SOAP server
    '''
    code = "CANNOTCONNECT"


class CannotParseArguments(Exception):
    '''
    Parsing input arguments
    '''
    code = "CANNOTPARSEARGUMENTS"


class InstrumentNotString(Exception):
    '''
    Argument 'Instrument' is not string
    '''
    code = "INSTUMENTNOTSTRING"


class FiletypeNotString(Exception):
    '''
    Argument 'Filetype' is not string
    '''
    code = "FILETYPENOTSTRING"


class InvalidDate(Exception):
    '''
    Argument 'Date' is invalid
    '''
    code = "INVALIDDATE"


class CannotDownloadFile(Exception):
    '''
    Error while downloading files
    '''
    code = "CANNOTDOWNLOADFILE"


class InvalidFileHash(Exception):
    '''
    Downloaded file has invalid hash
    '''
    code = "INVALIDFILEHASH"


class InvalidInstrumentOrType(Exception):
    '''
    Arguments "Instrument" or "Filetype" are invalid
    '''
    code = "INVALIDINSTUMENTORTYPE"


class CannotCreateDirectory(Exception):
    '''
    Error while creating directory
    '''
    code = "CANNOTCREATEDIRECTORY"


class NoDataDuringThisPeriod(Exception):
    '''
    Empty files during given period
    '''
    code = "NODATADURINTHISPERIOD"
