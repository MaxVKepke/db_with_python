from Main_class import DataBase


class MakeAnyQuery(DataBase):

    def create_table(self):
        create_regions = 'CREATE TABLE IF NOT EXISTS regions (id SERIAL PRIMARY KEY, name VARCHAR(255) UNIQUE NOT NULL, active BOOLEAN NOT NULL DEFAULT TRUE);'
        self.do_any_query(create_regions)


        create_cities = 'CREATE TABLE IF NOT EXISTS cities (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL, region_id INT NOT NULL, active BOOLEAN NOT NULL DEFAULT TRUE, FOREIGN KEY (region_id) REFERENCES regions(id));'
        self.do_any_query(create_cities)

    def add_field_in_tables(self):
        table = 'regions'
        add_field_in_regions = ['name']
        add_values = ["'Middle earth'"]
        self.add_field(add_field_in_regions, add_values, table)
        table = 'regions'
        add_field_in_regions = ['name']
        add_values = ["'Cool cities'"]
        self.add_field(add_field_in_regions, add_values, table)

        select_from_regions = 'SELECT * FROM regions;'
        self.make_request_select(select_from_regions)

        add_field_in_sities = ['name, ', 'region_id']
        add_values = ["'Mordor',", ' 1']
        self.add_field(add_field_in_sities, add_values)
        add_field_in_sities = ['name, ', 'region_id']
        add_values = ["'Rohan',", ' 1']
        self.add_field(add_field_in_sities, add_values)
        add_field_in_sities = ['name, ', 'region_id']
        add_values = ["'Azerot',", ' 2']
        self.add_field(add_field_in_sities, add_values)
        add_field_in_sities = ['name, ', 'region_id']
        add_values = ["'Atlantida',", ' 2']
        self.add_field(add_field_in_sities, add_values)
        add_field_in_sities = ['name, ', 'region_id']
        add_values = ["'Gotem',", ' 2']
        self.add_field(add_field_in_sities, add_values)

        select_from_cities = 'SELECT * FROM cities;'
        self.make_request_select(select_from_cities)


MakeAnyQuery().create_table()

MakeAnyQuery().add_field_in_tables()
