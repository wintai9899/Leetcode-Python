# Program to convert binary to decimal 

def bin_to_dec(binary):
    bin_list = list(binary)
    res = 0 
    
    for i in range(len(bin_list)):
        # pop from behind
        digit = bin_list.pop()
        if digit == "1":
            res += 2 ** i
    return res
    
    

if __name__ == '__main__':
    print(bin_to_dec("101"))