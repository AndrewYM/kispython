def main(arr):
    s = [
        {'GO', 'GAMS', 'SAS', arr[3]},
        {'GO', 'SCALA', 'SAS', arr[3]},
        {'HCL', arr[1], 'SAS', 'OX'},
        {'HCL', arr[1], 'SAS', 'LOGOS'},
        {'EJS', arr[1], 'SAS', 'OX'},
        {'EJS', arr[1], 'SAS', 'LOGOS'},
        [arr[0], 'GAMS', 'EC', 'OX'],
        [arr[0], 'SCALA', 'EC', 'OX'],
        [arr[0], arr[1], 'EC', 'LOGOS'],
        [arr[0], arr[1], 'GN', arr[3]],
    ]

    s1 = set(arr)
    return [i for i in range(len(s)) if not (
        len(set(s[i]) - s1))][0]
