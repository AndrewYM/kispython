def is_truthy(value):
    return value == "1"


def extract_second_word(cell_value):
    words = cell_value.split()
    return words[1] if len(words) > 1 else None


def extract_digits(cell_value):
    return ''.join(char for char in cell_value if char.isdigit(
    )) if cell_value else None


def remove_email_suffix(cell_value):
    return cell_value.split('[at]')[0] if cell_value else None


def transform_cell(cell_value, col_index):
    if col_index == 0:
        return "Да" if is_truthy(cell_value) else "Нет"
    elif col_index == 1:
        return extract_second_word(cell_value)
    elif col_index == 2:
        return extract_digits(cell_value)
    elif col_index == 3:
        return remove_email_suffix(cell_value)


def remove_empty_columns(table):
    non_empty_columns = [col_index for col_index, column in enumerate(
        zip(*table)) if any(cell is not None for cell in column)]
    return [[row[i] for i in non_empty_columns] for row in table if any(
        cell is not None for cell in row)]


def main(table):
    transformed_table = []
    table = remove_empty_columns(table)
    for row in table:
        transformed_row = [transform_cell(cell_value,
                                          col_index) for col_index,
                           cell_value in enumerate(row)]
        transformed_table.append(transformed_row)
    return transformed_table
