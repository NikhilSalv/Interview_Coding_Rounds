def even_odd(n):
    """
    using & operator, check the last bit
    if its 1, then number is odd.
    it makes all other bits as zero as and operator need both bits as 1, to let it become 1
    """
    if n & 1:
        return "odd"
    else:
        return "even"
    
def number_of_ones(n):
    count = 0
    while n:
        count += n &1
        n >>= 1
    return count

def is_power_of_two(n):
    return n > 0  and (n & (n-1)) == 0

def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return [a,b]

def set_kth_bit(n, k):
    n = n | (1 << k)
    return n

def clear_kth_bit(n,k):
    n = n & ~(1<<k)
    return n

def toggle(n,k):
    n = n ^ (1<<k)
    return n



if __name__ == "__main__":
    print("even or odd : ", even_odd(6))
    print("Number of 1s : ", number_of_ones(5)) #1001
    print("8 is power of 2?",is_power_of_two(8)) # true
    print("9 is power of 2?",is_power_of_two(9)) #false
    print("swap 5 and 8 : ", swap(5,8)) # [8,5]
    print("set_2nd_bit as one regardless",set_kth_bit(10, 2) ) # 1010 >> 1110:  output should be 14
    print("set_4th_bit as zero regardless",clear_kth_bit(28, 2) ) # 11100 >> 11000:  output should be 24
    print("toggle_2nd_bit",toggle(28, 2) ) # 11100 >> 11000:  output should be 24



