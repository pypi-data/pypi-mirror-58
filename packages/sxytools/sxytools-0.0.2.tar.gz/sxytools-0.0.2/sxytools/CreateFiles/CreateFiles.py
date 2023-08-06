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
    if size[-1] == "K":
        size = int(size[:-1]) * 1024
    elif size[-1] == "M":
        size = int(size[:-1]) * 1024 * 1024
    elif size[-1] == "G":
        size = int(size[:-1]) * 1024 * 1024 * 1024
    else:
        print("Size must use K/M/G")
    return size


def create_random_files(father_file_folder_path, num, min_size, max_size):
    """创建随机文件

    :param father_file_folder_path:顶层目录
    :param num: 文件数量
    :param min_size: 文件大小范围下限
    :param max_size: 文件大小范围上限
    :return: 存放随机文件的随机文件夹路径
    """
    # 创建随机父目录
    file_folder_path = create_random_file_folder(father_file_folder_path)
    print('Create folder:{}'.format(file_folder_path))

    min_size = convert_size_to_byte(min_size)
    max_size = convert_size_to_byte(max_size)
    for number in range(int(num)):
        size = random.randint(int(min_size), int(max_size))
        file_name = create_random_file(file_folder_path, size)
        print("[Num:{}][File Created:{}][Size:{}]".format(number+1, file_name, size))
        time.sleep(0.1)
    return file_folder_path


def CreateRandomFiles(base_path, run_times, nums, max_size, min_size, clear_flag):
    """创建随机文件

    :param base_path:
    :param run_times:
    :param nums:
    :param max_size:
    :param min_size:
    :param clear_flag:
    :return:
    """
    father_path = r'{}/test'.format(base_path)
    print(father_path)

    for i in range(run_times):
        create_random_files(father_path, nums, min_size, max_size)
        if clear_flag == 1:
            try:
                shutil.rmtree(father_path)
                print("Delete files")
            except BaseException as e:
                print(e)
