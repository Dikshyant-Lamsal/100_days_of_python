from prettytable import PrettyTable
from os import system
system('cls')
table = PrettyTable() 
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align['Pokemon Name']='l'
table.align['Type']='r'
print(table)