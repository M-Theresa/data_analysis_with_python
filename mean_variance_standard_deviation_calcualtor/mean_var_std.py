"""
calcualte() takes a list containing 9 elements, converts it into a 3x3 array,
calculate the mean, variance, standard deviation, min, max and sum, then stores
the values in a dictionary.

"""

import numpy as np

def calculate(list_input):
    # the list_input must contain 9 elements
    if len(list_input) != 9:
        raise ValueError(f'List must contain nine numbers.')

    try:
        # convert the list_input to numpy array
        cal_array = np.array(list_input, dtype='float').reshape(3,3)
    # rasie exception if unable to convert to float
    except ValueError:
        print(f'list contains the wrong data type')
        raise
    # calculate min, var, std, min, max and sum, and store in a dictionary
    mean_output = [list(np.mean(cal_array, axis=0)), list(np.mean(cal_array, axis=1)), np.mean(cal_array)]
    var_output = [list(np.var(cal_array, axis=0)), list(np.var(cal_array, axis=1)), np.var(cal_array)]
    std_output = [list(np.std(cal_array, axis=0)), list(np.std(cal_array, axis=1)), np.std(cal_array)]
    min_output = [list(cal_array.min(axis=0)), list(cal_array.min(axis=1)), cal_array.min()]
    max_output = [list(cal_array.max(axis=0)), list(cal_array.max(axis=1)), cal_array.max()]
    sum_output = [list(np.sum(cal_array, axis=0)), list(np.sum(cal_array, axis=1)), np.sum(cal_array)]
    calculations = {
        'mean': mean_output,
        'variance': var_output,
        'standard deviation': std_output,
        'max': max_output,
        'min': min_output,
        'sum': sum_output
    }
    return calculations

if __name__ == '__main__':
    A = ['3', '1', 2, 3, 1, 3, 5, 3, 0]
    print(calculate(A))
