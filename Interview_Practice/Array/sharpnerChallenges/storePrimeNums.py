def prime_numbers(n):
    """ Function to store first n prime_numbers in a list
    Return the list containing the prime numbers """
    counter = 0
    output = []
    start_num = 2
    while len(output) < n:
        flag = True
        for i in range(2,int(start_num**0.5) + 1):
            if start_num % i == 0:
                flag = False
                break
        if flag:
            output.append(start_num)
        start_num += 1
    return output

    
   
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    

if __name__ == "__main__":
    main()