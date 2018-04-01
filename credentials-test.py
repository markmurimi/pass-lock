import unittest
from credentials import Credentials

class CredentialsTest(unittest.TestCase):

    '''This is a test class that defines the credentials class test cases'''

    def setUp(self):

        '''This is the set up method that runs before each test case'''

        self.new_credentials = Credentials("Google","3344")

    def test_save_credentials(self):
        
        '''Is the case to test if the credentials are being saved'''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_credentials_instance(self):
        '''Testing if credentials have correct instances'''

        self.assertEqual(self.new_credentials.account_name,"Google")
        self.assertEqual(self.new_credentials.account_password, "3344")

    def test_delete_credentials(self):
        '''The deleting test'''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Google","3344")test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__=='__main__':
    unittest.main()
