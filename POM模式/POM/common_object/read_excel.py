from openpyxl import load_workbook

def read_xlsx(filename,sheet):
    wb = load_workbook(filename)

    ws = wb[sheet]

    test_case = []
    value_name = []

    for row in ws:
        case = []
        # test_case.append(row[0].value)
        # value_name.append(row[1].value)
        for i in row:
            if i.value is not None:
                case.append(i.value)
            else:
                case.append('')

        test_case.append(case[:-1])
        value_name.append(case[-1])

    return test_case[1:],value_name[1:]


if __name__ == '__main__':
    car_list, ids = read_xlsx('D:\\POM\\data\\车场列表用例.xlsx', 'CarList')
    print(car_list)
    print(ids)