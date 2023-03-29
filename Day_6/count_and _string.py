def count_substring(string, sub_string):
    c = string.count(sub_string)
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)