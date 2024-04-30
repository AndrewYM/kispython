def main(arr):
    match arr[2]:
        case 'GN':
            return 9
        case 'EC':
            return handle_EC(arr)
        case 'SAS':
            return handle_SAS(arr)


def handle_EC(arr):
    match arr[3]:
        case 'LOGOS':
            return 8
        case 'OX':
            match arr[1]:
                case 'SCALA':
                    return 7
                case 'GAMS':
                    return 6


def handle_SAS(arr):
    match arr[0]:
        case 'EJS':
            return handle_EJS(arr)
        case 'HCL':
            return handle_HCL(arr)
        case 'GO':
            return handle_GO(arr)


def handle_EJS(arr):
    match arr[3]:
        case 'LOGOS':
            return 5
        case 'OX':
            return 4


def handle_HCL(arr):
    match arr[3]:
        case 'LOGOS':
            return 3
        case 'OX':
            return 2


def handle_GO(arr):
    match arr[1]:
        case 'SCALA':
            return 1
        case 'GAMS':
            return 0
