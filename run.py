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

def main():
    print('\n')
    while True:
        print(
            "-------Welcome to my password locker app--------"
        )
        print('\n')
        print("If you dont have an acount create a new one but if you have an account proceed to login using the codes below")
        print("""Use these codes: \n "new"- create new user \n "log"-login to your account \n "ex"-to exit"""
        Code = input().lower()
        print('\n)

        if Code == 'new':
            print('*****Enter new username*****')
            new_user_name = input()

            print('*****Enter new password*****')
            new_user_password = input()

            print('*****confirm password*****')
            confirm_password = input()
            print('\n')

            while confirm_password != new_user_password:
                print("*****Password doesn't MATCH*****")
                print("*****Enter username again*****")
                new_user_password = input()
                print("*****Confirm the password*****")
                confirm_password = input()
                print('\n')
            else:
                print(
                    f"Hello {new_user_name}! Congratulations you have created yourself an account!"
                )
                print('\n')
                print("*****Now we move on to the login****")
                print('\n')
                print("*****Type in your username*****")
                typed_name = input()
                print("*****Type in the password*****")
                typed_password = input()

            while typed_name != new_user_name or typed_password != new_user_password
                print('\n')
                print("*****Password or username is wrong*****")




if__name__=='__main__':

    main()