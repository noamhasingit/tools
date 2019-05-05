import sys


def print_nice(message='', title='', char_painter='*', num=10):

    if len(message) > 0 and len(title) == 0:
        sys.stdout.write("\n")
        print(message)

        return
    total_chars = len(title) + num * 2

    i = 0
    while i < total_chars + 2:
        i = i + 1
        sys.stdout.write(char_painter)
    sys.stdout.write("\n")

    i = 0
    while i < num:
        i = i + 1
        sys.stdout.write(char_painter)

    sys.stdout.write(" " + title + " ")
    i = 0
    while i < num:
        i = i + 1
        sys.stdout.write(char_painter)
    i = 0
    sys.stdout.write("\n")
    while i < total_chars + 2:
        i = i + 1
        sys.stdout.write(char_painter)
    sys.stdout.write("\n")

    if len(message) > 0:
        print(message)


def main():
    print_nice("print_nice(message, title='', char_painter='*', num=10)", "Usage")


if __name__ == "__main__":
    main()
