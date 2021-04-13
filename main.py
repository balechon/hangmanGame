import re
from unicodedata import normalize

def read_data(): 
    with open("./data/data.txt",'r',encoding='utf-8') as df:
        values=[word.rstrip('\n').replace('á','a') for word in df]
        values=removeAcent(values)
    return(values)

def removeAcent(value):
    return [val.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') for val in value]

def run():
    df=read_data()
    print(df)

if __name__=="__main__":
    run()
