# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:00:47 2019

@author: Administrator
"""

import xlrd

rubbish = [] 

def read(file = r'F:\read.xlsx',sheet_index = 0):
    print('\n')
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(sheet_index)
    
    for i in range(0,sheet.nrows):
        rubbish.append(sheet.row_values(i))

read()
def rubbishMeau(): 
    print('^'*50) 
    print('     Garbage classification query system3.0        ') 
    print(" ")
    print('        0、Test')
    print('        1、View')                 
    print('        2、Increase')              
    print('        3、Exit') 
    print('^'*50) 

def show():
    print("-"*20)
    for i in range(0,len(rubbish)):
        print('    ' + rubbish[i][0] + '  ' + rubbish[i][1])
    print('-'*20 + '\n')
def add(): 
    rubbishInf = []
    name = input('\n   Please enter the name of the trash to be added：') 
    rubbishInf.append(name)
    rubtype = input('\n   Please define the type of garbage：')
    rubbishInf.append(rubtype)
    print('\n   Added successfully\n')
    rubbish.append(rubbishInf)  

rubbishMeau()

while True: 
    # rubbishMeau() 
    choice = int(input("\n   Please enter the number：")) 
    if choice == 0: 
        show() 
    elif choice == 1: 
        # inquire()
        show()
    elif choice == 2:
        add()
    elif choice == 3: 
        print('\n   Thank you for using！\n') 
        break
    else: 
        print('\n   Incorrect input, please enter a number：1、2、3  \n') 