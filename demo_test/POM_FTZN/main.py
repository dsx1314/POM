from os import system
import pytest
from common.mail_utils import send_test_report


def main():
    pytest.main(['D:\\POM_ftzn\\test_cases\\po_login.py'])
    ret = system('allure generate output/result --clean -o output/report')
    if ret == 0:
        print('生成测试报告成功')
    else:
        print('生成测试报告失败')

    send_test_report('今晚9点老地方', '查看测试报告', 'D:\\POM_ftzn\\output\\report\\index.html')
if __name__ == '__main__':
    main()