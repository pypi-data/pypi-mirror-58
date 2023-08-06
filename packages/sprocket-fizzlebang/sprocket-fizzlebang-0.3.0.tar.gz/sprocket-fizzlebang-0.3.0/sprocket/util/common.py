import os
from pathlib import Path

from fuzzywuzzy import process


def repo_root(*args):
    return os.path.join(Path(__file__).parent.parent, *args)


def find_audio(str):
    directory = repo_root("data", "audio")
    if os.path.exists(directory):

        contents = {x.split(".")[0]: x for x in os.listdir(directory)}

        match_ratios = process.extract(str, list(contents.keys()))
        best_str, best_ratio = match_ratios[0]

        if best_ratio == 100:
            return repo_root(directory, contents[best_str])
        else:
            return [x[0] for x in match_ratios]


def ls(directory, **kwargs):
    filter = kwargs.get("filter", "")
    delim = kwargs.get("delim", None)
    contents = [
        x.split(delim)[0] for x in os.listdir(directory) if filter in x
    ]
    return sorted(contents)
