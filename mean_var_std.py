import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    # Convert list to array 3x3
    matrix = np.reshape(list, (3,3))
    # Create dictionary to store the calculation
    calculation = {  'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
    }
    # Calculation of statistic of array 
    calculation["mean"] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    calculation["variance"] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    calculation["standard deviation"] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), float(matrix.std())]
    calculation["max"] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]  
    calculation['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    calculation['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    return calculation 
