from click.testing import CliRunner
from ccwc import ccwc
import pytest
import subprocess

runner = CliRunner()


def test_byte_count():
    result = runner.invoke(ccwc, ['-c', 'test.txt'])
    assert result.output == ' 342190 test.txt\n'


def test_line_count():
    result = runner.invoke(ccwc, ['-l', 'test.txt'])
    assert result.output == ' 7145 test.txt\n'


def test_word_count():
    result = runner.invoke(ccwc, ['-w', 'test.txt'])
    assert result.output == ' 58164 test.txt\n'


def test_char_count():
    result = runner.invoke(ccwc, ['-m', 'test.txt'])
    assert result.output == ' 339292 test.txt\n'


def test_all():
    result = runner.invoke(ccwc, ['test.txt'])
    assert result.output == ' 7145 58164 342190 test.txt\n'


def test_pipe():
    output = subprocess.check_output(
        'cat test.txt | python ccwc.py -l', shell=True)
    assert output.decode('utf-8') == ' 7145\n'


if __name__ == '__main__':
    pytest.main()
