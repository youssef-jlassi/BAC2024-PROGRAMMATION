"""el activite el lola """
########## Importing library ##########
from numpy import array

########## Entry number of Pupils ##########
def Saisie():
    n = int(input('Enter the number of pupils: '))
    while not 1 <= n <= 25:
        n = int(input('Enter the number of pupils: '))
    return n

########## Fill array ##########
def Remplissage(n):
    PL = array([{}]*n)
    for i in range(n):
        PL[i] = {}
        print('Pupil N°',i+1,':')
        PL[i]['name'] = input('Name: ')
        
        PL[i]['avg'] = float(input('Average: '))
        while not 0 <= PL[i]['avg'] <= 20:
            PL[i]['avg']=float(input('Average: '))
        
        PL[i]['rank'] = int(input('Rank: '))
        while not 1 <= PL[i]['rank'] <= n:
            PL[i]['rank'] = int(input('Rank: '))
        
        PL[i]['obs'] = input('Observation: ')
       
        print('-'*20)
        
    return PL
        
########## Display ##########
def Affichage(PL,n):
    print('List of pupils having an average >= 10:')
    for i in range(n):
        if PL[i]['avg'] >= 10:
            print('Name:',PL[i]['name'])
            print('Average:',PL[i]['avg'])
            print('Rank:',PL[i]['rank'])
            print('Observation:',PL[i]['obs'])
            print('-'*20)

########## Main Program ##########
n = Saisie()
PL = Remplissage(n)
Affichage(PL,n)