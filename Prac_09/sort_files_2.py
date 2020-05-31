import os
import shutil


def main():
    extension_to_directory = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        if extension not in extension_to_directory:
            directory = input("What category of directory would you like to sort {} files into? ".format(extension))
            extension_to_directory[extension] = directory
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass

        source = os.getcwd() + '/' + filename
        destination = os.getcwd() + '/' + extension_to_directory[extension]
        shutil.move(source, destination)
        print("{} moved to: {}/".format(filename, extension_to_directory[extension]))


main()

