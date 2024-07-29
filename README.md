# ccwc

`ccwc` is a simple word count utility that counts the number of lines, words, and characters in a text file. It is inspired by the Unix `wc` command and provides similar functionality.

## Features

- Count the number of lines in a text file
- Count the number of words in a text file
- Count the number of characters in a text file
- Count the number of bytes in a text file

## Requirements

- Python 3.6 or higher

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/emmanuelmoon/ccwc.git
cd ccwc
```

### Step 2: Create and activate a virtual environment

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install the requirements

```bash
pip install -r requirements.txt
```

## Usage

Run the `ccwc.py` script with the text file you want to analyze as an argument:

```bash
python ccwc.py <file_path>
```

Replace `<file_path>` with the path to the text file you want to count.

## Example

This will output the number of lines, words, and bytes in `test.txt`.

```bash
python ccwc.py test.txt
 7145 58164 342190 test.txt
```

This will output the number of bytes in `test.txt`.

```bash
python ccwc.py -c test.txt
 342190 test.txt
```

This will output the number of lines in `test.txt`.

```bash
python ccwc.py -l test.txt
 7145 test.txt
```

This will output the number of words in `test.txt`.

```bash
python ccwc.py -l test.txt
 58164 test.txt
```

This will output the number of characters in `test.txt`.

```bash
python ccwc.py -c test.txt
 339292 test.txt
```

This will run using standard input, since no filename is provided

```bash
cat test.txt | python ccwc -l
 7145
```

## Running Tests

To run tests for this project, you can use `pytest`. The tests are defined to check various functionalities of the `ccwc` command.

1. Install `pytest` if you haven't already:

   ```bash
   pip install pytest
   ```

2. Run the tests:

   ```bash
   pytest test_ccwc.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
