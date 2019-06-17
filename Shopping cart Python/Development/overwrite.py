def overwrite(stock_List,Dictionary):       #creates a function.
    stock_L=stock_List                      #assign the values
    d=Dictionary
    for keys in d.keys():                   #enters the loop.
        if keys=="PHONE":
            stock_L[0][2]=str(int(stock_L[0][2])-d['PHONE'])
   ##reduce the amount of quantity purchased by the user to the quantity present in the list
    #so as to decrease the quantity after each purchase.        
        elif keys=="LAPTOP":
            stock_L[1][2]=str(int(stock_L[1][2])-d['LAPTOP']) 
        else:
            stock_L[2][2]=str(int(stock_L[2][2])-d['HDD'])
    print(stock_L)
        
    files=open("stock.txt","w")         #open a file to write the updates.      
    for each in stock_L:                #enters the loop 
        files.write(str(",".join(each)))
        files.write("\n")           
    files.close()                       #close the file
    return
