class User:
    '''This class generates a new user to the user_list'''
    
    user_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''This method saves the user details to the user_list'''

        User.user_list.append(self)