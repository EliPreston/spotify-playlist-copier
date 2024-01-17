# external dependancies for main
import os
import time

# internal dependancies for main
import funcs.public_user_access as publicAccess


if __name__ == "__main__":

    invalid_uID = True
    while (invalid_uID):
        os.system('cls||clear')

        # in the future change this to search for the playlist, select it, and download it??
        # if user wants to copy a single playlist they know the id and name of
        single_or_multi = input("Do you want to copy a single playlist rather than (potentially) all? [Y/n] ")
        if (single_or_multi.lower() == 'y'):
            pName = input("Enter playlist name: ")
            pID = input("Enter playlist ID: ")
            publicAccess.copy_single_playlist(pName, pID)
        
        
        else:
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
