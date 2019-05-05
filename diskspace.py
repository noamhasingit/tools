from shutil import disk_usage
import sys
import osdetails
import print_nice

os_path = "/"


def cmd_variables():
    if len(sys.argv) == 1:
       # print("Checking disk space for ", osdetails.get_os_name(), " root drive: ", os_path)
        return 0
    else:
       # print("Checking  disk space for ", sys.argv[1])
        return 1


def get_os_path():
    if osdetails.get_os_name() == "windows":
        return "\\"
    else:
        return "/"


def print_usage(mypath):

    total, used, free = disk_usage(mypath)

    print_nice.print_nice("", "Disk Space")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))


# stuff to run always here such as class/def
def main():
    try:
        if cmd_variables() == 1:
            os_path = sys.argv[1]
        else:
            os_path = get_os_path()
        print_usage(os_path)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()

