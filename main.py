# external dependancies for main
# N/A

# internal dependancies for main
import funcs.public_user_access as publicAccess


if __name__ == "__main__":

    user_to_copy = input("Enter valid user ID you would like to copy public playlists from: ")
    publicAccess.copy_playlists(user_to_copy)

    

# c7esmmjgqo900ub3152g77ymk