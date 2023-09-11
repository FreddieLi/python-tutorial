'''Sum of absolute differences of indices of occurrences of each array element
Given an array arr[] consisting of N integers, the task for each array element arr[i] is to print the sum of |i - j| for all possible indices j such that arr[i] = arr[j].

Examples:

Input: arr[] = {1, 3, 1, 1, 2}
Output: 5 0 3 4 0
Explanation: 
For arr[0], sum = |0 - 0| + |0 - 2| + |0 - 3| = 5. 
For arr[1], sum = |1 - 1| = 0. 
For arr[2], sum = |2 - 0| + |2 - 2| + |2 - 3| = 3. 
For arr[3], sum = |3 - 0| + |3 - 2| + |3 - 3| = 4. 
For arr[4], sum = |4 - 4| = 0. 
Therefore, the required output is 5 0 3 4 0.

Input: arr[] = {1, 1, 1}
Output: 3 2 3
'''

# naive method
def sum(arr, n):
    # Traverse over the array
    for i in range(n):
        s = 0
 
        # Check for every other elements of the array
        for j in range(n):
 
            # Add into sum if such pair found
            if arr[i] == arr[j]:
                s += abs(i - j)
 
        # Print the sum
        print(s, end=" ")
 
# Driver code
if __name__ == '__main__':
    # Given array
    arr = [1, 3, 1, 1, 2]
    print('input is',arr)
    # Given size
    n = len(arr)
 
    # Function call
    sum(arr, n)