import time
from implicit_matrix_memoized import digits_sequence

if __name__ == '__main__':
    try:
        n = int(input("Enter n number : "))
        if n < 0:
            print('n should be greater or equal 0')
            exit(0)
    except ValueError:
        print('Please enter a valid number.')
        exit(0)
    print("=====================================================")
    print(f'Start to calculate {n}th number of fibonacci series.')
    print("=====================================================")
    start = time.perf_counter()
    number = digits_sequence(n)
    end = time.perf_counter()
    print(number)
    print("=====================================================")
    print(f'output is a {len(number)} digits number.')
    print(f'finished. time elapsed : {end - start} seconds.')
    print("=====================================================")