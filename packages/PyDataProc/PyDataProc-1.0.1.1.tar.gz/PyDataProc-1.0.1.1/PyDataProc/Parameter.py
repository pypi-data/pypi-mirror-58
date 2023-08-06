"""DataSource 解析sql的参数类
        """
import re


class Parameter():
    def __init__(self):
        self.__PARAMETER = """(^|[^#&])((#|&)\(?([a-zA-Z0-9_]+)\)?)"""

    def test(self, str):
        rs = re.compile(self.__PARAMETER)
        match = rs.findall(str)
        if len(match):
            return True
        else:
            return False

    def check(self, type, value):
        if type == "<class 'datetime.datetime'>" or type == "<class 'str'>":
            return "'%s'" % value
        else:
            return '%s' % value

    def get_default_value(self, type):
        if type == "<class 'datetime.datetime'>":
            return '0000-00-00 00:00:00'
        elif type == "<class 'str'>":
            return ''
        elif type == "<class 'int'>":
            return '0'
        else:
            return ''

    def parameter_change(self, sql, columns, row):
        fields = [i for i in columns.keys()]
        values = row.values
        for i in range(len(fields)):
            keywords1 = '#' + fields[i]
            keywords2 = '&' + fields[i]

            if fields[i] in values:
                value = str(values[fields[i]])
            else:
                value = self.get_default_value(columns[fields[i]])

            if sql.find(keywords1) != -1:
                sql = sql.replace(keywords1, value)

            if sql.find(keywords2) != -1:
                sql=sql.replace(keywords2, self.check(columns[fields[i]], value))
        return sql
