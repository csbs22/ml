import pandas as pd
data = {
    'Fever':['Y','Y','N','Y','N'], 
    'Cough': ['Y','N','Y','Y','N'],
    'Throat Pain':['Y','Y','N','Y','N'],
    'Body Pain':['Y','Y', 'N','N','Y'],
    'Covid-19':['positive','positive','negative','positive','negative']
}
df = pd.DataFrame(data)
df.to_csv('covid.csv', index=False)
print("CSV file created successfully!")
import csv
a = [ ]
with open('covid.csv', 'r') as csvfile:
 for row in csv.reader(csvfile):
     a.append(row)
 print(a)
print ("\n The total no of training instances are : ", len(a)-1)
num_attribute = len(a[0])-1
print ("\n The initial hypothesis is : ")
hypothesis = ['0'] * num_attribute
print(hypothesis)
for i in range(1, len(a)):
 if a[i][num_attribute] == 'positive':
     for j in range(0, num_attribute):
         if hypothesis[j] == '0' or hypothesis[j] ==a[i][j]:
             hypothesis[j] = a[i][j]
         else:
             hypothesis[j] = '?'
 print ("\n The hypothesis for the training instance {} is : \n"
.format(i), hypothesis)
print("\n The final hypothesis is ")
print(hypothesis)