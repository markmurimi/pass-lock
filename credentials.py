class Credentials:

    '''This is a class that comes up with the new instances for the credentials'''

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    def delete_credentials(self):

        '''Method used to delete the credentials'''

        Credentials.credentials_list.remove(self)

    def save_credentials(self):

        '''The method that saves the credentials on the credentials list'''

        self.credentials_list.append(self)
    credentials_list = []