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


def find_credential(account_name):
    '''
    method to find a credential that has been created
    '''

    return Credentials.find_by_name(account_name)

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
        print("""Use these codes: \n "new"- create new user \n "log"-login to your account \n "ex"-to exit""")
        Code = input().lower()
        print('\n')

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

            while typed_name != new_user_name or typed_password != new_user_password:
                print('\n')
                print("*****Password or username is wrong*****")
                print("*****Username*****")
                typed_name = input()
                print("*****The password*****")
                typed_password = input()
                print('\n')

            else:
                print('\n')
                print(
                    f"***** Welcome {typed_name} to your account*****"
                )
                print('\n')

                print("Select an option to continue: \n Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1:view your credentials")
                print("2:New credentials")
                print("3:Delete credentials")
                print("4:search credentials")
                print("5:log out")
                choice = input()

                if choice == '1':
                    while True:
                        print("***** This is a list of your credentials *****")

                        if display_credential():

                            for credential in display_credential():
                                print(
                                    f"***** Account Name:{credential.account_name} *****")
                                print(
                                    f"***** Password:{credential.account_password}***** ")

                        else:

                            print('\n')
                            print("-------No credentials available------")
                            print('\n')

                        print("Back to menu? y/n")

                        back = input().lower()

                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("***** invalid option ******")
                            continue

                elif choice == '2':
                    while True:                       
                        print("-----------Enter account username-----------")
                        user_name = input()
                        print('\n')
                        print(
                                "** I can create a password for if you type in - 'gp' \n** Or create your own password with - 'yp'")
                        codeword = input().lower()

                        if codeword == 'gp':
                            user_password = random.randint(
                                11111, 111111)
                            print('\n')
                            print('This is your password')
                            print(
                                    f" ******* Account: {user_name}  *******")
                            print(
                                    f" ******* Password: {user_password}  *******")
                            print('\n')

                        elif codeword == 'yp':
                                print("Create your own password password")
                                user_password = input()
                                print(
                                    f" *******Account: {user_name} *******")
                                print(
                                    f" ******* Password: {user_password} *******")
                                print('\n')

                        else:
                                print(" ****** Enter a valid codeword *****")

                                print("Back to menu? y/n")

                                back = input().lower()

                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("***** invalid option ******")
                            continue

                elif choice == '3':
                    while True:
                        print("---- search for credential to delete ----")

                        search_name = input()

                        # if check_existing_credentials(search_name):
                        search_credential = find_credential(search_name)
                        print(
                            f"Account Name: {search_credential.account_name}\n Password: {search_credential.account_password}")
                        print("Delete? y/n")

                        confirm = input().lower()
                        if confirm == 'y':
                            delete_credential(search_credential)
                            print("----- Account successfully removed -----")
                            break
                        elif confirm == 'n':
                            continue

                    else:
                        print("** Account does not exist -----")
                        break

                elif choice == '4':
                    while True:
                        print("continue? y/n")
                        option = input().lower()
                        if option == 'y':
                            print("*****Enter account name to find credentials*****")

                            search_name = input()

                            # if check_existing_credentials(search_name):
                            search_credential = find_credential(
                                search_name)
                            print(
                                f"Account Name: {search_credential.account_name}\n Password: {search_credential.account_password}")
                            print("*****Account does not exist *****")

                        elif option == 'n':
                            break
                        else:
                            print("*****Invalid code*****")

                    print("*****Invalid code*****")
                    continue

                elif Code == 'ex':
                    break
            else:
                print("Enter valid code to continue")

        elif Code == 'lg':
            print("----- welcome -----")
            print("----- Enter user name -----")
            user_name = input()
            print('\n')

        elif choice == '5':
                    print(
                        "WARNING all your details will be lost. \n Proceed? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("-------- You have logged out successfully --------")
                        print('\n')
                        break
                    elif logout == 'n':
                        continue

if __name__=='__main__':
    main()
