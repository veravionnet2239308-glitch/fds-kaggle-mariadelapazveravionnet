import json

def load_jsonl(path):
    """
    Loads a JSONL file and returns a list of Python dicts.
    """
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data
