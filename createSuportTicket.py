import os
import argparse
import sys
import time
from shutil import copy, move

dl_path = 'C:\\Users\\noamha\\Desktop\\Tickets\\'
dl_currentlogs = 'current_logs'
is_debug = False


def cmd_variables():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--ticket', nargs='*', help='Ticket number', dest='ticket')
    parser.add_argument('-s', '--search', nargs='*', help='Search error token', dest='search')
    parser.add_argument('--debug', help='Print debug messages'
                        , action='store_true', dest='debug', default=False)

    if len(sys.argv) == 2 and not sys.argv[1] == "--help":
        args = argparse.Namespace()
        x = []
        x.append(sys.argv[1])
        args.debug = is_debug
        args.ticket = x
        return args

    elif len(sys.argv) > 2:
        args = parser.parse_args()
        if not args.ticket:
            parser.print_help()
            parser.error('--match is empty')
    else:
        args = parser.parse_args()

    return args


def get_os_path():
    if osdetails.get_os_name() == "windows":
        return "\\"
    else:
        return "/"


def print_debug(action='INFO', message=''):
    global is_debug
    new_message = ''
    if type(message) is list:
        for i in message:
            if new_message == '':
                new_message += i
            else:
                new_message += ',' + i

    if is_debug and message:
        print(action, ': ', new_message)
    elif is_debug and not message:
        print(action)


def main():
    global is_debug
    args = cmd_variables()
    is_debug = args.debug

    args.ticket = input('Enter ticket number --> ').split(" ")
    args.search = input('Enter error expression --> ').split(" ")

    for ticket_name in args.ticket:
        if not os.path.exists(dl_path + ticket_name):
            os.makedirs(dl_path + ticket_name)
            if not os.path.exists(dl_path + ticket_name):
                print_debug("Failure!!!")
            else:
                print(dl_path + ticket_name, " was created successfully")
        else:
            print(dl_path + ticket_name, " already exists")
    time.sleep(3)
    copy(dl_path + "actimize_support_extract_and_search_err.bat",
         dl_path + ticket_name + "\\" + "actimize_extract_and_search_err_all.bat")
    print(dl_path + ticket_name)

    files = os.listdir(dl_path + dl_currentlogs)
    for f in files:
        move(dl_path + dl_currentlogs + "\\" + f, dl_path + ticket_name )
        print("Copy - " + dl_path + dl_currentlogs + f + " to " + dl_path + "\\" + ticket_name )

    if args.search:
        for search in args.search:
            print("Search for : ", search)
            with open(dl_path + ticket_name + "\\" + "actimize_extract_and_search_err_" + search + ".bat", "a") as file:
                    try:
                        file.write(r"python C:\Users\noamha\PycharmProjects\actimize_verification_tool\checkOS"
                                   r"\checkOS\errorsearch.py -m " + search)
                    except (IOError, OSError) as e:
                        print("Error writing line.")
    print("Finished!!!");
    time.sleep(3)

    return


if __name__ == '__main__':
    main()
