
import xlrd

class OperationExl:

    def __init__(self,path=None,sheet_name=None):

        if path == None:
            path = '../../../config/AutoCase.xls'

        if sheet_name == None:
            sheet_name ='登录用例参数'

        with xlrd.open_workbook(path) as workbook:
            self.data = workbook.sheet_by_name(sheet_name)


    def get_rows(self):
        return  self.data.nrows


    def get_cols(self):
        return  self.data.ncols

    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)