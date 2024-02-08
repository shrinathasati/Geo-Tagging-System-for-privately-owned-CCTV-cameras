def maxFrequency(arr, K, X):
    n = len(arr)
    
    # Sort the array
    arr.sort()
    
    maxFreq = 1
    
    for i in range(1, n):
        # Calculate the number of operations needed to extend the range
        ops = (arr[i] - arr[i-1] - 1) // X
        
        # Calculate the maximum frequency for the current range
        freq = ops + 1
        
        # Adjust the frequency if there are available operations
        freq = min(freq, K + 1)
        
        # Update the maximum frequency
        maxFreq = max(maxFreq, freq)
        
        # Update the remaining operations
        K -= (freq - 1)
    
    return maxFreq

# Example usage:
N = 4
K = 2
X = 2
arr = [1, 4, 6, 8]
result = maxFrequency(arr, K, X)
print("Maximum frequency:",)
