import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array_3x3 = np.array(list).reshape(3, 3)
    #print(array_3x3)

    axis1_mean = np.mean(array_3x3, axis=0)
    axis2_mean = np.mean(array_3x3, axis=1)
    flattened_mean = np.mean(array_3x3)
    
    axis1_var = np.var(array_3x3, axis=0)
    axis2_var = np.var(array_3x3, axis=1)
    flattened_var = np.var(array_3x3)

    axis1_std = np.std(array_3x3, axis=0)
    axis2_std = np.std(array_3x3, axis=1)
    flattened_std = np.std(array_3x3)

    axis1_max = np.max(array_3x3, axis=0)
    axis2_max = np.max(array_3x3, axis=1)
    flattened_max = np.max(array_3x3)

    axis1_min = np.min(array_3x3, axis=0)
    axis2_min = np.min(array_3x3, axis=1)
    flattened_min = np.min(array_3x3)

    axis1_sum = np.sum(array_3x3, axis=0)
    axis2_sum = np.sum(array_3x3, axis=1)
    flattened_sum = np.sum(array_3x3)

    calculations = {
        'mean': [axis1_mean.tolist(), axis2_mean.tolist(), flattened_mean],
        'variance': [axis1_var.tolist(), axis2_var.tolist(), flattened_var],
        'standard deviation': [axis1_std.tolist(), axis2_std.tolist(), flattened_std],
        'max': [axis1_max.tolist(), axis2_max.tolist(), flattened_max],
        'min': [axis1_min.tolist(), axis2_min.tolist(), flattened_min],
        'sum': [axis1_sum.tolist(), axis2_sum.tolist(), flattened_sum]
    }

    return calculations
