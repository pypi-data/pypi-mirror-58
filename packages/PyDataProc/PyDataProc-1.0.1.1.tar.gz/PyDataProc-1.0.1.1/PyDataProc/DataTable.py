from PyDataProc.DataRow import DataRow


class DataTable():
    def __init__(self):
        # self.columns_name = []
        self.__columns = {}
        self.__labels = {}
        self.__rows = []

    def add_field(self):
        pass

    def contains(self, field_name):
        return field_name.lower() in self.__columns

    def get_fieldtype(self, field_name):
        return self.__columns[field_name.lower()]

    def add_field_with_label(self, field_name, label_name, datatype):
        if field_name.find(".") >= 0:
            name = field_name[field_name.rfind(".") + 1:]
        else:
            name = field_name
        name = name.lower()
        self.__columns[name] = datatype
        self.__labels[name] = label_name

    def get_fieldnames(self):
        return [column for column in self.__columns]

    def new_row(self):
        row = DataRow()
        row.columns = self.__columns
        row.table = self
        return row

    def insert(self, row):
        self.__rows.append(row)
        return self

    def merge(self,otherTable):
        self.union(otherTable)
        otherTable.clear()
        return self

    def union(self, otherTable):
        # a= otherTable.get_rows()
        self.__rows  +=  otherTable.get_rows()
        self.__columns.update(otherTable.get_columns())
        self.__labels.update(otherTable.get_labels())
        return self

    def get_rows(self):
        return  self.__rows

    def get_columns(self):
        return  self.__columns

    def get_labels(self):
        return  self.__labels


    def count(self):
        return  len(self.__rows)

    def clear(self):
        self.__columns = {}
        self.__labels = {}
        self.__rows = []
        return self

    def show(self,num):
        if num > len(self.__rows):
            num = len(self.__rows)
        print("------------------------------------------------------------------------")
        print(str(len(self.__rows))+ " ROWS")
        print("------------------------------------------------------------------------")
        print(" ,".join(str(i) for i in self.__columns.keys()))
        for row in self.__rows[0:num]:
            print(row.get_values())
        print("------------------------------------------------------------------------")
        return self

    def is_empty(self):
        if len(self.__rows) == 0:
            return True
        else:
            return  False

    def non_empty(self):
        if len(self.__rows) == 0:
            return False
        else:
            return  True

    def get_rows(self):
        return self.__rows