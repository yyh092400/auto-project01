
from quote.db.dbhandle import DbHandle


class DbCustomer:

    def __init__(self):
        self.dbhandle = DbHandle('localhost', 'root', '123456', 'quote', 3306)


    def delete_customer(self,customer_no):
        self.dbhandle.update_data('delete from tb_customer where customerNo=%s',[customer_no])


    def search_customer(self,customer_no):
        return self.dbhandle.search_data('select * from tb_customer where customerNo=%s',[customer_no])

    def add_cus_data_one(self,customer_no):
        lst=[]
        res = self.search_customer(customer_no)
        for tup_o in res:
            for v in tup_o:
               if v != '':
                   lst.append(v)
        lst.sort()
        return lst

# db = DbCustomer()
# print(db.add_cus_data_one('c004'))