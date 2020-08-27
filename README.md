[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aaylafetzer/pdfRedactor)
# pdfRedactor
An argparse-based wrapper [JoshData's pdf-redactor](https://github.com/JoshData/pdf-redactor) to redact specific strings
such as names, dates, etc from pdf files.

## Usage
To use
- ``redact.py``: Pipe the pdf you want to redact with a command like ``cat`` into the program, list the strings to 
redact as arguments, and direct stdout to a file. For example:
```cat input.pdf | python3 redact.py "My name" "My address" > redacted_file.pdf```

- ``removepages.py``: Provide the input path as an argument and the page numbers to redact as trailing arguments. An
output file can optionally be defined with ``-o``, but the program will overwrite the input file by default if an
output file is not defined. For example, to drop pages 3, 6, and 9 from input.pdf and write the result to output.pdf:
```python3 removepages.py input.pdf  -o output.pdf 3 6 9```