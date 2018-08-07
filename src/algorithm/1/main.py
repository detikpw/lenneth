from functools import reduce

'''
Split an array into two equal Sum subarrays
Given an array of integers greater than zero,
find if it is possible to split it in two subarrays (without reordering the elements),
such that the sum of the two subarrays is the same.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output : ([1, 2, 3, 4], [5, 5])

Input : Arr[] = { 1 , 2 ,3 , 4 }
Output : false
source https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/

'''

sum = lambda list: reduce((lambda a, b: a + b), list, 0)

def get_result(left, right):
    if len(left) == 0:
        return false
    if sum(left) == sum(right):
        return (left, right)
    *head, tail = left
    return get_result(head, right + [tail])

def main():
    arr = [1, 2, 3, 4, 5, 5]
    res = get_result(arr, [])
    print(res)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()