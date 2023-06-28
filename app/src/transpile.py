import os
import sys
import tempfile
import runpy


def main(args):
    run_file, file_to_run = is_runnable(args)
    starting_file = 3 if run_file else 1

    for file_index in range(starting_file, len(args)):
        transpile_file(args[file_index])

    if run_file:
        transpile_file(file_to_run)
        print(f'Running {file_to_run}...')
        runpy.run_path(file_to_run)


def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def transpile_file(file: str):
    with open(file, 'r') as f, tempfile.NamedTemporaryFile('w', delete=False) as tf:
        buffer = ''
        for piece in read_in_chunks(f, 1):
            buffer += piece
            if len(buffer) == 2:
                if buffer == '++':
                    buffer = '+= 1'
                tf.write(buffer)
                buffer = ''

    os.replace(tf.name, file)


def is_runnable(args):
    run_file = False
    file_to_run = None

    if len(args) > 1 and args[1] == '-r':
        if len(args) > 2:
            run_file = True
            file_to_run = args[2]
        else:
            print('Error: no runnable file given')
            return False, None
    return run_file, file_to_run


if __name__ == "__main__":
    main(sys.argv)
