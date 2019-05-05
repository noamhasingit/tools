import re
import random

import findfile
from os import getenv
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
results_prefix = ["actimize_support_parser_"]

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

def run():
    #p = re.compile('@(P\d+) (\D+\(\d+\)[,]||@(P\d+) (\D+[,]))|@(P\d+) (\D+\d+,)', flags=re.IGNORECASE)
    p1 = re.compile("@(P\d+) (\D+\(\d+\))[,]", flags=re.IGNORECASE)
    p2 = re.compile("@(P\d+) (\D+\d+[,]\d+\))", flags=re.IGNORECASE)
    p3 = re.compile("@(P\d+) (\D+)[,]", flags=re.IGNORECASE)
    p4 = re.compile("(P\d+) (\D+\d+)[,][^\d]", flags=re.IGNORECASE)
    line_cnt = 0
    current_dict = {}
    with open(r'C:\Users\noamha\Desktop\ilsqlperfdb\ilsqlperfdb.txt', "r", encoding="utf8") as file_name:
        for line in file_name:
            line_cnt = line_cnt + 1
            match = p1.findall(line)

            if match:
                for k in match:
                    if current_dict.get(k[0], 0) == 0:
                        current_dict[k[0]] = dict({k[1]: 1})
                    elif current_dict.get(k[0]).get(k[1], 0) == 0:
                        print ("FOUND DYNAMIC VAR ", k[0], k[1])
                        current_dict[k[0]][k[1]] = 1
                    else:
                        add_cnt = current_dict.get(k[0]).get(k[1], 0)
                        current_dict[k[0]][k[1]] = add_cnt + 1
    line_cnt = 0
    with open(r'C:\Users\noamha\Desktop\ilsqlperfdb\ilsqlperfdb.txt', "r", encoding="utf8") as file_name:
        for line in file_name:
            line_cnt = line_cnt + 1
            match = p2.findall(line)

            if match:
                for k in match:
                    if current_dict.get(k[0], 0) == 0:
                        current_dict[k[0]] = dict({k[1]: 1})
                    elif current_dict.get(k[0]).get(k[1], 0) == 0:
                        print ("FOUND DYNAMIC VAR ", k[0], k[1])
                        current_dict[k[0]][k[1]] = 1
                    else:
                        add_cnt = current_dict.get(k[0]).get(k[1], 0)
                        current_dict[k[0]][k[1]] = add_cnt + 1
        file_name.close()
    line_cnt = 0
    with open(r'C:\Users\noamha\Desktop\ilsqlperfdb\ilsqlperfdb.txt', "r", encoding="utf8") as file_name:
        for line in file_name:
            line_cnt = line_cnt + 1
            match = p3.findall(line)

            if match:
                for k in match:
                    if current_dict.get(k[0], 0) == 0:
                        current_dict[k[0]] = dict({k[1]: 1})
                    elif current_dict.get(k[0]).get(k[1], 0) == 0:
                        print ("FOUND DYNAMIC VAR ", k[0], k[1])
                        current_dict[k[0]][k[1]] = 1
                    else:
                        add_cnt = current_dict.get(k[0]).get(k[1], 0)
                        current_dict[k[0]][k[1]] = add_cnt + 1
        file_name.close()
        line_cnt = 0
        with open(r'C:\Users\noamha\Desktop\ilsqlperfdb\ilsqlperfdb.txt', "r", encoding="utf8") as file_name:
            for line in file_name:
                line_cnt = line_cnt + 1
                match = p4.findall(line)
                if match:
                    for k in match:
                        if current_dict.get(k[0], 0) == 0:
                            print("CATCH",k[0])
                            current_dict[k[0]] = dict({k[1]: 1})
                        elif current_dict.get(k[0]).get(k[1], 0) == 0:
                            for i in range(0, 5):
                                print("FOUND DYNAMIC VAR ", k[0], k[1])
                            current_dict[k[0]][k[1]] = 1
                        else:
                            add_cnt = current_dict.get(k[0]).get(k[1], 0)
                            current_dict[k[0]][k[1]] = add_cnt + 1
        for p_dist in current_dict:
            if len(current_dict[p_dist]) > 1:
                print(p_dist,current_dict[p_dist])

        print ("Expected bindings: 940 and got: ", len(current_dict))
        for i in range(1,940):
            if current_dict.get(("P" + str(i)),0) == 0:
                print ("Missing: ",i)

    file_name.close()



# stuff to run always here such as class/def
def main():
    run()


if __name__ == "__main__":
    main()

