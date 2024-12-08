
#from openpyxl import workbook #we are using a list of cow_ids,and a variable of total milk, keeping it simple and a list of 7 days against each cow id and a dictionary of 2 variable morning and evening to store milk,whenever the cow is yielded the total milk is updated to avoid extra computation for using loops
base_id=101
num_cows=int(input('!!!** enter number of cows : **!!! ->'))
#initialization a dictionary of list of dictionary of list,that's a nested concept
cows=[
   
    {
        'total_milk':0.0,
        'day':[{'morning':0.0,'evening':0.0} for _ in range(7)]
    }
        for _ in range(num_cows)
     ]

def milked_cow():                                                    #function to insert milk record
    print('!!!** cows are being milked now **!!!\n')
    for i in range(7):
        print('!!! enter the milk record for day : !!!',i+1)
        shift=input('***: enter (morning or evening) shift : ')
        print()
        print()                                                #just to insert lines
        if shift=='morning':                                   #morning shift milk insertion
            
            morning_shift(i)
            evening_shift(i)                                         #if started from morning then of that day evening should also by entered that way
        elif shift=='evening':                                 #evening shift milk insertion
            print('please make sure you have entered morning records')
            evening_shift(i)
        else:                                                        #error in the selection of shift
             print('!!!** error in shift selection **!!!\n\n')
             return
  
                
    
def morning_shift(i):
    print('!!!** please proceed with morning milk records : **!!!\n\n')
    for j in range(num_cows):
                cow_id=j                                           #int(input('enter cow id : '))%1000            #to restrict input to 3 digit
                print('cow id : ',cow_id+base_id)
                mor_milk=round(float(input('enter milk quantity : ')),1)#getting milk for morning and rounding upto 1 decimal
                cows[cow_id]['total_milk']+=mor_milk                 #storing it in the total milk of that cow
                cows[cow_id]['day'][i]['morning']=mor_milk
                print()                                              #to create a clear output
    return

def evening_shift(i):
    print('!!!** please proceed with evening milk records : **!!!\n\n')
    for k in range(num_cows):
                cow_id=k                                            #int(input('enter cow id : '))%1000            #to restrict input to 3 digit
                print('cow id : ',cow_id+base_id)
               
                eve_milk=round(float(input('enter milk quantity: ')),1)#getting milk for night and rounding upto 1 decimal
                cows[cow_id]['total_milk']+=eve_milk                 #storing it in the total milk of that cow
                cows[cow_id]['day'][i]['evening']=eve_milk
                print()                                              #to create a clear output
    return

def cal_displayANDmax():                                                   #finding max producer and displaying average and total milk of each cow
    stored_milk=0.0                                                      #total milk production
    for m in range(num_cows):
        max_milk=cows[0]['total_milk']                             #defining maximum milk variable
        max_cow_id=0                                               #maximum milk producer cow
        stored_milk+=cows[m]['total_milk']
        
        print('\n\n-------milk record ',m+1,' -------')
        print('----------------------cow id : ',base_id+m)               #printing record
        print('total milk produced in a week: ',round(cows[m]['total_milk'],1)) #printing total milk produced
        
        print('-------- record ended -------')
        if max_milk<cows[m]['total_milk']:                       #checking for maximum milk by a cow in week
            max_milk=cows[m]['total_milk']
            max_cow_id=m
    print('\n\n-------MAXIMUM MILK PRODUCTION RECORD-------')
    print('-------------------------cow id : ',max_cow_id+base_id)              #printing record
    print('total milk by this cow in a week: ',round(cows[max_cow_id]['total_milk'],1)) #printing total milk produced by single cow
    print('-------- record ended -------')
    avg_milk=round(stored_milk/7,1)
    print('\n\nmilk production of herd in a week: ',round(stored_milk,1),'liters')     #printing total milk produced of herd
    print('-average milk produced daily : ',round(avg_milk,1),'liters')            #printing average milk

def min_milk():
    for day in range(7):
        if day>3:                                                 #cows with production less than 12 liters
            for n in range(num_cows):
                if cows[n]['total_milk']<12.0:
                    print('\n\n-------LESS THAN 12L MILK PRODUCTION RECORD-------')
                    print('----------------------cow id : ',base_id+n)              #printing record
                    print('total milk produced in ',n+1,' days: ',cows[n]['total_milk']) #printing total milk produced
                    print('-------- record ended -------')
            return
            

milked_cow()
cal_displayANDmax()
min_milk()
    
    

