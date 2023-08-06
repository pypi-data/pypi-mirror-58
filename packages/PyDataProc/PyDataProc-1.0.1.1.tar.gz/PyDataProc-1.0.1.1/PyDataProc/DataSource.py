import os
import sys, pickle
import time
import re
import pymysql
import datetime
from pyhive import hive
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
import sqlite3
from PyDataProc.DataTable import DataTable
from  PyDataProc.Parameter import Parameter


class ConnType():
    mysql = "mysql"
    hive = "hive"
    presto = "presto"
    cache = "cache"
    temp = "temp"


class DataSource():
    # conn = None
    # cu = None
    # connection_name = ""
    # database_name = ""
    # connection = ""
    # # connection_name = ""
    # # database_name = ""
    # batchSQLs = []
    # batchValues = []
    # config文件默认引用位置
    config_default_path = '/azkaban/program_framework/mail'
    # 调用的脚本的路劲
    path = ''

    def __init__(self, connection_name, database_name=""):

        # 初始化变量
        self.conn_listmap = []
        self.conn = None
        # self.cur = None
        self.connection_name = connection_name
        self.database_name = database_name
        if connection_name == "":
            self.connection_name = "mysql_dev"
        # if database_name == "":
        #     self.database_name = "zichan360bi_ods"
        self.debug = False
        # connection = ""
        # connection_name = ""
        # self.database_name = ""
        self.batchSQLs = []
        self.batchValues = []
        self.conntype = "mysql"
        self.data_table = DataTable()
        # # config文件默认引用位置
        # self.config_default_path = '/azkaban/program_framework/mail'
        # # 调用的脚本的路劲
        # self.path = ''
        self.__batchSQLs = []
        self.__batch_values = []

    def setDebug(self, debug):
        self.debug = debug
        return self

    def setPath(self, path):
        self.config_default_path = path
        return self

    def getPath(self):
        os.getcwd()

    def getConfig(self):
        connection = {}
        # 获取连接串
        try:
            sys.path.insert(0, os.getcwd())
            import config
            connection = getattr(config, self.connection_name)
        except:
            try:
                sys.path.insert(0, self.config_default_path)
                import config
                connection = getattr(config, self.connection_name)
            except:
                print("The connection_name : " + self.connection_name + " is not exist!")
                sys.exit()
        finally:
            return connection

    def open(self):
        connection = self.getConfig()
        if self.connection_name not in self.conn_listmap:
            # 判断类型
            if 'dbtype' not in connection:
                print("Connection config must be dict,and dict must include key: dbtype!")
            else:
                connection = dict(connection)
                ##mysql类型数据库
                if connection['dbtype'].lower() == "mysql":
                    # 判断连接数据的必要信息是否具备
                    if 'host' not in connection or 'port' not in connection or 'user' not in connection or 'password' not in connection or 'db' not in connection or 'charset' not in connection:
                        print("Mysql connection dict must include key: (host,port,user,password,db,charset)! ")
                    else:
                        try:
                            if self.database_name == "":
                                db = connection['db']
                            else:
                                db = self.database_name
                            # 连接数据库
                            self.conn = pymysql.Connect(
                                host=connection['host'],
                                port=connection['port'],
                                user=connection['user'],
                                passwd=connection['password'],
                                db=db,
                                charset=connection['charset']
                            )
                            self.conn.autocommit(True)
                            self.conntype = ConnType.mysql
                            conn_map = {self.connection_name: self.conn}
                            self.conn_listmap.append(conn_map)
                            if self.debug: print("Connect to %s" % connection['host'])
                        except pymysql.Error as e:
                            print("CAN'T CONNECT TO MYSQL DATABASE: " + self.connection_name)
                            print("Error :%s" % e)
                            sys.exit()
                elif connection['dbtype'].lower() == "hive":
                    # 判断连接数据的必要信息是否具备
                    if 'host' not in connection or 'port' not in connection or 'user' not in connection or 'db' not in connection:
                        print("Hive connection dict must include key: (host,port,user,db)! ")
                    else:
                        try:
                            if self.database_name == "":
                                db = connection['db']
                            else:
                                db = self.database_name
                            # 连接数据库
                            self.conn = hive.connect(
                                host=connection['host'],
                                port=connection['port'],
                                username=connection['user'],
                                database=db,

                            )
                            self.conn.autocommit(True)
                            self.conntype = ConnType.hive
                            conn_map = {self.connection_name, self.conn}
                            self.conn_listmap.append(conn_map)
                            if self.debug: print("Connect to %s" % connection['host'])
                        except hive.Error as e:
                            print("CAN'T CONNECT TO Hive DATABASE: " + self.connection_name)
                            print("Error :%s" % e)
                            sys.exit()

                elif connection['dbtype'].lower() == "presto":
                    # 判断连接数据的必要信息是否具备
                    if 'host' not in connection or 'port' not in connection or 'user' not in connection or 'db' not in connection:
                        print("Hive connection dict must include key: (host,port,user,db)! ")
                    else:
                        try:
                            if self.database_name == "":
                                db = connection['db']
                            else:
                                db = self.database_name
                            # 连接数据库
                            self.conn = create_engine('presto://%s:%s/%s' % (
                                connection['host'], connection['port'], db))
                            self.conn.autocommit(True)
                            self.conntype = ConnType.presto
                            conn_map = {self.connection_name: self.conn}
                            self.conn_listmap.append(conn_map)
                            if self.debug: print("Connect to %s" % connection['host'])
                        except:
                            print("CAN'T CONNECT TO presto DATABASE: " + self.connection_name)
                            sys.exit()
                            # print("Error :%s" % e)

        return self

    def openSQLite(self, connection_type):
        # 连接数据库
        self.conn = sqlite3.connect(connection_type)
        if connection_type == ":memory:":
            self.conntype = ConnType.cache
        else:
            self.conntype = ConnType.temp
        if self.debug: print("Connect TO SQLite3: " + connection_type)
        return self

    def executeSQL(self, sql, *args):
        starttime = datetime.datetime.now()
        if self.debug: print(sql)
        # try:
        cursor = self.conn.cursor()
        if self.conntype == "mysql":
            num = cursor.execute(sql, *args)
        else:
            cursor.execute(sql)
            num = 0
        cursor.close()
        self.conn.commit()
        # except:
        #     sys.exit(1)
        endtime = datetime.datetime.now()
        time_diff = (endtime - starttime).seconds
        if self.debug: print("THE AFFECTED ROWS: %d ,use time %s's" % (num, time_diff))
        return self

    def  executeSQLs(self, SQLList):
        starttime = datetime.datetime.now()

        # try:
        cursor = self.conn.cursor()
        num = 0
        if self.conntype == "mysql":
            for sql in SQLList:
                if self.debug: print(sql)
                num = num + cursor.execute(sql)
        else:
            cursor.execute(sql)
        cursor.close()
        self.conn.commit()
        # except:
        #     sys.exit(1)
        endtime = datetime.datetime.now()
        time_diff = (endtime - starttime).seconds
        if self.debug: print("THE AFFECTED ROWS: %d ,use time %s's" % (num, time_diff))
        return self

    def excute_many_SQL(self, sql, datas):
        starttime = datetime.datetime.now()
        if self.debug: print(sql)
        # try:
        cursor = self.conn.cursor()
        if self.conntype == "mysql":
            num = cursor.executemany(sql,datas)
        else:
            cursor.execute(sql)
            num = 0
        cursor.close()
        self.conn.commit()
        # except:
        #     sys.exit(1)
        endtime = datetime.datetime.now()
        time_diff = (endtime - starttime).seconds
        if self.debug: print("THE AFFECTED ROWS: %d ,use time %s's" % (num, time_diff))
        return self

    def selectSQL(self, sql):
        starttime = datetime.datetime.now()
        if self.debug: print(sql)
        # try:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        table_record = cursor.fetchall()
        column = cursor.description
        column = [x[0] for x in column]
        cursor.close()
        self.conn.commit()
        # except:
        #     sys.exit(1)
        endtime = datetime.datetime.now()
        time_diff = (endtime - starttime).seconds
        if self.debug: print("THE AFFECTED ROWS: %d ,use time %s's" % (len(table_record), time_diff))
        return table_record, column

    def open_if_not(self):
        try:
            # 若ping通则返回0，否则报错
            self.conn.ping()
            # time.sleep(1)
            return true
        except:
            # print("Can't connection " + tuple(self.conn_listmap[-1].keys)[0])
            # sys.exit()
            return false

    def execute_datatable(self, sql):
        table: DataTable = DataTable()

        table_record, columns = self.selectSQL(sql)
        # self.data_table.columns_name = list(columns)

        for i in range(len(columns)):
            field_name = columns[i]
            # .is illegal char in SQLite and field name contains "." in hive columns
            if (field_name.find(".")):
                field_name = field_name[field_name.rfind(".") + 1:]
            if re.search("^[a-zA-Z_][a-zA-Z0-9_]*$", field_name) is None or table.contains(field_name):
                field_name = "column" + str(i)
            # println(meta.getColumnLabel(i) + ": " + meta.getColumnTypeName(i) + ", " + meta.getColumnClassName(i))
            table.add_field_with_label(field_name, field_name, str(type(field_name)))

        columns = table.get_fieldnames()

        for table_data in table_record:
            row = table.new_row()
            for i in range(len(table_data)):
                row.set(columns[i], table_data[i])
            table.insert(row)

        return table

    def use(self, DataBase):
        self.conn.executeSql("use " + DataBase)

    # def info(self):
    #     return connection_name, self.database_name

    def load(self):
        print(self.a)
        print(type(self.a))
        return self.a

    def table_update(self, SQL, table):
        count = -1

        if table.non_empty():
            if SQL.find("?") != -1:
                self.set_batch_command(SQL)
                for row in table.get_rows():
                    self.add_batch(tuple(row.get_values()))
                count = self.execute_batch_update()
            else:
                table_columns = table.get_columns()
                for row in table.get_rows():
                    SQL1 = Parameter().parameter_change(SQL, table_columns,row)
                    self.add_batch_command(SQL1)
                count = self.execute_batch_commands()
        return  count

    def set_batch_command(self, SQL):
        SQL =SQL.strip()
        if self.__batchSQLs != []:
            self.__batchSQLs = []
        if SQL.find("?"):
            SQL = SQL.replace("?", "%s")
        if SQL[-1] != ";":
            SQL = SQL + ";"
        self.__batchSQLs.append(SQL)

    def add_batch_command(self,SQL):
        SQL = SQL.strip()
        if SQL[-1] != ";":
            SQL = SQL + ";"
        self.__batchSQLs.append(SQL)

    def add_batch(self, values):
        self.__batch_values.append(values)

    def execute_batch_update(self):
        self.open_if_not()
        count = len(self.__batch_values)
        for i in range(count // 1000):
            self.excute_many_SQL(self.__batchSQLs[0], self.__batch_values[0:1000])
            del self.__batch_values[0:1000]
        if len(self.__batch_values):
            self.excute_many_SQL(self.__batchSQLs[0], self.__batch_values)
        self.__batchSQLs = []
        self.__batch_values = []
        return  count


    def execute_batch_commands(self):
        count = len(self.__batchSQLs)
        for i in range(count // 1000):
            self.executeSQLs(self.__batchSQLs[0:1000])
            del self.__batchSQLs[0:1000]
        if len(self.__batchSQLs):
            self.executeSQLs(self.__batchSQLs)
        # for i in range(count // 1000):
        #     print(" ".join(self.__batchSQLs[0:1000]))
        #     self.executeSQL(" ".join(self.__batchSQLs[0:1000]))
        #     del self.__batchSQLs[0:1000]
        # if len(self.__batchSQLs):
        #     self.executeSQL(" ".join(self.__batchSQLs))
        self.__batchSQLs = []
        self.__batch_values = []
        return count





