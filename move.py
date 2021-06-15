"""
    This script will copy all media files ('.jpg', '.png', '.gif', '.mp4', '.mov', '.m4v', '.avi', '.3gp', '.jpeg', '.heic', '.webp', '.mkv') 
    from one folder with sub dirs to a single folder

    I used this for googles "takeout system" because they are jackasses and put everything in sorted order ;)

    When I find the need to do so I will implement a multi threading version of this script
"""

import os
import pathlib
import shutil
import time

def check_if_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    else:
        print(f"'{dir}' Already exists")

def get_valid_name(dir, file):
    split_fn = os.path.splitext(file)
    tmp_name = split_fn[0] + split_fn[1]

    count = 1

    while os.path.isfile(os.path.join(dir, tmp_name)):
        tmp_name = split_fn[0] + " (" + str(count) + ")" + split_fn[1]
        count += 1

    return tmp_name


def copy_all_files(files, from_dir, to_dir):
    copied_count = 0
    for file in files:
        copied = copy_file(file, from_dir, to_dir)

        if copied:
            copied_count += 1

    return copied_count

def copy_file(file, from_dir, to_dir):
    fileExt = ['.jpg', '.png', '.gif', '.mp4', '.mov', '.m4v', '.avi', '.3gp', '.jpeg', '.heic', '.webp', '.mkv']

    filename = file.lower()
    file_extension = pathlib.Path(filename).suffix
    
    if file_extension in fileExt:
        # adding exception handling
        try:
            new_file_name = get_valid_name(to_dir, file)

            f = os.path.join(from_dir, file)
            t = os.path.join(to_dir, new_file_name)

            shutil.copy2(f, t)

            return True
        except IOError as e:
            print(f"Unable to copy. {e}")
            return False
    else: 
        return False

def main():

    # Change dirs to whatever you want to
    root_dir = 'D:/Dropbox/Sociala medier Takeout 061219'
    target_dir = 'D:/outDirTwo'

    check_if_dir(target_dir)    
    copied_total = 0
    for subdir, dirs, files in os.walk(root_dir):
        copied_total += copy_all_files(files, subdir, target_dir)

        # Om jag orkar hålla på med threading
        # thread.start_new_thread(handle_dir_files, (files, subdir, outputDir,  ))

    time.sleep(5)
    print(f"Done copying {copied_total} files!")

if __name__ == '__main__':
    main()