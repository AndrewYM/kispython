def main(df):
    result = []
    for i in range(len(df)):
        x = df[i]
        x[1] = ('Нет', 'Да')[x[1] == '1']
        x[2] = x[2].split('. ')[-1]
        x[3] = ''.join(filter(str.isdigit, x[3]))
        x[4] = x[4].split('[at]')[0]
        mas = [x[1], x[2], x[3], x[4]]
        result.append(mas)
    return result
