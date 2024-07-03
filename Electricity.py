def calculateBill(units):
 

    # Condition to find the charges 

    # bar in which the units consumed 

    # is fall 

    if (units <= 100):

      

        return units * 10; 

     

    elif (units <= 200):

     

        return ((100 * 10) +

                (units - 100) * 15); 

     

    elif (units <= 300):

      

        return ((100 * 10) +

                (100 * 15) +

                (units - 200) * 20); 

     

    elif (units > 300):

     

        return ((100 * 10) +

                (100 * 15) +

                (100 * 20) +

                (units - 300) * 25); 

     

    return 0; 
 
# Driver Code 

units = 250; 

print(calculateBill(units)); 
 
