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

    '''
    Uses table "fuck_leaderboard" with fields "user_id", "guild_id" and "fuck_count", in that order.
    '''

#######################################

    def update_fuck_leaderboard(self, user_id, guild_id):
        '''
        Checks if user has a record in specified server then:
            *Updates record if one is found
            *Creates a record if nots
        '''
        # move update into a try command and have it run the command in a try
        #checks if a record exists
        sql = 'SELECT fuck_count FROM fuck_leaderboard WHERE user_id = %s and guild_id = %s'

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, user_id, guild_id)
        data = self.cursor.fetchall()
        if data: 
            #updates the record if one is found
            fuck_count = data[0][0]
            sql = 'UPDATE fuck_leaderboard SET fuck_count = %s WHERE user_id = %s and guild_id = %s'

            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, fuck_count, user_id, guild_id)
            data = self.cursor.fetchall()
        else: # move insert into a try command and have it run the command in a try
            #creates a record if no record is found
            sql = 'INSERT INTO fuck_leaderboard VALUES (%s, %s, %s)'

            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, user_id, guild_id, 1)
            data = self.cursor.fetchall()

#######################################

    def get_fuck_leaderboard(self, guild_id, from_record=0, record_count=5):
        '''
        Fetches the leaderboard of fuck.
        from_record used to define from which record the function will return.
        record_count used to define how many records to return.
        '''

        sql = 'SELECT user_id, SUM(fuck_count) AS total_fucks FROM fuck_leaderboard WHERE guild_id = %s GROUP BY user_id ORDER BY fuck_count DESC'
        
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, guild_id)
        data = self.cursor.fetchall()
        if data:
            return data[from_record: record_count + 1]
        else:
            return None

#######################################

    def get_user_fuck(self, user_id, guild_id):
        '''
        Fetches a user's fuck count.
        If guild_id is set to 0 function will return a global count.
        '''

        if guild_id:
            sql = 'SELECT SUM(fuck_count) AS total_fucks FROM fuck_leaderboard WHERE user_id = %s and guild_id = %s GROUP BY user_id'
        else:
            sql = 'SELECT SUM(fuck_count) AS total_fucks FROM fuck_leaderboard WHERE user_id = %s GROUP BY user_id'

        self.conn.ping(reconnect=True)
        if guild_id:
            self.cursor.execute(sql, user_id, guild_id)
        else:
            self.cursor.execute(sql, user_id)
        data = self.cursor.fetchone()
        if data:
            return data
        else:
            return None
