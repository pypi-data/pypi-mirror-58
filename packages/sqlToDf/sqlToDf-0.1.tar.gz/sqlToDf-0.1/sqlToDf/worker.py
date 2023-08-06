from subprocess import call
class bcp_package:
    def __init__(self, query="SELECT * FROM charge", directory=''
                 , host='127.0.0.1', username='SA', password='abc$12345', coldelim=',', rowdelim='\n',
                 database='testing', table='charge'):
        directory = directory + table + '.txt'
        self.query = query
        self.dir = directory
        self.host = host
        self.user_name = username
        self.password = password
        self.col_delim = coldelim
        self.row_delim = rowdelim
        self.database_name = database
        self.table_name = table

    def fetch_in_txt(self):
        call(['bcp', self.query, 'queryout', self.dir, '-t', self.col_delim,'-c', '-S', self.host, '-d', self.database_name, '-U', self.user_name, '-P', self.password])

if __name__=='__main__':
    instance = bcp_package(query='Select * from charge',directory='',coldelim='/',password='abc$12345')
    instance.fetch_in_txt()
