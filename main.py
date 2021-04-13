import random
import os
import time

def read_data(): 
    with open("./data/data.txt",'r',encoding='utf-8') as df:
        values=[word.rstrip('\n').upper() for word in df]
        values=removeAcent(values)
    return(values)

def removeAcent(value):
    return [val.replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U') for val in value]


def startGame(data, attemps):
    randomWord=random.choice(data)
    # print(randomWord)
    word=[letter for letter in randomWord]
    playerWord=['_' for _ in randomWord]

    while attemps != 0:
        print("""
           _    _  ____  _____    _____          _____   ____  
     /\   | |  | |/ __ \|  __ \  / ____|   /\   |  __ \ / __ \ 
    /  \  | |__| | |  | | |__) |  |       /  \  | |  | | |  | |
   / /\ \ |  __  | |  | |  _  / | |      / /\ \ | |  | | |  | |
  / ____ \| |  | | |__| | | \ \ | |____ / ____ \| |__| | |__| |
 /_/    \_\_|  |_|\____/|_|  \_\ \_____/_/    \_\_____/ \____/ 
                                                                                                 
        ////////////////////////////////////////           
        /#    *@                              ##                     
        /#  *@,                               ##            
        /#*@.                                 ##                       
        /#                                 *@ @ @.           
        /#                               .@*      /@.       
        /#                               @.        .@       
        /#                               @*        /&       
        /#                                /@     /@/                                
        /#                                   @@@@          
        /#                                 @/ %@ \@        
        /#                                @/  %@  \@                 
        /#                                    %@           
        /#                                   @  @          
        /#                                  @    @          
        /#                                 @      @              
        /#                                  
/#/#/#/#/#/#/#/#/#/#/#                                                                                   
                                                              """)



        print("\n")
        print('Palabra:', end=" ")
        printList(playerWord)
        try:
            print(f'Intentos Restantes: {attemps}')
            choice=input('Escoge una letra: ')
            if choice.isnumeric():
                raise ValueError('No se puede ingresar numeros')
            if len(choice)>1:
                raise ValueError('Solo una Letra o Vocal')

            for idx, _ in enumerate(word):
                if word[idx]==choice.upper():
                    playerWord[idx]= choice.upper()
            os.system('clear')
            attemps-=1
        except ValueError as ve:
            os.system('clear')
            print(f'  ****** Error: {ve} *******')
            time.sleep(2)
            os.system('clear')

    printList(playerWord)

    newWord=input('Escribe la Palabra: ')
    if newWord.upper()==randomWord:
        print("""
   _____          _   _           _____ _______ ______ 
  / ____|   /\   | \ | |   /\    / ____|__   __|  ____|
 | |  __   /  \  |  \| |  /  \  | (___    | |  | |__   
 | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __|  
 | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____ 
  \_____/_/    \_\_| \_/_/    \_\_____/   |_|  |______|
                                                                                                          
        """)
        print(f'La palabra era {randomWord}')
    else:
        print("""
  ______      _      _                _____ _______ ______ 
 |  ____/\   | |    | |        /\    / ____|__   __|  ____|
 | |__ /  \  | |    | |       /  \  | (___    | |  | |__   
 |  __/ /\ \ | |    | |      / /\ \  \___ \   | |  |  __|  
 | | / ____ \| |____| |____ / ____ \ ____) |  | |  | |____ 
 |_|/_/    \_\______|______/_/    \_\_____/   |_|  |______|
                                                           
        """)
        print(f'La palabra era {randomWord}')
    
def printList(mylist):
    for i in mylist:
        print(i, end=" ")
    print('\n')

def run():
    df=read_data()
    attemps= 8
    while True:
        startGame(df,attemps)
        print("""
 __      __   _                               _                      ___  
 \ \    / /  | |                             | |                    |__ \ 
  \ \  / /__ | |_   _____ _ __    __ _       | |_   _  __ _  __ _ _ __ ) |
   \ \/ / _ \| \ \ / / _ \ '__|  / _` |  _   | | | | |/ _` |/ _` | '__/ / 
    \  / (_) | |\ V /  __/ |    | (_| | | |__| | |_| | (_| | (_| | | |_|  
     \/ \___/|_| \_/ \___|_|     \__,_|  \____/ \__,_|\__, |\__,_|_| (_)  
                                                       __/ |              
                                                      |___/   
        """)
        repeat=input("Si/No:  ")
        if repeat.upper() =="NO":
            break



if __name__=="__main__":
    run()
