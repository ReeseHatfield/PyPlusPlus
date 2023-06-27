import sys


def main(args):
    # transpile.py [optional -r] [if -r, transpile and run this file, else just transpile] [transpile_me_1.py] ...
    # args[1] is file itself

    run_file, file_to_run = is_runnable(args)




def is_runnable(args):
    if args[1] == '-r':

        try:
            run_file = True
            file_to_run = args[2]
            print(f'Running {args[2]}...')
        except IndexError:
            print('Error: no runable file given')
    return run_file, file_to_run


if __name__ == "__main__":
    main(sys.argv);
