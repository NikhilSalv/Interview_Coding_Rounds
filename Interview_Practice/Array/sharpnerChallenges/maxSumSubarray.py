def find_maximum_subarray(arr, length):
    """write the code to find the maximum subarray sum
    only return the maximum sum of the subarray . 
    Both array and size of array is given """
    sum = arr[0]
    i = 0

    while i < length:
        j = i
        while j < length:
            k = i
            sum_subarray = 0
            while k <= j:
                sum_subarray += arr[k]
                k += 1
            sum = max(sum, sum_subarray)
            j += 1
        i += 1
    return sum
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum_subarray(arr, n))
    

if __name__ == "__main__":
    main()