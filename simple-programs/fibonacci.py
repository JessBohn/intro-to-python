# THis is a simple program that will return the nth number in the
# Fibonacci sequence

def fibonacci_sequence(n):
    list_1 = [0,1]
    current_index = len(list_1)

    while (current_index - 2) != n:
        list_1.append((list_1[current_index - 2] + list_1[current_index - 1]))
        current_index += 1

    return list_1[n]

print "Here is the nth number of the Fibonacci Sequence: ", fibonacci_sequence(7)


def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n <= 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

print "Here is the nth number of the Fibonacci Sequence, done recursively: ", recursive_fibonacci(10)
