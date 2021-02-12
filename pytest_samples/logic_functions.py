import json
from collections import Counter

def is_balanced(inp_str):
    '''
    Check if input string has balanced number of brackets e.g.:
        {[()]} - balanced
        {{[ }}] - unbalanced
        {()}[]() - balanced
    :return: bool: returns True if string could be considered as balanced
    '''

    c = Counter(inp_str)
    brackets = {
        '{': '}',
        '[': ']'
    }
    for b in brackets:
        if b in c:
            if not c[b] == c[brackets[b]]:
                return False
    return True







def get_json_data_from_file(path):
    '''
    :param path: str path to file with json data
    :return: dict with decocded json
    :raise
        FileNotFoundError if path is not correct

    '''
    with open(path, 'r') as f:
        return json.load(fp=f)
