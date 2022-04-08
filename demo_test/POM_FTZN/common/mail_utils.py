

import yagmail
from openpyxl import load_workbook


def send_test_report(subject, contents, report):
    """
    发送测试报告邮件
    :param subject: 邮件主题
    :param contents: 邮件内容
    :param report: 测试报告文件
    :return:
    """
    # 连接邮件发送服务器
    mail = yagmail.SMTP(user='2986787982@qq.com',
                        password='fsjxmtdqxnsudege',
                        host='smtp.qq.com')

    wb = load_workbook('D:\\POM_ftzn\\lib\\system_config.xlsx')
    ws = wb['email_receiver']

    # 读取Excel里的收件人地址
    addr = []
    for row in ws:
        # print(row[0].value)
        addr.append(row[0].value)

    addr.pop(0)
    print(addr)


    # 发送邮件
    mail.send(to=addr,
              subject=subject,
              contents=contents,
              attachments=report)

    # 关闭连接
    mail.close()


if __name__ == '__main__':
    send_test_report('今晚8点老地方', 'xxxx', 'D:\\POM_ftzn\\output\\report\\index.html')
    print("-----发送成功-----")