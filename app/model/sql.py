import sqlite3
import json


class connect(object):

    def __init__(self, value=None):
        self.conn = sqlite3.connect('./app/database.db')
        self.cursor = self.conn.cursor()

    def PrepareConnection(self):
        return self.conn

    def QuerySelect(self):
        try:
            result = self.cursor.execute(
                'SELECT producers FROM dbase WHERE winner = "yes" ')
            return result.fetchall() 
        except:
            return '400'

    def WorstMmovieTreatment(self, lista):
        data = []
        red = []
        result_arr = []
        for i in range(len(lista)):
            result = self.cursor.execute(
                f'select MAX(dbase.year) AS maxyear, MIN(dbase.year) AS minyear, \
                    ( MAX(dbase.year) - MIN(dbase.year) ) as  total ,producers from dbase where winner = "yes" and producers LIKE "%{lista[i]}%"  ')
            r = result.fetchall()
            if r[0][2] != 0:
                result_arr = {
                    "producer": lista[i],
                    "interval": r[0][2],
                    "previousWin": r[0][1],
                    "followingWin": r[0][0]
                }
                data.append(result_arr)

        order = sorted(data, key=lambda k: k['interval'])
        red.append(['min', order[0], order[1] ])
        red.append(['max', order[-1], order[-2] ])

        return json.dumps(red, indent=4, sort_keys=False)
