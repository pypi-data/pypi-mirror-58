# from PyDataProc.DataTable import DataTable
# from PyDataProc.DataSource import DataSource
class DataRow():
    def __init__(self):
        self.fields = []
        self.columns = {}
        self.values = {}
        self.table  = None

    def set(self,field_name, value,**kwargs):
        if len(kwargs) == 0:
            if self.table == None:
                inkw = {"DataType":str(type(value))}
                self.set(field_name,value,**inkw)
            else:
                ## 在table中的row
                if self.table.contains(field_name):
                    inkw = {"DataType": self.table.get_fieldtype(field_name)}
                    self.set(field_name, value, **inkw)
                else:
                    print("Field name {field_name} is not contained its DataTable!".format(field_name = field_name))
        elif "DataType" in kwargs:
            name = field_name.lower()
            if name not in self.columns :
                self.columns[name] = kwargs.get("DataType")
            self.values[name] = value
            self.fields.append(name)


    def get_values(self):
        return  [ values for values in self.values.values()]
