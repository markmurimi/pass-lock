import unittest
from credentials import Credentials

class CredentialsTest(unittest.TestCase):

    '''This is a test class that defines the credentials class test cases'''

    def setUp(self):

        '''This is the set up method that runs before each test case'''

        self.new_credentials = Credentials("Google","3344")

    def tearDown(self):
        '''
         This is the tear down method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    
    def test_display_all_credentials(self):
        '''
        Test to check if all credentials can be viewed
        '''

        self.assertEqual(Credentials.display_credentials(),
        Credentials.credentials_list)

    def test_save_credentials(self):
        
        '''Is the case to test if the credentials are being saved'''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_credentials_instance(self):
        '''Testing if credentials have correct instances'''

        self.assertEqual(self.new_credentials.account_name,"Google")
        self.assertEqual(self.new_credentials.account_password, "3344")

    def test_find_credentials_by_name(self):
        '''
        test to find out if information is displayed
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Google", "3344")
        test_credentials.save_credentials()

    def test_delete_credentials(self):
        '''The deleting test'''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Google","3344")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__=='__main__':
    unittest.main()
