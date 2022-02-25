class Model:
    #List is used to hold on to results retrived by select(). Used in insert() to compare values being inserted as to not make an extra call to the database
    current_words = []

    def __init__(self, conn, curr):
        self.conn = conn
        self.curr = curr

    #Creates a string to create a new table. Columns will come in as a tuple to indicate any attribute they might have.
    def create_table(self, table_name, columns):
        try:
            query = 'CREATE TABLE IF NOT EXISTS %s (' % table_name
            for column in range(len(columns)):
                column_attr = ''

                for attribute in columns[column]:
                    column_attr += attribute + ' '

                if column + 1 == len(columns):
                    query += column_attr
                else:
                    query += column_attr + ', '

            query += ');'
            self.curr.execute(query)
            self.conn.commit()

        except:
            raise Exception('An error occured while trying to create a new table')
    
    #Retrives data from given table. Only able to take one column. Returns as a list
    def select(self, column, table):
        try:
            query = 'SELECT %s FROM %s' % (column, table)
            self.curr.execute(query)

            result = self.curr.fetchall()
            self.current_words = []

            for res in result:
                self.current_words.append(res[0])
            return self.current_words

        except:
            raise Exception('An error occured while trying to run SELECT')
    
    #Inserts given values into given table. Values are given as a list. Values that are already in the table cannot be inserted again.
    def insert(self, values, table):
        try:
            duplicated_word = False

            for value in values:
                if value not in self.current_words:
                    query = 'INSERT INTO %s VALUES(\'%s\');' % (table, value)
                    self.curr.execute(query)
                    self.conn.commit()
                else:
                    duplicated_word = True

            return duplicated_word
            
        except:
            raise Exception('An error occured while trying to run INSERT')

        