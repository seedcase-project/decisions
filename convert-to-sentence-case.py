import os
import re


def sentence_case(text):
    return text[0].upper() + text[1:].lower()


def process_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if line.startswith("#"):
                # This is a header line
                line_content = line.lstrip("# ").rstrip("\n")
                line = line.replace(line_content, sentence_case(line_content))
            file.write(line)


# Walk through the current directory and process all .qmd files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".qmd"):
            process_file(os.path.join(root, file))
