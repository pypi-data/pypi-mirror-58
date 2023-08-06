""" Unit tests for email audit queries """
from utils_package.data_controller.scripts.email_controller.email_audit_queries import AuditReader, AuditWriter
from unittest import TestCase
import random


class TestEmailAuditQueries(TestCase):
    """ Unit tests for audit queries """

    def setUp(self):
        """ Set up class variables """
        self.audit_writer = AuditWriter()
        self.audit_reader = AuditReader()

    def test_create_new_record_and_retrieve(self):
        """ Validates that a new record is created appropriately
        1. Generate test data
        2. Generate new record in the database
        3. Build request to get records
        4. Validate data back is correct
        """
        # 1. Generate test data
        record_dict = {
            'strname': 'John Dave Franklin',
            'stremailaddress': 'test_email_%s@test.com' % str(random.randint(000, 999)),
            'strmessage': 'This is a test message'
        }

        # 2. Generate new record in the database
        response = self.audit_writer.insert_new_record(record_dict)
        self.assertIsNotNone(response)

        # 3. Build request to get records
        response = self.audit_reader.get_record_for_email(record_dict['stremailaddress'])[1]
        self.assertEqual(record_dict['stremailaddress'], response[0]['stremailaddress'])
