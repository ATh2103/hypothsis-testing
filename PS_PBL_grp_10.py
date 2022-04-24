
import pandas as pd # to read the CSV data set file
import numpy as np # for calculation purpose
from scipy.stats import ztest_1samp # very important to finding the p-value and doing T-test
file2 = pd.read_csv(r'C:/Users/dell/Downloads/ps3.csv') # reading the csv dataset 
def hypo_test():
    print("The data set is: ")
    file2['diff'] = (file2['CLUBS'] - file2['CGPA']) # finding the difference to find the mean difference for paired T-test
    print(file2)
    mean = np.mean(file2)
    print(mean)

    print("\n****____Enter the values for paired T-test____****")
    n = float(input("\nEnter your value for null hypothesis: ")) # value for null hypothesis
    losig = float(input("Enter the level of significance: ")) # significance value 

    file3 = file2['diff']
    tset , pval = ztest_1samp(file3 , n) #finding the p-value
    print("\nP-value is:", pval)

    #comparing the value and level of significance
    if(pval < losig): 
        print("\nSince the value of significance is: ", losig , "and pval < level of Sig.")
        print("We have to reject the Null hypothesis")
    else:
        print("\nAs the value of significance is: ", losig , "and pval > level of Sig.")
        print("We have failed to reject the Null hypothesis")


#The bulit menu, Enjoy your time
print("\n\t\t*****________HYPOTHESIS TESTING BY PAIRED T-TEST_______*****")
print("Press 1 to see the data\nPress 2 for calculating the T-test\nPress 3 to exit")
ch = int(input("\tEnter your choice: "))

while True:
    if(ch == 1):
        print("The data set is: ")
        print(file2)
        ch = input("Do you want to continue: ")
        if(ch == "Y" or ch == "y"):
            print("\n")
            hypo_test()
            break
        break
    elif(ch == 2):
        hypo_test()
        break
    elif(ch == 3):
        print("Thank you for your time, Hope you would liked it.")
        exit(0)
    else:
        print("Wrong value, try again")
        break