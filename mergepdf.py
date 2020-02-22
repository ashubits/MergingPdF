import os
from PyPDF2 import PdfFileMerger
# use dict to sort by filepath or filename
file_dict = {}
for subdir, dirs, files in os.walk("a"):
    for file in files:
        filepath = subdir + os.sep + file
        # you can have multiple endswith
        if filepath.endswith((".pdf", ".PDF")):
            file_dict[file] = filepath
# use strict = False to ignore PdfReadError: Illegal character error
merger = PdfFileMerger(strict=False)

for k, v in file_dict.items():
    print(k, v)
    merger.append(v)

merger.write("combined_result.pdf")
