# object DataHub:
#     def Qross = DataHub()
import datetime
import os
import random

from PyDataProc.DataSource import DataSource
from PyDataProc.DataTable import DataTable
from PyDataProc.FileUtil import Excel
from PyDataProc.PyEmail import PyEmail


class PyDataHub():

    # SOURCES = {"DEFAULT":DataSource()}
    def __init__(self, default_connection_name=""):
        self.debug = True
        self.__SOURCE = {"DEFAULT": DataSource(default_connection_name).open()}
        self.__CURRENT_conn = self.__SOURCE["DEFAULT"]
        self.__TARGET_conn = self.__SOURCE["DEFAULT"]

        # 初始化变量
        # self.DEBUG = True
        # self.conn = None
        self.__TABLE = DataTable()
        self.__COUNT = 0
        self.__TOTAL = 0
        self.__Email = PyEmail()

    def open(self, connection_name=""):
        # self.conn = self.Source.open(connection_name).conn
        if connection_name in self.__SOURCE:
            if self.__SOURCE[connection_name].open_if_not():
                self.__CURRENT_conn = self.__SOURCE[connection_name]
            else:
                self.__SOURCE[connection_name] = DataSource(connection_name).open()
                self.__CURRENT_conn = self.__SOURCE[connection_name]
        else:
            self.__SOURCE[connection_name] = DataSource(connection_name).open()
            self.__CURRENT_conn = self.__SOURCE[connection_name]
        return self

    def openCache(self):
        # self.conn = self.Source.openSQLite(":memory:").conn
        connection_name = "CACHE"
        if connection_name in self.__SOURCE:
            if self.__SOURCE[connection_name].open_if_not():
                self.__CURRENT_conn = self.__SOURCE[connection_name]
            else:
                self.__SOURCE[connection_name] = DataSource(connection_name).openSQLite(":memory:")
                self.__CURRENT_conn = self.__SOURCE[connection_name]
        else:
            self.__SOURCE[connection_name] = DataSource(connection_name).openSQLite(":memory:")
            self.__CURRENT_conn = self.__SOURCE[connection_name]
        return self

    def openTemp(self):
        templite = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 99999999)).zfill(8)
        connection_name = "CACHE"
        if connection_name in self.__SOURCE:
            if self.__SOURCE[connection_name].open_if_not():
                self.__CURRENT_conn = self.__SOURCE[connection_name]
            else:
                self.__SOURCE[connection_name] = DataSource(connection_name).openSQLite(templite)
                self.__CURRENT_conn = self.__SOURCE[connection_name]
        else:
            self.__SOURCE[connection_name] = DataSource(connection_name).openSQLite(templite)
            self.__CURRENT_conn = self.__SOURCE[connection_name]
        return self

    def close(self):
        # self.conn.execute(sql)
        try:
            self.__CURRENT_conn.close()
            self.__TARGET_conn.close()
            # while len(self.__SOURCE) :
            #     self.__SOURCE


        except Exception as e:
            print(e)

    def execute(self, sql):
        self.__CURRENT_conn.executeSQL(sql)

    def select(self, sql):
        # res = self.Source.cacheSelectSQL(sql)
        return self.__CURRENT_conn.selectSQL(sql)

    def debugs(self, enabled):
        self.debug = enabled
        self.__CURRENT_conn.setDebug(enabled)
        return self

    def debugging(self):
        return self.debug
        # return self

    # def openCache(self):
    #     self.reset()
    #
    #
    #
    # def reset(self):
    #     pass

    # 清除数据
    def reset(self):
        return self

    def get(self, select_SQL):
        self.reset()
        if self.debug:
            print(select_SQL)

        self.__TABLE.merge(self.__CURRENT_conn.open().setDebug(False).execute_datatable(select_SQL))
        self.__TOTAL += self.__TABLE.count()
        self.__COUNT = self.__TABLE.count()
        # print(self.__TOTAL)
        return self

    def get_table(self):
        return self.__TABLE

    def get_rows(self):
        return self.__TABLE.get_rows()

    def put(self, non_querySQL):
        if self.debug:
            self.__TABLE.show(10)
        if self.debug:
            print(non_querySQL)
        if self.__TABLE.non_empty():
            self.__TARGET_conn.open().setDebug(False).table_update(non_querySQL, self.__TABLE)

    '''
        comm：   查询后的数据直接保存成excel文件 
        author:  chongmengzhao
        time:    2019年10月24日11:15:16
        param:   values[元组类型(保存后的文件路径，保存后的sheet名称)]   
    '''

    def saveExcel(self, *values):
        if len(values) == 2:
            Excel(values[0], values[1], self.__TABLE.get_rows(), self.__TABLE.get_fieldnames())
        if len(values) == 3:
            Excel(values[0], values[1], self.__TABLE.get_rows(), self.__TABLE.get_fieldnames(), values[2])
        if len(values) == 1:
            Excel(values[0], "Sheet1", self.__TABLE.get_rows(), self.__TABLE.get_fieldnames())

    '''
        comm：   创建excel文件 
        author:  chongmengzhao
        time:    2019年10月24日11:15:16
        param:   va[元组类型(文件路径,Sheet名称)]        
    '''

    def createExcel(self, *va):
        self.Excel = Excel.createFile(Excel(), va)

    '''
        comm：   添加excel文件标题 
        author:  chongmengzhao
        time:    2019年10月24日11:15:16
        param:   titles[元组类型(字段1，字段2，字段3，……)]        
    '''

    def addTitle(self, row_index=1, column_index=1, *titles):
        if self.Excel is not None:
            if self.Excel.suffixName == ".xls":
                print("开始追加03标题")
                self.Excel.addTitle03(row_index, column_index, titles)
            if self.Excel.suffixName == ".xlsx":
                print("开始创建07标题")
                self.Excel.addTitle07(row_index, column_index, titles)
        else:
            print("未创建指定文件")

    '''
        comm：   excel文件数据追加 
        author:  chongmengzhao
        time:    2019年10月24日11:15:16
        param:   row[元组类型([DataRow])]        
    '''

    def append(self, row_index=2, column_index=1, threadNum=4, *row):
        if self.Excel is not None:
            if self.Excel.suffixName == ".xls":
                print("开始追加03标题")
                self.Excel.append03(row_index, column_index, threadNum, row)
            if self.Excel.suffixName == ".xlsx":
                print("开始创建07标题")
                self.Excel.append07(row_index, column_index, threadNum, row)
        else:
            print("未创建指定文件")

    '''
        comm：   查询数据追加到指定模板 
        author:  chongmengzhao
        time:    2019年10月24日11:15:16
        param:   template_dir   模板路径
                 row_index      开始行索引
                 column_index   开始列索引      
    '''

    def to_template(self, template_dir, row_index=2, column_index=1, threadNum=4):
        self.Excel = Excel()
        self.Excel.to_template(template_dir, self.__TABLE.get_rows(), self.__TABLE.get_fieldnames(), row_index,
                               column_index, threadNum)

    def write_email(self,subject):
        self.__Email.WriteEmail(subject)
        return  self

    def attach(self,attachs):
        self.__Email.attach(attachs)
        return  self

    def write_email_content(self,mail_content):
        self.__Email.setEmailContent(mail_content)
        return self

    def to(self,*to):
        self.__Email.to(*to)
        return  self

    def cc(self,*cc):
        self.__Email.cc(*cc)
        return self

    def bcc(self,*bcc):
        self.__Email.bcc(*bcc)
        return self

    def send(self):
        self.__Email.send()
        return self




# def put(nonQuerySQL: String): DataHub = {
#
#         if (DEBUG) {
#             TABLE.show(10)
#             println(nonQuerySQL)
#         }
#
#         if (TABLE.nonEmpty) {
#             TARGET.tableUpdate(nonQuerySQL, TABLE)
#         }
#
#         if (pageSQLs.nonEmpty || blockSQLs.nonEmpty) {
#             stream(table => {
#                 TARGET.tableUpdate(nonQuerySQL, table)
#                 table.clear()
#             })
#         }
#
#         TO_BE_CLEAR = true
#
#         this
#     }
