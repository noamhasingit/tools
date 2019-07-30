import os
import print_nice


def check_env_var(name, value):
    print_nice.print_nice("", "Env Variables")
    print(name, os.environ[name])


# stuff to run always here such as class/def
def main():
    check_env_var("LANG", "en_US.UTF-8")


if __name__ == "__main__":
    main()


