# external dependancies for main
import os
import time

# internal dependancies for main
import funcs.public_user_access as publicAccess


if __name__ == "__main__":

    invalid_uID = True
    while (invalid_uID):
        os.system('cls||clear')

        user_to_copy_from = input("Enter valid user ID you would like to copy public playlists from: ")
        check_copy_success = publicAccess.copy_playlists(user_to_copy_from)
        if (check_copy_success):
            invalid_uID = False
        else:
            print("\nPlease make sure the uID you are entering is correct...")
            print("Try again in 5 seconds...")
            [time.sleep(1) for i in range(5)]

