# external dependancies for main
import os
import time

# internal dependancies for main
import funcs.public_user_access as publicAccess


if __name__ == "__main__":

    invalid_uID = True
    while (invalid_uID):
        os.system('cls||clear')

        # get uID of user to copy playlists from
        user_to_copy_from = input("Enter valid user ID you would like to copy public playlists from: ")

        # ask user if they want prompting
        prompt_copy = input("Would you like to be prompted before copying a playlist? [Y/n] ")        
        prompt_before_copy = False
        if (prompt_copy.lower() == 'y'):
            prompt_before_copy = True       

        # call copy playlists with or without prompting
        check_copy_success = publicAccess.copy_playlists(user_to_copy_from, prompt_before_copy)

        # check if uID passed exists
        if (check_copy_success):
            invalid_uID = False
        else:
            print("\nPlease make sure the uID you are entering is correct...")
            print("Try again in 5 seconds...")
            [time.sleep(1) for i in range(5)]
