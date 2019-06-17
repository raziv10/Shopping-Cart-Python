def purchase(stock_List):                               #creates a function.
    stock_L=stock_List                                  #assign the list used in readfile function.
    name=input("Enter the name of customer: ")          # ask the user to input his/her name.
    d={}                                                #creates an empty dictionary .
    ans="Y"
    while ans.upper()=="Y":                             #enters the loop.
        product=input("Enter the product name: ").upper()#ask to input the product name.
        #checks the index of the list where products are placed so as to find the product inserted by the user is in the list or not.
        if product == (stock_L[0][0]).upper() or product == stock_L[1][0].upper()  or product== stock_L[2][0].upper() :
            a=True
            while a==True:
                                                            #enters loop inside a loop. 
                try:                                        # try if it is True.
                    quantity=int(input("Number of product: "))#ask to input the quantity numbers in integer.
                    if quantity <= int(stock_L[0][2]) and quantity <= int(stock_L[1][2]) and quantity <= int(stock_L[2][2]):
                        #checks the index of the list where quntity are placed so as to find the quantity inserted by the user is in the list or not.
                        d[product]=quantity                 #assign the value of quantity to store the purchase item and its corresponding quantity.
                        a=False
                    else:
                        print("We don't have enough stock please insert the quantity of the stock available.")#displays the result if the quantity is less than the quantity required by the user.
                except:
                    print("Enter integer value please!! ")            #ask to input integer value only.
            ans=(input("more products?(Y/N)"))                        #ask to continue further or not and exits the inner loop.
        else:
            print("Sorry we are out of stock!!")                      # if the product name is not in the list display the result and exits the loop.
    print(d)

    
##Calculation.
#Generating Invoice.
    total=0                                                         #assign total to zero.
    for keys in d.keys():                                           #enters the loop.
        if keys==stock_L[0][0].upper():                             #check the index where the product is placed. 
            phone_price=int(stock_L[0][1])                          #check the price of the phone.
            qty1=int(d[keys])                                       #checks the quantity of the phone.
            phone_amount=(phone_price*qty1)                         #multiplies the quantity and the price of the phone.
            total+=(phone_price*qty1)                               #gives the total price for the phone.
            print("Cost for phone: ",phone_amount) 
        elif keys==stock_L[1][0].upper():                           ## same as above case.
            laptop_price=int(stock_L[1][1])
            qty2=int(d[keys])
            laptop_amount=(laptop_price*qty2)
            total+=(laptop_price*qty2)
            print("Cost for laptop: ",laptop_amount)
        else:                                                       ## same as above case.
            hdd_price=int(stock_L[2][1])
            qty3=int(d[keys])
            hdd_amount=(hdd_price*qty3)
            total+=(hdd_price*qty3)
            print("Cost for HDD: ",hdd_amount)
    print("Total cost of products: ", total)
    discount=float(input("Enter the discount percentage(%): "))
    grandtotal=float(total-(discount*total)/100)
    print("TOTAL AMOUNT: ", grandtotal)
    print("\n")

    import datetime                                                 #imports datetime from buildin python functions.
    dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    s=str(dt)                                                       #assin to s.
    file=open(s+".txt","w")                                         #creates/writes a file named with current time as the name of the file.
    file.write("__________________________INVOICE______________________________")
    file.write("\n")
    file.write("\n")
    file.write("_____________________ GADGETIFICATION MART_____________________")
    file.write("\n")
    file.write("_______________________ Dillibazar,Ktm_________________________")
    file.write("\n")
    file.write("__________________________ 01-444222___________________________")
    file.write("\n")
    file.write("\n")
    file.write(str("Name: "+str(name)+"                       Date: "+s))#assign user's name to "Name:" and current time to "Date:". 
    file.write("\n")
    file.write("\n")
    file.write("\tProducts \t Qty \t Rate \t Price"                 )#displays product qty and Price as headings with tabs included in the invoice structure.
    file.write("\n")
          
    for keys in d.keys():                                           #enter the loop.
        if keys=="PHONE":                                           #if the dict key is equal to the string PHONE.
            file.write(str("\t"+str(keys)+" \t\t "+str(d['PHONE'])+" \t "+str(stock_L[0][1])+" \t "+str(phone_amount)))#write the quantity,name,price and total product price of the item in string.
            file.write("\n")
        elif keys=="LAPTOP":
            file.write(str("\t"+str(keys)+" \t\t "+str(d['LAPTOP'])+" \t "+str(stock_L[1][1])+" \t "+str(laptop_amount)))
            file.write("\n")
        else:
            file.write(str("\t"+str(keys)+" \t\t "+str(d['HDD'])+" \t "+str(stock_L[2][1])+" \t "+str(hdd_amount)))
            file.write("\n")

    file.write("______________________________________________________________")
    file.write("\n")
    file.write("\t\t\t\t Total:  "+str(total))                      #calls total to display in the invoice structure.
    file.write("\n")
    file.write("______________________________________________________________")
    file.write("\n")
    file.write("\t\t\t\t Discount% :"+str(discount))                #calls discount to display in the invoice structure.
    file.write("\n")
    file.write("______________________________________________________________")
    file.write("\n")
    file.write("\t\t\t\t Grand Total:"+str(grandtotal))             #calls grandtotal to display in the invoice structure.
    file.write("\n")
    file.write("\n")
    file.write("________________________THANK YOU!!!__________________________")
    file.write("\n")
    file.write("______________________ Do visit again.________________________")
    file.close()
    return d
    
