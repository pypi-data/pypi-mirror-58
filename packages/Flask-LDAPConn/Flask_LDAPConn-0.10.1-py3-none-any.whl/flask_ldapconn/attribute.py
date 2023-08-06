# -*- coding: utf-8 -*-

from flask import current_app

from ldap3 import AttrDef
from ldap3.core.exceptions import LDAPAttributeError
from ldap3 import (STRING_TYPES, NUMERIC_TYPES, MODIFY_ADD, MODIFY_DELETE,
                   MODIFY_REPLACE)


class LdapField(object):

    def __init__(self, name, validate=None, default=None, dereference_dn=None):
        self.name = name
        self.validate = validate
        self.default = default
        self.dereference_dn = None

    def get_abstract_attr_def(self, key):
        return AttrDef(name=self.name, key=key,
                       validate=self.validate,
                       default=self.default,
                       dereference_dn=self.dereference_dn)


class LDAPAttribute(object):

    def __init__(self, name):
        self.__dict__['name'] = name
        self.__dict__['values'] = []
        self.__dict__['changetype'] = None

    def __str__(self):
        if isinstance(self.value, STRING_TYPES):
            return self.value
        else:
            return str(self.value)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self.values.__iter__()

    def __contains__(self, item):
        return item in self.__dict__['values']

    def __setattr__(self, item, value):
        if item not in ['value', '_init']:
            raise LDAPAttributeError('can not set key')

        # set changetype
        if item == 'value':
            if self.__dict__['values']:
                if not value:
                    self.__dict__['changetype'] = MODIFY_DELETE
                else:
                    self.__dict__['changetype'] = MODIFY_REPLACE
            else:
                self.__dict__['changetype'] = MODIFY_ADD

        if isinstance(value, (STRING_TYPES, NUMERIC_TYPES)):
            value = [value]

        self.__dict__['values'] = value

    @property
    def value(self):
        '''Return single value or list of values from the attribute.
           If FORCE_ATTRIBUTE_VALUE_AS_LIST is True, always return a
           list with values.
        '''
        if len(self.__dict__['values']) == 1 and current_app.config['FORCE_ATTRIBUTE_VALUE_AS_LIST'] is False:
            return self.__dict__['values'][0]
        else:
            return self.__dict__['values']

    @property
    def changetype(self):
        return self.__dict__['changetype']

    def get_changes_tuple(self):
        values = [val.encode('UTF-8') for val in self.__dict__['values']]
        return (self.changetype, values)

    def append(self, value):
        '''Add another value to the attribute'''
        if self.__dict__['values']:
            self.__dict__['changetype'] = MODIFY_REPLACE

        self.__dict__['values'].append(value)

    def delete(self):
        '''Delete this attribute

        This property sets the value to an empty list an the changetype
        to delete.
        '''
        self.value = []
