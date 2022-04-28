import pytest
from os import system


if __name__ == '__main__':
    # pytest.main(['--reruns=1'])
    pytest.main()
    ret = system('allure generate output/result --clean -o output/report')

    # open_html = system('allure open output/report')
    if ret == 0:
        print('生成测试报告成功')
    else:
        print('生成测试报告失败')