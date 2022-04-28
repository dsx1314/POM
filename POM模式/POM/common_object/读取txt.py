# import csv
#
# def read_csv():
#     file = 'D:\\POM\common_object\\dsx.csv'
#
#     with open(file) as f:
#         read = csv.reader(f)
#         header_row = next(read)
#
#         for row in read:
#             print(row)
# if __name__ == '__main__':
#     read_csv()

def read_txt():
    result = []
    f = open('D:\\POM\\common_object\\dsx.txt','r')
    # for line in f.readlines():
    #     result.append(list(map(int,line.split(','))))
    # print(result)
    a = list(f)
    # print('success-1')
    return a


if __name__ == '__main__':
    print(read_txt())