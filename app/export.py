import pandas as pd
from app.model import sql


def csv():
    conn = sql.connect().PrepareConnection()
    path2 = './app/list.csv'
    
    df = pd.read_csv(path2, sep=';')
    rs = df.to_sql(name='dbase', con=conn, if_exists='replace')
   
    return rs

def treatment(value):
    if value is not None:
        data = []
        for i in value:
            data.append(i)

        names = []
        for sublist in data:
            for name in sublist:
                names += name.strip().split('and')

        sname = [name.strip().lstrip() for i in names for name in i.split(',')]
        
        return sname
