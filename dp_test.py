from Main_class import DataBase

class WorkWithDb(DataBase):

    def request_in_db(self):

        # name_table = 'cityes'
        # type_varcar = 'varchar(255)'
        # data_base.add_new_column(name_table, 'region', type_varcar)
        # select_all = "select * from cityes"
        # self..make_request_select(select_all)
        # print('---------------------------------------------------------------')

        list_field = ['id, ', 'name',]
        list_values = ['1, ', "'Azerot'"]
        self.add_field(list_field, list_values)


        order_by = 'SELECT * FROM cityes ' \
                   'ORDER BY id'
        self.make_request_select(order_by)

        test_query = ''

        # id = '5'
        # self.delete_field(id)
        # self.make_request_select(order_by)


WorkWithDb().request_in_db()




# import psycopg2 as p
#
# connection = p.connect(dbname='new_database',
#                        user='postgres',
#                        password='1111',
#                        host='localhost')
# cursor = connection.cursor()
# cursor.execute("select * from cities")
# # cursor.execute()
# for row in cursor:
#     print(row)
# # rows = cursor.fetchall()
# #
# # for field in rows:
# #     print(field)
