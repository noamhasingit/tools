import os
import platform
import print_nice


def linux_distribution():

    try:
        return platform.linux_distribution()
    except:
        return "N/A"


def get_os_name():
    if os.name == "nt":
        return "windows"
    else:
        return "linux"


# stuff to run always here such as class/def
def main():

    print_nice.print_nice("", "Operating System Details (" + get_os_name() + ")")
    if os.name == "nt":
        print(platform.architecture(), platform.platform(), platform.uname())
    elif os.name == "posix":
        print(linux_distribution(), platform.system(),
              platform.machine(), platform.platform(), platform.uname(), platform.version())
    else:
        print("Unsupported OS", os.name, platform.architecture(), platform.platform(), platform.system())


if __name__ == "__main__":
    main()

