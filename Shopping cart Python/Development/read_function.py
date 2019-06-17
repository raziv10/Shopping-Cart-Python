def readfile():                                     # creates a function.
    readfile=open("stock.txt","r")                  #read the text file
    lines=readfile.readlines()                      # read every line of the text file
    stock_L=[]                                      # creats an empty list.
    for line in lines:                              # enters the loop.
        stock_L.append(line.replace("\n","").split(","))
        #appends the text file to the empty list replacing new line break(\n) character and spaces and also spliting the text seperated by commas.
    readfile.close()                                # close the file so that pythn can save some memory.
    for i in range(len(stock_L)):                   # enters the loop.
        print("PRODUCT AVAILABLE: ",stock_L[i][0],"\t PRICE: ",stock_L[i][1],"\t QUANTITY: ",stock_L[i][2])
    return stock_L                                  # return the value of the list to the main function.
    
