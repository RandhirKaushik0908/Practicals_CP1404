"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('Lyrics/Christmas')
    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename
    for x, y in enumerate(new_name):
        try:
            if new_name[x].islower() and new_name[x + 1].isupper():
                new_name = new_name.replace("{}{}".format(new_name[x], new_name[x + 1]),
                                            "{}_{}".format(new_name[x], new_name[x + 1]))
            if new_name[x] == ' ':
                if new_name[x + 1].isalpha():
                    new_name = new_name.replace(" {}".format(new_name[x + 1]), "_{}".format(new_name[x + 1].title()))
                elif new_name[x + 1] == '(' and new_name[x + 2].isalpha():
                    new_name = new_name.replace(" ({}".format(new_name[x + 2]), "_({}".format(new_name[x + 2].title()))
            if new_name[x] == '.' and new_name[x + 1] == 'T' and new_name[x + 2] == 'X' and new_name[x + 3] == 'T':
                new_name = new_name.replace("{}{}{}{}".format(new_name[x], new_name[x + 1], new_name[x + 2],
                                                              new_name[x + 3]), ".txt")
            if new_name[x].isupper() and new_name[x + 1].isupper():
                new_name = new_name.replace("{}".format(new_name[x]), "{}_".format(new_name[x]))
        except IndexError:
            pass
    print(new_name)
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        # Rename the files
        for filename in filenames:
            current_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(current_name, new_name)


# main()
demo_walk()
