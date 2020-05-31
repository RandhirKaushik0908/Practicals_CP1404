import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        source = os.getcwd() + '/' + filename
        destination = os.getcwd() + '/' + extension
        shutil.move(source, destination)
        print("{} moved to: {}/".format(extension, filename))


main()
