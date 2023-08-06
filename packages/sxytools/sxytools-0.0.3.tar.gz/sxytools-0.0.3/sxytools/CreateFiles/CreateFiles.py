# -*- coding:utf-8 -*-
"""
脚本说明
此脚本为Python脚本，需要安装Python 3.0

脚本功能
创建随机大小文件

功能描述
1、批量创建随机文件夹，文件夹内产生指定数量的指定随机大小文件，文件名为文件的MD5值
2、创建文件不要太大，建议在最大在1G内，太大内存无法分配。
3、need_delete 标志为创建完毕后是否创建的文件夹和文件。
4、create_random_files函数中的sleep.time(秒)可以控制文件创建的速度。
"""

import os
import sys
import random
import string
import shutil
import hashlib
import time
if sys.version_info[0] < 3:
    raise RuntimeError(r'At least Python 3 is required')

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# 错误码
UNSUPPORT_SIZE = 100
PATH_NOT_EXIST = 101
STRING_NOT_INT = 102
STRING_NOT_TUPLE = 103
STRING_NOT_STRING = 104

def create_random_file(file_path, size):
    """产生一个指定大小的txt文件,文件名为其md5值

    :param file_path: 文件路径
    :param size: 文件大小,单位b
    :return: 文件路径+文件名
    """

    old_file_name = r'{}/tmp_file_name.txt'.format(file_path)
    with open(old_file_name, 'wb') as fp:
        fp.write(os.urandom(size))
    fp.close()
    myhash = hashlib.md5()
    with open(old_file_name, 'rb') as fp:
        while True:
            b = fp.read(8096)
            if not b:
                break
            myhash.update(b)
    new_file_name = r'{}/{}.txt'.format(file_path, myhash.hexdigest())
    try:
        os.rename(old_file_name, new_file_name)
    except Exception as e:
        print(e)
    return new_file_name


def create_random_file_folder(father_file_folder_path):
    """产生一个随机的文件夹
    文件夹名称是一个10位的字符串

    :param father_file_folder_path:文件夹父目录
    :return: 文件夹路径
    """
    file_folder_name = r''.join(random.sample(string.ascii_letters + string.digits, 10))
    file_folder_path = r'{}/{}'.format(father_file_folder_path, file_folder_name)
    if not os.path.exists(file_folder_path):
        os.makedirs(file_folder_path)
    return file_folder_path


def convert_size_to_byte(size):
    if size[-1] == "K" or size[-1] == "k":
        size = int(size[:-1]) * 1024
    elif size[-1] == "M" or size[-1] == "m":
        size = int(size[:-1]) * 1024 * 1024
    elif size[-1] == "G" or size[-1] == "g":
        size = int(size[:-1]) * 1024 * 1024 * 1024
    else:
        print("Error:Size must end with k/K/m/M/g/G")
        exit(UNSUPPORT_SIZE)
    return size


def create_random_files(father_file_folder_path, num, min_size, max_size, current_turn, total_files,interval_time=0.1):
    """创建随机文件

    :param father_file_folder_path:顶层目录
    :param num: 文件数量
    :param min_size: 文件大小范围下限
    :param max_size: 文件大小范围上限
    :param current_turn:
    :param total_files:
    :param interval_time:
    :return: 存放随机文件的随机文件夹路径
    """
    # 创建随机父目录
    file_folder_path = create_random_file_folder(father_file_folder_path)
    print(r'Info:Create folder "{}"'.format(file_folder_path))

    min_size = convert_size_to_byte(min_size)
    max_size = convert_size_to_byte(max_size)
    for number in range(int(num)):
        size = random.randint(int(min_size), int(max_size))
        file_name = create_random_file(file_folder_path, size)
        print(r'Info:[{}/{}]Create file "{}"  Size:{} '.format(current_turn*num+number+1, total_files, file_name, size))
        time.sleep(interval_time)
    return file_folder_path


def CreateRandomFiles(base_path, turns, nums, max_size, min_size, clear_flag=False, interval_time=0.1):
    """创建随机文件

    :param base_path:创建文件的父目录
    :param turns:创建文件夹个数
    :param nums:每个文件夹中文件个数
    :param max_size:每个随机文件最大值（建议最大不要超过1G）
    :param min_size:每个随机文件最小值
    :param clear_flag:每次执行后是否删除创建的文件和文件夹，True为删除 False为保留(默认保留)
    :param interval_time:文件创建时间间隔，默认最短0.1秒创建1个文件（大文件创建时间可能需要长）
    :return:
    """

    if not os.path.exists(base_path):
        exit(PATH_NOT_EXIST)

    if type(turns) is not int:
        print_usage()
        exit(STRING_NOT_INT)

    if type(nums) is not int:
        exit(STRING_NOT_INT)

    if type(min_size) is not str:
        exit(STRING_NOT_STRING)

    if type(max_size) is not str:
        exit(STRING_NOT_STRING)

    if type(clear_flag) is not bool:
        exit(STRING_NOT_TUPLE)

    father_path = r'{}/test'.format(base_path)
    print(r'Info:Create folder "{}"'.format(father_path))

    for i in range(turns):
        create_random_files(father_path, nums, min_size, max_size, i, turns * nums, interval_time)
        if clear_flag is True:
            try:
                shutil.rmtree(father_path)
                print("Info:Delete All Created files.")
            except BaseException as e:
                print(e)
        else:
            print("Info:Total {} files Created.".format(turns * nums))


def print_usage():
    print('函数用法:\n'
          '\tCreateRandomFiles(base_path, turns, files_num, file_size_max, file_size_min, clear_flag=True, interval_time=0.1)\n'
          '\t\tbase_path:创建文件的父目录，需要是已存在的路径，绝对路径\n'
          '\t\ttruns:创建文件夹个数，数字\n'
          '\t\tfiles_num:每个文件夹中文件个数，数字\n'
          '\t\tfile_size_max:每个随机文件最大值（建议最大不要超过1G），字符串以kKgGmG字母结尾\n'
          '\t\tfile_size_min:每个随机文件最小值，字符串以kKgGmG字母结尾\n'
          '\t\tclear_flag:每次执行后是否删除创建的文件和文件夹，True为删除 False为保留(默认保留)\n'
          '\t\tinterval_time:文件创建时间间隔，默认0.1秒创建1个文件\n'
          '例子:\n'
          '\t在C:\TestFolder下随机创建200个1k-10m的随机文件（每个随机文件夹中创建100个随机文件，共创建2个随机文件夹）\n'
          '\tCreateRandomFiles("C:\TestFolder", 2, 100, 1k, 10m)\n')


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    turns = 1  # 运行多少次
    files_num = 10  # 每次产生多少文件
    file_size_min = "1K"  # 产生文件的最小值
    file_size_max = "10k"  # 产生文件的最大值
    clear_all = True  # 每次执行后是否删除创建的文件和文件夹

    CreateRandomFiles(base_path, turns, files_num, file_size_max, file_size_min)
