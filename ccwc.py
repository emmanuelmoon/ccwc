import os
import sys
import click
import select


def stdin_operations():
    byte_count, word_count, line_count, char_count = 0, 0, 0, 0
    for line in sys.stdin.buffer:
        byte_count += len(line)
        encoded_line = line.decode()
        line_count += line.count(b'\n')
        word_count += len(encoded_line.split())
        char_count += len(encoded_line)
    return byte_count, word_count, line_count, char_count


def file_operations(filename):
    try:
        byte_count = os.path.getsize(filename)
        line_count = 0
        word_count = 0
        char_count = 0
        with open(filename, 'rb') as file:
            for line in file:
                line_count += line.count(b'\n')
                word_count += len(line.split())
                char_count += len(line.decode())
        return byte_count, word_count, line_count, char_count
    except Exception as exc:
        raise exc


@click.command()
@click.option('-c', '--count-bytes/--no-count-bytes', default=False)
@click.option('-l', '--count-lines/--no-count-lines', default=False)
@click.option('-w', '--count-words/--no-count-words', default=False)
@click.option('-m', '--count-chars/--no-count-chars', default=False)
@click.argument('filename', required=False, default='-')
def ccwc(count_bytes, count_lines, count_words, count_chars, filename):
    if filename != '-':
        if os.path.exists(filename):
            try:
                (byte_count, word_count, line_count,
                 char_count) = file_operations(filename)
                results = ['']

                expression = (count_bytes
                              or count_lines
                              or count_words
                              or count_chars)
                if count_lines or not expression:
                    results.append(line_count)
                if count_words or not expression:
                    results.append(word_count)
                if count_bytes or not expression:
                    results.append(byte_count)
                if count_chars:
                    results.append(char_count)
                results.append(filename)
                print(' '.join(map(lambda result: str(result), results)))
            except Exception:
                print('Error')
        else:
            exit('ccwc: No valid file or directory provided')

    else:
        try:
            if select.select([sys.stdin, ], [], [], 0.0)[0]:
                (byte_count, word_count, line_count,
                 char_count) = stdin_operations()
                results = ['']

                expression = (count_bytes
                              or count_lines
                              or count_words
                              or count_chars)
                if count_lines or not expression:
                    results.append(line_count)
                if count_words or not expression:
                    results.append(word_count)
                if count_bytes or not expression:
                    results.append(byte_count)
                if count_chars:
                    results.append(char_count)
                print(' '.join(map(lambda result: str(result), results)))
            else:
                raise Exception
        except Exception:
            exit('ccwc: No valid file or directory provided')



if __name__ == '__main__':
    ccwc()
