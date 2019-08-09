string = "durgadevi"  
count = {}   
for i in string: 
    if i in count: 
        count[i] += 1
    else: 
        count[i] = 1
print ("Count of all characters:\n "+str(count)) 
