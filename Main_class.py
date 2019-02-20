import psycopg2 as p


class DataBase:
    def __init__(self):
        self.connection = p.connect(dbname='new_database',
                              user='postgres',
                              password='1111',
                              host='localhost')
        self.cursor = self.connection.cursor()

    def complete_the_request(self, request_string):
        try:
            self.cursor.execute(request_string)
            self.connection.commit()
            for row in self.cursor:
                print(row)
            print('Your query is done! Good luck and have nice day.')
        except Exception:
            print('Your request has not been completed!')

    def add_new_column(self, name_table, name_column, type):
        add_column = 'ALTER TABLE' + ' ' + name_table + ' ' + 'ADD COLUMN IF NOT EXISTS' + ' ' + name_column + ' ' + type
        print(add_column)
        self.cursor.execute(add_column)
        self.connection.commit()

    def add_field(self, list_name_field, list_values, table_name='cityes'):
        """
        :param list_name_field: one or few name for field, what need add in table
        :param list_values: one or faw values for field what need add in table
        :param table_name: name of the table, where you add new field
        """
        if len(list_name_field) == len(list_values):
            print('Data is valid! All is all right')
        else:
            print('Ups!!! It looks like you are transmitting a different number of parameters. Check that and try again.')

        str_field = ''
        for name_field in list_name_field:
            str_field += name_field

        str_values = ''
        for values in list_values:
            str_values += values

        add_field = 'INSERT INTO ' + table_name + '(' + str_field + ')' + ' values' + '(' + str_values + ')'
        self.cursor.execute(add_field)
        self.connection.commit()
        print('Field is added! Good luck and have nice day')

    def delete_field(self,  id, table_name='cityes'):
        delete_field = 'DELETE FROM ' + table_name + ' WHERE id = ' + id
        self.cursor.execute(delete_field)
        self.connection.commit()


