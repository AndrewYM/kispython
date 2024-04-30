def main(input_string):
    blocks = input_string.split('<block>')
    parsed_result = []
    for block in blocks[1:]:
        data = block.split('</block>')[0].strip()
        if 'auto' in data:
            data = data.split('auto')[1].strip()
            key, value = data.split('->')
            key = key.strip()
            value = value.strip().rstrip(';')
            parsed_result.append((value, key))
    return parsed_result
