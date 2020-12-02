import pymysql
from decouple import config

class sql_class():
    def __init__(self): 
        host = config('SQLIP')
        port = int(config('SQLPORT'))
        user = config('SQLUSER')
        password = config('SQLPASS')
        database = config('SQLDATA')

        self.conn = pymysql.connect(host = host, port = port, user = user, password = password, database =database)
        self.cursor = self.conn.cursor()

    def get_user(self, user_name):
        '''
        docs go here but imn lazy
        '''
        sql = "SELECT `id` FROM users WHERE `name` = %s"

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, user_name)
        data = self.cursor.fetchall()
        if data:
            return data[0][0]
        else:
            return None
    
    def get_user_role(self, user_id):
        '''
        docs go here but imn lazy
        '''
        sql = "SELECT `role_id` FROM user_role WHERE `user_id` = %s"

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, user_id)
        data = self.cursor.fetchall()
        if data:
            return data[0]
        else:
            return None
    
    def get_role_user(self, role_id):
        '''
        docs go here but imn lazy
        '''
        sql = "SELECT `user_id` FROM user_role WHERE `role_id` = %s"

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, role_id)
        data = self.cursor.fetchall()
        if data:
            return data[0]
        else:
            return None

    def add_user(self, user_id, name):
        '''
        docs go here but imn lazy
        '''
        sql = 'INSERT INTO users (`id`, `name`) VALUES (%s,%s)'

        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, (user_id, name))
            self.conn.commit()
        except  Exception as exc:
            self.conn.rollback()
            print(str(exc))