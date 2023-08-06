# -*- coding: utf-8 -*-
# Stalker a Production Asset Management System
# Copyright (C) 2009-2018 Erkan Ozgur Yilmaz
#
# This file is part of Stalker.
#
# Stalker is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Stalker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with Stalker.  If not, see <http://www.gnu.org/licenses/>

import unittest
import pytest
from sqlalchemy import Column, Integer

from stalker import ACLMixin
from stalker.db.declarative import Base


# create a new class and mix it with ACLMixin
class TestClassForACL(Base, ACLMixin):
    __tablename__ = 'TestClassForACLs'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.name = None


class ACLMixinTester(unittest.TestCase):
    """tests the stalker.models.mixins.ACLMixin class
    """

    def setUp(self):
        """setup the test
        """
        # create permissions
        from stalker import Permission
        self.test_perm1 = Permission(
            access='Allow',
            action='Create',
            class_name='Something'
        )
        self.test_instance = TestClassForACL()
        self.test_instance.name = 'Test'
        self.test_instance.permissions.append(self.test_perm1)

    def test_permission_attribute_accept_Permission_instances_only(self):
        """testing if the permissions attribute accepts only Permission
        instances
        """
        with pytest.raises(TypeError) as cm:
            self.test_instance.permissions = [234]

        assert str(cm.value) == \
               'TestClassForACL.permissions should be all instances of ' \
               'stalker.models.auth.Permission not int'

    def test_permission_attribute_is_working_properly(self):
        """testing if the permissions attribute is working properly
        """
        assert self.test_instance.permissions == [self.test_perm1]

    def test_acl_property_returns_a_list(self):
        """testing if the __acl__ property returns a list
        """
        assert isinstance(self.test_instance.__acl__, list)

    def test_acl_property_returns_a_proper_ACL_list(self):
        """testing if the __acl__ property returns a proper ACL list according
        to the given permissions
        """
        assert self.test_instance.__acl__ == \
            [('Allow', 'TestClassForACL:Test', 'Create_Something')]
