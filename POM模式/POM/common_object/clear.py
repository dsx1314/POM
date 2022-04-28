import os
import shutil

# 整个我文件夹清空
# def clean(filename):
#     if os.path.isdir(filename):
#         shutil.rmtree(filename)
#         print("---清理完毕---")




# 清理文件夹的内容·
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

if __name__ == '__main__':
    del_file(r'D:\POM\picture')