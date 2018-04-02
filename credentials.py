class Credentials:

    '''This is a class that comes up with the new instances for the credentials'''

    credentials_list = []

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    @classmethod
    def find_by_name(cls, account_name):
        '''
        a method that takes in a name and returns a credential that matches that name
        Args:
            name: account_name that has a password
        return:
            the account that matches that name
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def credential_exists(cls, account_name):
        '''
        method to check if credential exists
        Args:
            name: account_name to be searched
        boolean:
                true or false 
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return False
  
    @classmethod
    def display_credentials(cls):
        '''
        This method displays the current details
        '''
        return cls.credentials_list

    def save_credentials(self):
        '''The method that saves the credentials on the credentials list'''

        self.credentials_list.append(self)
    

    def delete_credentials(self):

        '''Method used to delete the credentials'''

        Credentials.credentials_list.remove(self)

    
