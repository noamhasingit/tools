#!/usr/bin/env python3

import re
import random

import findfile
from os import getenv, getcwd
import argparse
import sys

try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

exact_match = ['ERROR', 'FAILED', 'EXCEPTION', 'CAUSED BY']
max_lines_per_file_cons = 65000
is_debug = False
results_prefix = ["Transmit_support_parser_"]

def print_debug(action, message = ''):

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


def cmd_variables():

    parser = argparse.ArgumentParser()
    parser.add_argument('-ext', '--extension', nargs='*', help='Parse files with the following extensions'
                        , dest='extension', default=False)
    parser.add_argument('-all', '--findall', help='Search in all files'
                        , action='store_true', dest = 'findall', default=True)
    parser.add_argument('-p', '--path', nargs='*', help='Full path to search', dest='path',
                        default=[getcwd()])

    parser.add_argument('-m', '--match', nargs='*', help='Fine a match', default=exact_match)
    parser.add_argument('-c', '--countline',  help='Limit number of matches per file for each pattern.',
                        type=int, default=max_lines_per_file_cons)
    parser.add_argument('-rl', '--read_line', help='Match for each line'
                        , action='store_true', dest='read_line', default=True)
    parser.add_argument('-uz', '--unzip', help='Unzip all files'
                        , action='store_true', dest='unzip', default=True)

    parser.add_argument('--print', help='Match for each line'
                        , action='store_true', dest='printx', default=False)
    parser.add_argument('--debug', help='Print debug messages'
                        , action='store_true', dest='debug', default=False)


    if len(sys.argv) == 2 and not sys.argv[1] == "--help":
        args = argparse.Namespace()
        x=[]
        x.append(sys.argv[1])
        args.path = x
        args.match = exact_match
        args.debug = is_debug
        args.printx = False
        args.extension = False
        args.findall = True
        args.read_line = True
        args.countline = max_lines_per_file_cons
        args.unzip = True
        return args
    elif len(sys.argv) > 2:
        args = parser.parse_args()
        if not args.match:
            parser.print_help()
            parser.error('--match is empty')
    else:
        args = parser.parse_args()
        parser.print_help()

    return args


def build_dict_match_count(exactmatch):
    dict_match_count = {}
    for err_i in exactmatch:
        dict_match_count[err_i] = 0
    return dict_match_count


def build_dict_regex(exactmatch, left, right):
    dict_regex = {}
    for err_i in exactmatch:
        dict_regex[err_i] = left + err_i + right

    return dict_regex


def parse_files(files, regex, parse_each_line=True, count_per_file=max_lines_per_file_cons):

    if not files:
        print("Missing input files")
        exit(1)
    pattern_cnt = 0
    current_dict = {}
    p = re.compile(regex, flags=re.IGNORECASE)

    if parse_each_line:
        for name in files:
            pattern_per_file = 0
            line_cnt = 0
            try:
                with open(name, "r", encoding="utf8") as file_name:
                    for line in file_name:
                        line_cnt = line_cnt + 1
#                       print (line_cnt, line)
                        if line_cnt == 476:
                            match = p.match(line)
                            print (name,regex,match)
#                           exit ()
                        match = p.match(line)
                        if match:
                            match_text = match.group()
                            pattern_cnt = pattern_cnt + 1
                            pattern_per_file = pattern_per_file + 1
                            current_dict[pattern_cnt] = (name, line_cnt, match_text)
                            if pattern_per_file >= count_per_file:
                                break
                file_name.close()
            except (TypeError, ValueError):
                try:
                    with open(name, "r") as file_name:
                        for line in file_name:
                            line_cnt = line_cnt + 1
                            match = p.match(line)
                            if match:
                                match_text = match.group()
                                pattern_cnt = pattern_cnt + 1
                                pattern_per_file = pattern_per_file + 1
                                current_dict[pattern_cnt] = (name, line_cnt, match_text)
                                if pattern_per_file >= count_per_file:
                                    break
                    file_name.close()
                except (TypeError, ValueError):
                    print_debug(name + " --> Not ASCII or UTF8 - is also a superclass of io.UnsupportedOperation")
                    print ("Error: Fail to read file:  ", name)
    return current_dict


def print_result(logs, err, res):

    global results_prefix
    print ("Found ", len(res), " lines for ", err, " pattern.")
    for name in logs:
        print (name + "/" + results_prefix[0] + err)
        try:
            with open(name + "/" + results_prefix[0] + err + '.txt', "w+") as file:
                for ent in res.values():
                    try:
                        file.write("[" + ent[0] + "," + str(ent[1]) + "] - " + ent[2] + "\n")
                    except (TypeError, ValueError) as e:
                        print("Error in line: ", "[" + ent[0] + "," + str(ent[1]) + "]", " for - ", ent[2] )
        except (IOError, OSError):
            print ("New Name: ", name + "/" + results_prefix[0] +  random.randint(0, 10000) + '.txt')
            with open(name + "/" + results_prefix[0] + random.randint(0, 10000) + '.txt', "w+") as file:
                print("Saving file in: ", name + "/" + results_prefix[0], random.randint(0, 10000))
                for ent in res.values():
                    try:
                        file.write("[" + ent[0] + "," + str(ent[1]) + "] - " + ent[2] + "\n")
                    except (TypeError, ValueError) as e:
                        print("Error in line: ", "[" + ent[0] + "," + str(ent[1]) + "]", " for - ", ent[2] )

def run():

    global is_debug
    print("Current path:", getcwd())
    args = cmd_variables()
    is_debug = args.debug

    if args.unzip:

        zipped_files = findfile.find_files_by_type(args.path, findfile.get_zip_types(), results_prefix)
        findfile.unzip_files(zipped_files, False, results_prefix)

    if args.match:

        dict_count = build_dict_match_count(args.match)
        dict_regex = build_dict_regex(args.match, left='.*(', right=').*')

    if args.extension and args.findall:
        print_debug("Looking for ", args.extension)
        files = findfile.find_files_by_type(args.path, args.extension, results_prefix)
    elif args.findall:
        print_debug("Look for All")
        files = findfile.find_files_by_type(args.path, "*", results_prefix)
    else:
        print_debug("Look for all")
        files = findfile.find_files_by_type(args.path, "*", results_prefix)

    print (files)
    for err1, err in dict_regex.items():
        if args.printx:
            print("Search for: ", err)
        res = parse_files(files, err, parse_each_line=args.read_line, count_per_file=args.countline)
        print_result(args.path, err1, res)
        if args.printx:
            print(res)


# stuff to run always here such as class/def
def main():
    run()

if __name__ == "__main__":
    main()
