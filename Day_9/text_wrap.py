#using library
import textwrap

def wrap(string, max_width):
   
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#without using library

def wrap(string, max_width):
    # Initialize an empty list to store the wrapped substrings
    wrapped = []
    
    # Split the string into substrings of length max_width
    for i in range(0, len(string), max_width):
        wrapped.append(string[i:i+max_width])
    
    # Join the wrapped substrings with a newline character
    return '\n'.join(wrapped)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
