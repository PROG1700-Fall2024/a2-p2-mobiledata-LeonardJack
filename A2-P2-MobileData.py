#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Take in the users date usage in MB
    #if less than 200mb ---> 20$
    #if over 200mb but less than or equal to 500 add 20$ and 0.105$ per mb
    #if over 500mb but less than or equal to 1000mg add 20$ and 1.110 per mb
    #if over 1000mb ---> 118$
    #calculate a print total based on which category total falls into

    dataUsage = int(input("Enter the amount of data you used(mb): "))   #Takes in data used
    total = 20  #intial cost will at least be 20
    dataBilled = dataUsage - 200 #data after the 200mb covered by flat fee

    if dataUsage <= 200:     #if less than or equal to 200mb keep cost the same
        pass
    elif dataUsage > 200 and dataUsage <= 500:   #adds to total if greater than 200 and less than or equal to 500
        total += dataBilled * 0.105
    elif dataUsage > 500 and dataUsage <= 1000:#adds to total if greater than 500 and less than or equal to 1000
        total += dataBilled * 0.110
    elif dataUsage > 1000:      #makes total 118 flat fee if greater than 1000mb
        total = 118
    
    print("Total charge is: ${0:.2f}".format(total))    #formatted print statement with total








    # YOUR CODE ENDS HERE

main()