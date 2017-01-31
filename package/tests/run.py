"""
Test Runner
"""
import unittest

from package.tests.controller_tests import ControllerTests

obj_tests = [ControllerTests]

for test in obj_tests:
    test_group = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=5).run(test_group)