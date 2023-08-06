""" Queries for writing to and getting information from the EmailAudit table in the coreapp schema """
from utils_package.data_controller.pg_util import PGUtil
from utils_package.data_controller import query_tools


class AuditWriter(object):
    """ Queries for writing to the email audit table """
    
    def __init__(self):
        """ Initialize class variables """
        self.audit_pg = PGUtil(user='app_writer', database='catan_local')

    def insert_new_record(self, rel_dict):
        """
        Inserts a new record for a first time contact
        :param rel_dict: Dictionary of all relavent information
        :return: Row count and SQL response
        """
        columns, values = query_tools.insert_string_from_dict(rel_dict)
        sql = """
        INSERT INTO coreapp.emailaudit
                    (%s)
        VALUES      (%s)
        """ % (columns, values)
        response = self.audit_pg.execute_query(sql)
        assert response[0] == 1
        assert response[1] is None
        return response


class AuditReader(object):
    """ Queries for reading from the email audit table """

    def __init__(self):
        """ Intialize class variables """
        self.audit_pg = PGUtil(user='app_reader', database='catan_local')

    def get_record_for_email(self, email_address):
        """
        Get all records of contact for a given email address
        :param email_address: Email address to to find all records for
        :return: Row count and SQL response
        """
        sql = """
        SELECT *
        FROM   coreapp.emailaudit
        WHERE  stremailaddress = '%s'  
        """ % email_address
        response = self.audit_pg.execute_query(sql)
        return response
