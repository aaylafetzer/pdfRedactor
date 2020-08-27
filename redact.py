from pdfredactor import pdf_redactor
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("text", help="strings to remove", nargs="+")
args = parser.parse_args()

# Define the redactor options
options = pdf_redactor.RedactorOptions()
# Clear all PDF metadata
options.metadata_filters = {
    "DEFAULT": [lambda value: None]
}
# Clear all PDF metadata
options.xmp_filters = [lambda xml: None]
# Redact the actual content
options.content_filters = []
for string in args.text:
    options.content_filters.append(
        (
            re.compile(string),
            lambda m: "X" * len(string)
        )
    )
pdf_redactor.redactor(options)
