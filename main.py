import random
import os
import time

def read_data(): 
    with open("./data/data.txt",'r',encoding='utf-8') as df:
        values=[word.rstrip('\n').upper() for word in df]
        values=removeAcent(values)
    return(values)

def removeAcent(value):
    return [val.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') for val in value]


def startGame(data):
    randomWord=random.choice(data)
    # print(randomWord)
    word=[letter for letter in randomWord]
    playerWord=['_' for _ in randomWord]

    while word !=playerWord:
        print('Adivina la Palabra')
        printList(playerWord)
        try:
            choice=input('Escoge una letra: ')
            if choice.isnumeric():
                raise ValueError('Numbers are not allowed')
                
            for i in range(0,len(word)):
                if word[int(i)]==choice.upper():
                    playerWord[int(i)]= choice.upper()
            os.system('clear')
        except ValueError as ve:
            os.system('clear')
            print(f'  ****** Error: {ve} *******')
            
            time.sleep(2.5)
            os.system('clear')
    print(f'*******GANASTE**** la palabra era {randomWord}')

def printList(mylist):
    for i in mylist:
        print(i, end=" ")
    print('\n')

def run():
    df=read_data()
    startGame(df)

if __name__=="__main__":
    run()
