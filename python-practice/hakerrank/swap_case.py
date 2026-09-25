def swap_case(s):
    value=s.swapcase()
    return value

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)