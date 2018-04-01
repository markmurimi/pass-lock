import unittest
from user import User

class TestUser (unittest.TestCase):
    '''
    Class for testing the behaviours

    Args:
        unnitest.TestCase :Test case that assist in the creation.
    '''

    def setUp(self):

        '''
        The method above was or is supposed to run before each test case
        '''
        self.new_user = User("mark","password")


    def test_save_user(self):
        '''This test case is used to check if the user saves data properly'''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_init_(self):

        '''
        Test case used to check if user is initialised properly
        '''
        self.assertEqual(self.new_user.user_name, "mark")
        self.assertEqual(self.new_user.password, "password")

    
if __name__=='__main__':
    unittest.main()
