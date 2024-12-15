from random import randint
import string


student=[
    {
    'name':'',
    'weight_first':0.0,
    'weight_last':0.0,
    'weight_diff':0.0
    }
    for _ in range(30)
    ]


def measure_weight():
    shift=input('enter shift(firstday/lastday) : ').lower()
    if shift=='firstday':
        first_input()
        print('\n\nenter weight on last day: \n')
        last_input()
    elif shift=='lastday':
        print('!!! firstly enter record of first term !!! \n!!!     empty records     !!!')
        return
    
def first_input():
      for i in range(30):
        print('  *** student record no '+str(i+1)+' ***')
        student[i]['name']=input('  enter student name : ')
        student[i]['name']+=str(randint(1,30)%(i+1))
        student[i]['weight_first']=round(float(input('  enter weight (kg) : ')),1)
        print('       ***  record ended  ***\n')
def last_input():
    for j in range(30):
       print('  *** student record no '+str(j+1)+' ***')
       print('  student name: ',student[j]['name'])
       student[j]['weight_last']=round(float(input('  enter weight (kg) : ')),1)
       print('       ***  record ended  ***\n')
    
        
    

def output(x):
    print('student name : ',student[x]['name'])
    print('first weight : ',student[x]['weight_first'])
    print('last weight  : ',student[x]['weight_last'])
    student[x]['weight_diff']=round(student[x]['weight_first']-student[x]['weight_last'],1)
    print('\n')

def weightchange():
    for x in range(30):
        if abs(student[x]['weight_diff'])>=2.5:
            output(x)
            if student[x]['weight_diff']>0:
                print('good work! your lost weight. ')
            else:
                print('Oops you gained weight !!! ')
        print('\n')       

measure_weight()
print('\n\n\n')

for n in range(30):
    output(n)
    print('\n')
print('\n\n\n')
weightchange()
