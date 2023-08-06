#!/usr/bin/env python
# coding: utf-8

from trivoreid.models.user import Address

class LegalInfo(object):
    '''
    The LetalInfo class that represents user's legal information.
    '''

    def __init__(self, data={}):
        '''
        Args:
            data (dict): user legal info fields
        Dictionary keys:
            'firstNames' (str)
            'lastName' (str)
            'callingName' (str)
            'email' (str)
            'phone' (str)
            'domicile' (LegalDomicile)
            'personalIdentityCode' (str)
            'protectionOrder' (boolean)
            'dateOfBirth' (str)
            'dateOfDeath' (str)
            'addresses' (list of trivoreid.models.user.Address)
            'lastUpdatedAt' (str)
            'studentInfo' (StudentInfo)
        '''

        addresses = []
        for a in data.pop('addresses', []):
            addresses.append(Address(a))

        self.firstNames = data.pop('firstNames', None)
        self.lastName = data.pop('lastName', None)
        self.callingName = data.pop('callingName', None)
        self.email = data.pop('email', None)
        self.phone = data.pop('phone', None)
        self.domicile = LegalDomicile(data.pop('domicile', {}))
        self.personalIdentityCode = data.pop('personalIdentityCode', None)
        self.protectionOrder = data.pop('protectionOrder', None)
        self.dateOfBirth = data.pop('dateOfBirth', None)
        self.dateOfDeath = data.pop('dateOfDeath', None)
        self.addresses = addresses
        self.lastUpdatedAt = data.pop('lastUpdatedAt', None)
        self.studentInfo = 	StudentInfo(data.pop('studentInfo', {}))

    def serialize(self):
        addresses = []
        for a in self.addresses:
            addresses.append(a.serialize())

        return {
            'firstNames': self.firstNames,
            'lastName': self.lastName,
            'callingName': self.callingName,
            'email': self.email,
            'phone': self.phone,
            'domicile': self.domicile.serialize(),
            'addresses': addresses,
            'studentInfo': self.studentInfo.serialize(),
            'personalIdentityCode': self.personalIdentityCode,
            'protectionOrder': self.protectionOrder,
            'dateOfBirth': self.dateOfBirth,
            'dateOfDeath': self.dateOfDeath,
            'lastUpdatedAt': self.lastUpdatedAt
        }

class LegalDomicile(object):
    '''
    LegalDomicile class that represents user's legal domicile object.
    '''
    def __init__(self, data={}):
        '''
        Args:
            data (dict): user legal domicile fields
        Dictionary keys:
            'names' (dict)
            'code' (str)
        '''

        self.names = data.pop('names', {})
        self.code = data.pop('code', None)

    def serialize(self):
        return {
            'names': self.names,
            'code': self.code
        }

class StudentInfo(object):
    '''
    StudentInfo class that represents user's student info.
    '''
    def __init__(self, data={}):
        '''
        Args:
            data (dict): user legal domicile fields
        Dictionary keys:
            'state' (StudentStatus)
            'studentValidFrom' (str)
            'studentValidTo' (str)
            'informationUpdated' (str)
            'remoteState' (str)
            'notStudentReason' (str)
            'queryConsentEnds' (str)
        '''

        self.state = data.pop('state', None)
        self.studentValidFrom = data.pop('studentValidFrom', None)
        self.studentValidTo = data.pop('studentValidTo', None)
        self.informationUpdated = data.pop('informationUpdated', None)
        self.remoteState = data.pop('remoteState', None)
        self.notStudentReason = data.pop('notStudentReason', None)
        self.queryConsentEnds = data.pop('queryConsentEnds', None)

    def serialize(self):
        return {
            'state': self.state,
            'studentValidFrom': self.studentValidFrom,
            'studentValidTo': self.studentValidTo,
            'informationUpdated': self.informationUpdated,
            'remoteState': self.remoteState,
            'notStudentReason': self.notStudentReason,
            'queryConsentEnds': self.queryConsentEnds
        }

class StudentStatus(object):
    '''
    Student statuses.
    '''
    FULL_TIME = 'FULL_TIME'
    PART_TIME = 'PART_TIME'
    NOT_STUDENT = 'NOT_STUDENT'
    FORBIDDEN = 'FORBIDDEN'
    UNKNOWN = 'UNKNOWN'
