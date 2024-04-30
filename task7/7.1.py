def main(arr):
    default = [
        ['GO', 'GAMS', 'SAS', arr[3]],
        ['GO', 'SCALA', 'SAS', arr[3]],
        ['HCL', arr[1], 'SAS', 'OX'],
        ['HCL', arr[1], 'SAS', 'LOGOS'],
        ['EJS', arr[1], 'SAS', 'OX'],
        ['EJS', arr[1], 'SAS', 'LOGOS'],
        [arr[0], 'GAMS', 'EC', 'OX'],
        [arr[0], 'SCALA', 'EC', 'OX'],
        [arr[0], arr[1], 'EC', 'LOGOS'],
        [arr[0], arr[1], 'GN', arr[3]],
    ]
    return default.index(arr)
