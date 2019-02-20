from Main_class import DataBase

class JoinTables(DataBase):
    def left_join(self):
        # request = 'CRATE TABLE regions (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NUL UNIQUE, active BOOLEAN NOT NULL DEFAULT TRUE);'
        request = 'select * from regions;'
        print(request)
        self.complete_the_request(request)

JoinTables().left_join()
