#this is a function that takes in two data-sets and regresses them, the two datasets need to have the same length. 
from decimal import *
getcontext().prec = 6
summary_indicator = False
def regression_function(dependant_variable, independant_variable, summary_indicator):
    decimal_dependant_variable = [Decimal(i) for i in dependant_variable]
    decimal_independant_variable = [Decimal(i) for i in independant_variable]
#summary of data
    if summary_indicator == True:
        print('Maximum of Dependant Variable: ' + str(max(decimal_dependant_variable)))
        print('Minimum of Dependant Variable: ' + str(min(decimal_dependant_variable)))
        print('Mean of Dependant Variable: ' + str(sum(decimal_dependant_variable)/len(decimal_dependant_variable)))
        print('Maximum of Independant Variable: ' + str(max(decimal_independant_variable)))
        print('Minimum of Independant Variable: ' + str(min(decimal_independant_variable)))
        print('Mean of Independant Variable: ' + str(sum(decimal_independant_variable)/len(decimal_independant_variable)))
#covariance of variables
    ex_of_xy_counter = 0
    janky_index_counter = -1
    ex_of_xy = 0
    covariance_of_variables = 0
    product_of_means = 0
    mean_of_dependant = sum(decimal_dependant_variable)/len(decimal_dependant_variable)
    mean_of_independant = sum(decimal_independant_variable)/len(decimal_independant_variable)
    for i in decimal_dependant_variable:
        janky_index_counter = janky_index_counter + 1
        ex_of_xy_counter = i*decimal_independant_variable[janky_index_counter] + ex_of_xy_counter
    ex_of_xy = ex_of_xy_counter / len(decimal_dependant_variable)
    product_of_means = mean_of_dependant * mean_of_independant
    covariance_of_variables = ex_of_xy - product_of_means
    print('Covariance of Variables: ' + str(covariance_of_variables))
#variance of x
    variance_of_independant_variable = 0
    variance_independant_variable_counter = 0
    for i in decimal_independant_variable:
        variance_independant_variable_counter = (i-mean_of_independant)**2 + variance_independant_variable_counter
    variance_of_independant_variable = variance_independant_variable_counter / len(decimal_independant_variable)
#beta calculation
    beta_hat = covariance_of_variables / variance_of_independant_variable
    print('Coeficient of Regression: ' + str(beta_hat))
#need prediction of fi in SSres befor we can work on r squared
    f1 = []
    for i in decimal_independant_variable:
        f1.append(i * beta_hat)
#sum of squares and R squared
    squares_container = 0
    for i in decimal_dependant_variable:
        squares_container = (i - mean_of_dependant)**2 + squares_container
    explained_squares_container = 0
    explained_squares_indexor = 0  
    for i in decimal_dependant_variable:
        explained_squares_container = (i - f1[explained_squares_indexor])
        explained_squares_indexor = explained_squares_indexor + 1
    r_squared = 1 - (explained_squares_container / squares_container)
    print('R-squared: ' + str(r_squared))
        


regression_function([1,2,3,4,5,6,7,8,9,10], [10,20,30,40,50,60,70,80,90,100], False)
