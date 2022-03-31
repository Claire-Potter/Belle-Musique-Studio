"""
Django validate templates test
"""
import unittest
from django.core.management import call_command


class MyTests(unittest.TestCase):
    """
    Django validate templates test
    """
    def test_validate_templates(self):
        """
        Django validate templates test
        """
        call_command('validate_templates')
        # This throws an error if it fails to validate
