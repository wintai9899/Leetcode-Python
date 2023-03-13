def dec_to_bin(num):
    res = []
    
    while num != 0:
        remainder = num % 2
        res.append(str(remainder))
        num = num // 2
    # reverse res
    binary = res[::-1]
    return "".join(binary)
    
    
    
if __name__ == '__main__':
    print(dec_to_bin(5))
    print(dec_to_bin(28))
    print(dec_to_bin(64))