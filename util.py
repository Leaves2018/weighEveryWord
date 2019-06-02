# -*- coding="UTF-8" -*-
import re


def lines(file):
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


def sentences(file):
    text = file.read()
    s = re.split("[.!?]+", text)
    for sentence in s:
        yield sentence
