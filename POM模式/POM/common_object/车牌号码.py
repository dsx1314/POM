import random


def get_car_number():
    letter = ['京','津','泸','鲁','贵','粤','湘','冀','晋','蒙','辽','黑','沪','苏','浙',
              '皖','闽','赣','豫','鄂','桂','琼','渝','川']

    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    english = ['A','B','C','D','E','F','G','H','J','K','L','N','M','P','Q','R','S','T','U','V','W','X','Y','Z']


    value_01 = "".join(random.sample(letter,1))

    value_chinese = "".join(random.sample(english,1))


    total_two = number + english
    value_02 = "".join(random.sample(total_two,5))

    total = value_01 + value_chinese + value_02

    return total

if __name__ == '__main__':
    print(get_car_number())


# import random
#
#
# def get_number():
#     letter = ['京','津','泸','鲁','贵','粤','湘','冀','晋','蒙','辽','黑','沪','苏','浙',
#               '皖','闽','赣','豫','鄂','桂','琼','渝','川']
#
#     number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     english = ['A','B','C','D','E','F','G','H','J','K','L','N','M','P','Q','R','S','T','U','V','W','X','Y','Z']
#
#     two_demo = number + english
#     # print(two_demo)
#     f = open('dsx.csv', 'w')
#     f.write('carnumber\n')
#     for i in range(300):
#
#         u_len = random.randint(5, 6)
#         value_demo = ''.join([random.choice(two_demo) for i in range(u_len)])
#
#         # print(value_demo)
#         p_len = random.randint(1,1)
#         value_demo_2 = ''.join([random.choice(letter) for i in range(p_len)])
#         # print(value_demo_2)
#
#         n_len = random.randint(1,1)
#         n_value = ''.join([random.choice(english) for i in range(n_len)])
#
#         total_value = value_demo_2 + n_value + value_demo
#
#         print(total_value)
#         f.write(f'{total_value}\n')
#     f.close()
# if __name__ == '__main__':
#     get_number()