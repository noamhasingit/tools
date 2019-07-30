#!/usr/bin/env python3
from os import walk, path, getenv, remove
from shutil import move
from fnmatch import fnmatch
import print_nice
import argparse
import zipfile
import tarfile
import rarfile

log_types = ['log', 'xml', 'config', 'conf']
zip_types = ['zip', 'tar.gz', 'tar', '7z', 'rar']

def cmd_variables():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log', nargs='*', help='Parse only logs', default=["/home",
                                                                                   getenv('USERPROFILE') + "/"])
    parser.add_argument('-skipl', '--skip_logs', help='Skip logs', action='store_true'
                        , dest='skip_logs', default=False)
    parser.add_argument('-uz', '--unzip', help='Unzip files before searching', action='store_true'
                        , dest='unzip', default=False)
    parser.add_argument('-uzd', '--unzip_del', help='Unzip files before searching and delete zipped files'
                        , action='store_true', dest='unzip_del', default=False)
    parser.add_argument('-sn', '--scan_number', nargs='?', help='Unzip X times',
                        type=int, default=1)
    parser.add_argument('-all', '--findall', nargs='*', help='Search in all files',
                        default=["/home", getenv('USERPROFILE') + "/"])

    args = parser.parse_args()
    return args


def find(pattern, my_path, ignore_list=[]):
    result = []
    global skip_to_next
    for root, dirs, files in walk(my_path):
        for name in files:

            skip_to_next = False
            if len(ignore_list) > 0:
                for ignore_pattern in ignore_list:
                    if fnmatch(name, ignore_pattern + "*"):
                        #print("Found actimize file , skipping ", name)
                        skip_to_next = True
                        break
            else:
                skip_to_next = False
            if skip_to_next is False and fnmatch(name, pattern):
                result.append(path.join(root, name))
    return result


def find_files_by_type(directories, files_type=log_types[0], ignore_list=[]):

    if type(files_type) is str:
        try:
            for next_dir in directories:

                if not path.exists(next_dir):
                    print(next_dir, " does not exist skip to the next dir.")
                    continue
                print("Search for " + next_dir + ".*" + files_type, " files")
                result = find('*.' + files_type, next_dir, ignore_list)
                return result

        except Exception as e:
            print(str(e))
    elif type(files_type) is list:
        try:
            for next_dir in directories:
                if not path.exists(next_dir):
                    print(next_dir, " does not exist skip to the next dir.")
                    continue
                print('Search for [%s]' % ', '.join(map(str, files_type)) , " in ", next_dir)
                result = []
                for next_type in files_type:
                    result.extend(find('*.' + next_type, next_dir, ignore_list))
                return result

        except Exception as e:
            print(str(e))



def return_output_path(file_name):

    parent_path = path.split(file_name)[0]
    output_folder_name = path.splitext(file_name)[0]
    output_path = path.join(parent_path, output_folder_name)
    return output_path

def get_zip_types():
    return zip_types



def unzip_files(files, removefile=False, new_name=''):

    if not files:
        print("Zip files were not found.")
        return

    for file in files:

        if file.endswith("tar.gz"):
            try:
                tar = tarfile.open(file, "r:gz")
                tar.extractall(return_output_path(file))
                tar.close()
            except Exception as e:
                print(str(e))
                continue
        elif file.endswith("rar"):
            try:
                tar = rarfile.RarFile(file)
                tar.extractall(return_output_path(file))
                tar.close()
            except Exception as e:
                print(str(e))
                continue
        elif file.endswith("tar"):
            try:
                tar = tarfile.open(file, "r:")
                tar.extractall(return_output_path(file))
                tar.close()
            except Exception as e:
                print(str(e))
                continue
        elif file.endswith("zip"):
            try:
                zip_ref = zipfile.ZipFile(file)  # create zipfile object
                zip_ref.extractall(return_output_path(file))  # extract file to dir
                zip_ref.close()  # close file
            except Exception as e:
                print(str(e))
                continue
        elif file.endswith("7z"):
            try:
                print ("Error: Is not supported")
            except Exception as e:
                print(str(e))
                continue

        if removefile:
            try:
                remove(file)  # delete zipped file
            except Exception as e:
                print(str(e))

        if new_name != '':
            s_file = file[:file.rfind("/") + 1]
            e_file = file[file.rfind("/") + 1:]
            move(file, s_file + new_name[0] + e_file)
            print ("Backup zip: ", s_file + new_name[0] + e_file)


def unzip_files_and_clean(files):
    unzip_files(files, removefile=True)


def run():


    args = cmd_variables()


    for i in range(args.scan_number):

        if args.scan_number > 1:
            print_nice.print_nice("", str(i + 1))

        if args.unzip:
            for zip_type in zip_types:
                zipped_files = find_files_by_type(args.log, zip_type)
                print ("ZIP: ", zipped_files)
                print("Found :", len(zipped_files), " ", zip_type, " files")
                unzip_files(zipped_files)

        if args.unzip_del:
            for zip_type in zip_types:
                zipped_files = find_files_by_type(args.log, zip_type)
                print("Found :", len(zipped_files), " ", zip_type, " files")
                unzip_files_and_clean (zipped_files)

        if args.log and not args.skip_logs:
            res = find_files_by_type(args.log, log_types[0])
            print("Found :", len(res), " logs files")

        if args.findall and not args.skip_logs:
            res = find_files_by_type(args.log, "*")
            print("Found :", len(res), " files")

# stuff to run always here such as class/def
def main():
    run()


if __name__ == "__main__":
    main()

