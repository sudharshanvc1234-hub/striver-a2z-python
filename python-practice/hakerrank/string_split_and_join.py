def split_and_join(line):
    value1=line.split()
    value2="-".join(value1)
    return value2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)