import sqlite3

class connect(object):

    def __init__(self, value=None):
        self.conn = sqlite3.connect('./app/database.db')
        self.cursor = self.conn.cursor()

    def PrepareConnection(self):
        return self.conn

    def QuerySelect(self):
        try:
            result = self.cursor.execute('SELECT producers FROM dbase WHERE winner = "yes" ')
            return result.fetchall()
        except:
            return '400'

    def WorstMmovieTreatment(self, lista):
        data = []
        red = []
        for i in range(len(lista)):
            result = self.cursor.execute(
                f'select MAX(dbase.year) AS maxyear, MIN(dbase.year) AS minyear, \
                    ( MAX(dbase.year) - MIN(dbase.year) ) as  total ,producers from dbase where winner = "yes" and producers LIKE "%{lista[i]}%"  ')
            r = result.fetchall()
            if r[0][2] != 0:
                result = {
                    'producer': lista[i],
                    'interval' : r[0][2],
                    'previousWin': r[0][1],
                    'followingWin': r[0][0]
                }
                data.append(result)
       
        flist = list(data)
        r = sorted(flist, key=lambda k: k['interval'])
        rcount = len(r)
        red.append(['min', r[0], r[1]])
        red.append(['max', r[rcount-1], r[rcount-2]])
        return red
