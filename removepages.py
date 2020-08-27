import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file")
parser.add_argument("--output", "-o", help="output file. Program will run in place without this defined.")
parser.add_argument("pages", help="pages to remove", nargs="+")
args = parser.parse_args()

outpath = args.input if not args.output else args.output  # Default to in place operation

pdf = PdfFileReader(args.input)
output = PdfFileWriter()
pagesToDelete = [int(i) for i in args.pages]

for i in range(pdf.getNumPages()):
    if i not in pagesToDelete:
        output.addPage(pdf.getPage(i))

with open(outpath, "wb") as outfile:
    output.write(outfile)
