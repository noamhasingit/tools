import subprocess
import print_nice

def checklib(lib_name):

    rpm_command_line = "-qa"
    command = ['rpm', rpm_command_line, lib_name]
    p = run(command, subprocess.PIPE)



def run(*popenargs, input=None, check=False, **kwargs):
    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:

        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr


# stuff to run always here such as class/def
def main():

    print_nice.print_nice("", "Libraries")
    print_nice.print_nice("glibc:",)
    checklib("glibc")
    print_nice.print_nice("glibc-common:",)
    checklib("glibc-common")
    print_nice.print_nice("libxslt:")
    checklib("libxslt")
    print_nice.print_nice("bc:")
    checklib("bc")
    print_nice.print_nice("unixODBC:")
    checklib("unixODBC")


if __name__ == "__main__":
    main()


