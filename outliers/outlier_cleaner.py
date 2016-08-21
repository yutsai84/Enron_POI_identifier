#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    

    error = (predictions-net_worths)**2 
    cleaned_data = zip(ages,net_worths,error)
    cleaned_data = sorted(cleaned_data,key=lambda x: x[2],reverse=True)
    limit =int(len(net_worths)*0.1)
    
    
    ### your code goes here

    
    return cleaned_data[limit:]

