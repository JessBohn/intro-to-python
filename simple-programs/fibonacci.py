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
