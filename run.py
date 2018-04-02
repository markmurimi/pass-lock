#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials


def create_new_credential(account_name, account_password):
    '''
     The method that creates  new  account name.
    '''
    new_credential = Credentials(account_name, account_password)

    return new_credential


def delete_credential(credentials):
    '''
    method to delete a credential that has been created
    '''

    return Credentials.delete_credentials(credentials)
    
def save_new_credential(credentials):
    '''
    method to save new credentials
    '''

    credentials.save_credentials()


def display_credential():
    '''
    THis method displays credentials.
    '''
    return Credentials.display_credentials()
