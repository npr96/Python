global remainder_of_my_dataset
global variance_of_my_dataset
global variance_of_my_regressor
my_dataset = (7,11,13,98,22,64,55,100,42,87)
my_regressor = (6, 14, 17, 88,35,75,88,111,22,91)
regressor_length = len(my_regressor)
dataset_length = len(my_dataset)
average_of_my_dataset = sum(my_dataset) / dataset_length
average_of_my_regressor = sum(my_regressor) / regressor_length
remainder_of_my_dataset = 0
variance_of_my_dataset = 0
variance_of_my_regressor = 0
Covariance_of_my_dataset = 0
#remainder
for i in my_dataset:
    remainder_of_element = abs(i - average_of_my_dataset)
    remainder_of_my_dataset = remainder_of_my_dataset + remainder_of_element
print('remainder: ' + str(remainder_of_my_dataset))
# variance
for i in my_dataset:
    variation_in_element = (i - average_of_my_dataset)**2
    variance_of_my_dataset = variance_of_my_dataset + variation_in_element
standard_deviation_of_my_dataset = variance_of_my_dataset**(1/2)
print('variance: ' + str(variance_of_my_dataset))
print('standard deviation: ' + str(standard_deviation_of_my_dataset))
for x in my_regressor:
    variation_in_element = (i - average_of_my_dataset)**2
    variance_of_my_regressor = variance_of_my_regressor + variation_in_element
print('regressor variance: ' + str(variance_of_my_regressor))
#b
for x, y in zip(my_dataset, my_regressor):
    covariance_first = x * y / dataset_length
    covariance_second =average_of_my_dataset * average_of_my_regressor / dataset_length
    covariance_in_element = covariance_first + covariance_second
    Covariance_of_my_dataset = covariance_in_element + Covariance_of_my_dataset
print('covariance: ' + str(Covariance_of_my_dataset))
b_hat = Covariance_of_my_dataset / variance_of_my_regressor
print('B1: ' + str(b_hat))
#there seems to be an issue with values holding from block to block