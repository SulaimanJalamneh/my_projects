# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:32:08 2021

@author: sulaiman_noursy
"""
"""
import numpy as np
import pandas as pd
studentsNum=int(input('enter int number of students?'))

studentsInfo=[]
for x in range(studentsNum):
    studentsName=input('enter students info as Name?')
    studentsID=input('enter students info as ID?')
    studentsPhoneNum=input('enter students info as phoneNum?')
    studentsGrade=input('enter students info as Grade?')


    
    studentsInfo+=[[studentsName,studentsID,studentsPhoneNum,studentsGrade]]

print(studentsInfo)
results=pd.DataFrame(studentsInfo,columns=["NAME","ID","PHONENUM","GRADE"])
print(results)
"""

import numpy as np
import pandas as pd

n = eval(input('Enter the total numbers of students: '))
#DF=pd.DataFrame({"Name": Name, "ID": ID, "Phone_Num": Phone_Num, "Grade": Grade})
name=[]
Id=[]
Phone_num=[]
grade=[]

e=0
while e < n:
    Name= eval(input('Enter Student name: '))
    ID= eval(input('Enter Student id: '))         
    Phone_Num= eval(input('Enter Student phone number: '))
    Grade= eval(input('Enter Student grade: '))
    name+=[Name]
    Id+=[ID]
    Phone_num+=[Phone_Num]
    grade+=[Grade]
    
    e+=1

print(name)
print(Id)  
print(Phone_num)
print(grade) 
results ={"Name": name, "ID": Id, "Phone_Num": Phone_num, "Grade": grade}  
print(results) 
DF=pd.DataFrame(results)
print(DF)

"""
import numpy as np
import pandas as pd
ddd={"name":['sulaiman','mohammasd'],
     "id":[1,2],
     "grade":[89,78]
     
     }
df=pd.DataFrame(ddd)
print(df)

"""
