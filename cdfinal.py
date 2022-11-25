#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:28:35 2022

@author: amitkumar
enrollment number : BT20HCS186
"""

from prettytable import PrettyTable

num_Nonterminals = int(input("Enter the number of non- terminals: "))
nonTer = []
print("Enter the non- terminals: \n")
for i in range(0,num_Nonterminals):
    nonTer.append(input(f"{i+1}. : "))
   


num_Terminals = int(input("Enter the number of terminals: "))
ter = []
print("Enter the terminals: \n")
for i in range(0,num_Terminals):
    ter.append(input(f"{i+1}. : "))

ter.append('$')
num_Terminals +=1

num_items = int(input("Enter the number of LR(1) items your grammar will have: "))



lr1_items = []
gotos = []
shifts = []

for i in range(0, num_items):
    items_coll = []
    goto_coll = []
    shifts_coll = []
   
    num_prod = int(input(f"Enter the number of production rules in your I{i} state: "))
   
    print("Enter productions with their look ahead separated by , from the production: ")
    print("eg: A -> .aA,a|b  -- The right Hand side of the production must not have a space between any symbol\n  ")
   
    print("Enter ")
    for j in range(0, num_prod):
        items_coll.append(input(f"member{j+1}: "))
       
    lr1_items.append(items_coll)
   
   
    print(f"Enter the shift states for item I{i}: \n")
    print("## Press blank space if it doesnot go anyhere on scanning the terminal asked##")
   
    for j in range(0, num_Terminals):
        ans = input(f"On scanning {ter[j]} : ")
        shifts_coll.append(f"{ter[j]}:{ans}")
   
    shifts.append(shifts_coll)
   
    print(f"Enter the goTo states for item I{i}: \n")
    print("## Press space if it doesnot go anyhere on scanning the non -terminal asked##")
   
    for j in range(0, num_Nonterminals):
        ans = input(f"On scanning {nonTer[j]} : ")
        goto_coll.append(f"{nonTer[j]}:{ans}")
   
    gotos.append(goto_coll)
       
   
   
columns = [' '] + ter + nonTer
   
myTable = PrettyTable(columns)


for i in range(0, num_items):
   
    row = [f"I{i}"]
   
    for j in range(0, num_Terminals):
        if(shifts[i][j][2] != " "):
            row.append("s" + ((shifts[i])[j][2]))
        else:
            row.append(" ")
    for j in range(0, num_Nonterminals):
        row.append(gotos[i][j][2])
       
   
    for j in range(0, len(lr1_items[i])):
        string = ""
        for k in range(0, len(lr1_items[i][j])):
            if(lr1_items[i][j][k] == '.' and lr1_items[i][j][k +1] == ','):
                string = lr1_items[i][j][:k]
                break
        k = k+2
        while(k< len(lr1_items[i][j])):
            if(lr1_items[i][j][k] != '|'):
                symbol = lr1_items[i][j][k]
               
                for m in range(0, num_Terminals ):
                    if(ter[m] == symbol):
                        break
                if(row[m+1] == " "):
                    row[m+1] = "reduce: " + string
                else:
                    row[m+1] = row[m+1] + " , " + "r: " + string
               
            k +=1
           
    if(i == 1):
        row[num_Terminals] += " -- ACCEPT"
           
    myTable.add_row(row)

print("\nThe CLR(1) parsing table corresponding to the following set of canonical collections is: \n")
print(myTable)

