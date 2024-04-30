import re


def main(input_string):
    pattern = r'<block>\s*auto\s*([^\s]+)\s*->\s*([^\s;]+);\s*</block>'
    matches = re.findall(pattern, input_string)
    parsed_result = [(value, key) for key, value in matches]
    return parsed_result
