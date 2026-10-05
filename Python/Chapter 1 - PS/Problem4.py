import os

def list_directory_contents(path):
    """
    Prints the contents of the specified directory using os.listdir().
    """
    try:
        # Check if the path exists first
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return

        # os.listdir() returns a list of filenames and directory names
        contents = os.listdir(path)

        print(f"Contents of '{path}':")
        print("-" * 30)
        
        if not contents:
            print("The directory is empty.")
        else:
            for item in contents:
                print(item)

    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # You can change '.' to any specific path you want to list
    # '.' represents the current working directory
    target_directory = "/YASH EVERYTHING FOLDER" 
    list_directory_contents(target_directory)