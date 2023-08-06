# -*- coding:utf-8 -*-
from __future__ import print_function
import cx_Oracle
import random
import string
import time
import sys
if sys.version_info < (2, 7):
    raise RuntimeError(r'At least Python 2.7 is required')


class OracleDB:
    """提供Oracle数据库的基本操作
    参数：
        host:Oracle主机名（IP或计算机名）
        db_user_name:数据库用户名
        db_passwd:数据库密码
        service_name:数据库服务名
        port:端口号，默认1521
        protocol:连接协议，默认TCP
    方法：
        Query:查询
        Exec:增、删、改
    """

    def __init__(self, host, db_user_name, db_passwd, service_name, port=1521, protocol='TCP'):
        self._host = host
        self._db_user_name = db_user_name
        self._db_passwd = db_passwd
        self._service_name = service_name
        self._port = port
        self._protocol = protocol
        self._conn = None
        self.ReConnect()

    def ReConnect(self):
        if not self._conn:
            tns = '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL={})(HOST={})' \
                  '(PORT={})))(CONNECT_DATA=(SERVICE_NAME={})))'.format(self._protocol,
                                                                        self._host,
                                                                        self._port,
                                                                        self._service_name)
            try:
                self._conn = cx_Oracle.connect(self._db_user_name, self._db_passwd, tns)
            except cx_Oracle.DatabaseError:
                self._conn = cx_Oracle.connect(self._db_user_name, self._db_passwd, tns, cx_Oracle.SYSDBA)
        else:
            pass

    def __del__(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def NewCursor(self):
        cur = self._conn.cursor()
        if cur:
            return cur
        else:
            return None

    def DelCursor(self, cur):
        if cur:
            cur.close()

    def Commit(self):
        if self._conn:
            self._conn.commit()

    def Execute(self, cur, sql):
        rt = True
        rs = None
        if cur:
            try:
                cur.execute(sql)
            except cx_Oracle.DatabaseError as e:
                rs = str(e)
                rt = False
        return rt, rs

    # 检查sql语句
    def PermitedUpdateSql(self, sql):
        rt = True
        lrsql = sql.lower()
        sql_elems = lrsql.strip().split()

        # 更新删除语句，判断首单词，不带where语句的sql不予执行
        if sql_elems[0] in ['update', 'delete']:
            if 'where' not in sql_elems:
                rt = False

        return rt

    # 导出结果为文件
    def Export(self, sql, file_name, colfg = '||'):
        rt = self.Query(sql)
        if rt:
            with open(file_name, 'a') as fd:
                for row in rt:
                    ln_info = ''
                    for col in row:
                        ln_info += str(col) + colfg
                    ln_info += '\n'
                    fd.write(ln_info)
                    fd.close()

    # 查询
    def Query(self, sql, nStart=0, nNum=-1):
        rt = None
        rs = []

        # 获取cursor
        cur = self.NewCursor()
        if not cur:
            return rt,rs

        rt, rs = self.Execute(cur, sql)
        if rt:
            rs = []  # 查询结果放入列表
            if (nStart == 0) and (nNum == 1):
                rs.append(cur.fetchone())
            else:
                rs = cur.fetchall()
                if nNum == -1:
                    rs.extend(rs[nStart:])
                else:
                    rs.extend(rs[nStart:nStart + nNum])

        # 释放cursor
        self.DelCursor(cur)

        return rt, rs

    # 增、删、改
    def Exec(self, sql):
        # 获取cursor
        rt = None
        rs = None
        cur = self.NewCursor()
        if not cur:
            return rt, rs

        # 判断sql是否允许其执行
        if not self.PermitedUpdateSql(sql):
            return rt, rs

        # 执行语句
        rt, rs = self.Execute(cur, sql)

        # 释放cursor
        self.DelCursor(cur)

        # commit
        self.Commit()

        return rt, rs


def OracleDBTest(host, username, password, service_name, tablespace_name, datafile_path, size, max):
    print('准备连接数据库')
    ora = OracleDB(host, username, password, service_name)
    print('数据库连接成功')
    print('正在查询数据库所有表空间')
    rt, rs = ora.Query("select * from v$tablespace")  # 查询数据库所有表空间，rs为查询结果
    print('查询成功')
    if rt:  # 查询成功
        for result in rs:
            if result[1] == tablespace_name.upper():  # 如果数据库中存在表空间[tablespace_name],则删除表空间
                print('表空间[{}]已经存在，删除表空间'.format(tablespace_name))
                rt, rs = ora.Exec(
                    'drop tablespace {} including contents and datafiles cascade constraint'.format(tablespace_name))
                print('表空间[{}]删除完毕'.format(tablespace_name))
                break
        # 创建表空间[tablespace_name]
        print('即将创建表空间{},{},{}G'.format(tablespace_name, datafile_path, size))
        rt, rs = ora.Exec("create tablespace {} datafile {} size {}G".format(tablespace_name, datafile_path, size))
        print('创建表空间{} 创建完毕'.format(tablespace_name, datafile_path, size))
        if not rt:
            print('创建表空间失败[{}]'.format(rs))
            exit(1)

    else:  # 查询失败
        print('查询数据库空间失败[{}]'.format(rs))
        exit(1)

    tables = ['table1', 'table2', 'table3', 'table4', 'table5', 'table6', 'table7', 'table8', 'table9']
    # 在表空间[tablespace_name]中创建表
    for table_name in tables:
        ora.Exec('create table {}(name VARCHAR2(50),address VARCHAR2(50),age NUMBER) tablespace {}'.format(table_name,
                                                                                                           tablespace_name))
        print('Create table {}'.format(table_name))

    num = 0
    while 1:
        rt, rs = ora.Query('select * from v$flash_recovery_area_usage')
        archivelog_used = rs[2][1]
        print('Query archive log space: {}'.format(archivelog_used))
        if int(archivelog_used) > 90:
            break
        num = num + 1
        j = random.randint(0, 8)
        table_name = tables[j]  # 随机取一张表
        name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        addr = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        age = num
        ora.Exec("insert into {} VALUES('{}','{}',{})".format(table_name, name, addr, age))  # 向表中插入随机数据
        print('Insert valuse into table {}: name({}) addr({}) age({})'.format(table_name, name, addr, age))
        rt, rs = ora.Query("select * from {}".format(table_name))  # 插入后查询整个表
        print('Query table {} all records'.format(table_name))
        rt, count = ora.Query("select count(*) from {}".format(table_name))  # 查询表中数据数量
        print('Query table {} record count({})'.format(table_name, count))
        if int(count[0][0]) > max:  # 如果表中数据达到临界值，则清空表
            ora.Exec('drop table {}'.format(table_name))
            print('Drop tables {}'.format(table_name))
            ora.Exec('create table {}(name VARCHAR2(50),address VARCHAR2(50),age NUMBER )'.format(table_name))
            print('Create table {}'.format(table_name))
            time.sleep(0.5)


if __name__ == '__main__':
    """
    参数说明
        host 表示Oracle数据库的地址，可以是IP可以是计算机名（计算机名或者ScanIP需要能够解析）
        username/password 表示登录数据库的用户名和密码
        service_name 监听中的服务名
        tablespace_name 测试表空间
        datafile_path 测试表空间所在的物理位置
        size 测试表的物理文件大小
        max 测试数据中最大数据量

    过程说明：
        1、脚本根据提供的host username password service_name连接数据库，如果连接失败则会打印错误信息
        2、查询所有表空间，查找是否有测试表空间，如果有，则删除测试表空间
        3、根据提供的表空间名，测试物理文件位置，测试物理文件大小创建表空间
        4、在测试表空间中创建10个表，用于测试
        5、开始测试，测试过程如下（无限循环）
            A、查询归档日志空间，如果超过90%则停止写入数据
            B、随机取一张表，向表中插入随机数据，number/address为随机字符串，age为持续增量整数
            C、插入后查询，如果表中数据大于max限定，则删除此表，重新创建此表。
    """
    host = 'cyy12cscan.oracle.com'
    username = 'sys'
    password = 'infocore'
    service_name = 'ORCL'
    tablespace_name = 'test_tablespace'
    datafile_path = '+DATA/ORCL/DATAFILE/test.dbf'

    size = 10  # 单位GB
    max = 5000  # 每个测试数据表中最大数据量（单位:条）
    OracleDBTest(host, username, password, service_name, tablespace_name, datafile_path, size, max)
