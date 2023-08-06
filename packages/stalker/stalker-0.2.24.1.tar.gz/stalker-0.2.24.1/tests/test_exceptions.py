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


class ExceptionTester(unittest.TestCase):
    """testing exceptions
    """

    def test_login_error_is_working_properly(self):
        """testing if LoginError is working properly
        """
        from stalker.exceptions import LoginError
        test_message = 'testing LoginError'
        with pytest.raises(LoginError) as cm:
            raise LoginError(test_message)

        assert str(cm.value) == test_message

    def test_circular_dependency_error_is_working_properly(self):
        """testing if CircularDependencyError is working properly
        """
        from stalker.exceptions import CircularDependencyError
        test_message = 'testing CircularDependencyError'
        with pytest.raises(CircularDependencyError) as cm:
            raise CircularDependencyError(test_message)

        assert str(cm.value) == test_message

    def test_over_booked_error_is_working_properly(self):
        """testing if OverBookedError is working properly
        """
        from stalker.exceptions import OverBookedError
        test_message = 'testing OverBookedError'
        with pytest.raises(OverBookedError) as cm:
            raise OverBookedError(test_message)

        assert str(cm.value) ==test_message

    def test_status_error_is_working_properly(self):
        """testing if StatusError is working properly
        """
        from stalker.exceptions import StatusError
        test_message = 'testing StatusError'
        with pytest.raises(StatusError) as cm:
            raise StatusError(test_message)

        assert str(cm.value) == test_message

    def test_dependency_violation_error_is_working_properly(self):
        """testing if DependencyViolationError is working properly
        """
        from stalker.exceptions import DependencyViolationError
        test_message = 'testing DependencyViolationError'
        with pytest.raises(DependencyViolationError) as cm:
            raise DependencyViolationError(test_message)

        assert str(cm.value) ==test_message
