def fibonacci_sequence(n):
    seq = [0, 1]
    while seq[-1] < n:
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)
    return seq

def is_in_fib_seq(num, fibonacci_seq):
    return num in fibonacci_seq

def main():
    num = int(input("Informe um número: "))
    fibonacci_seq = fibonacci_sequence(num)
    if is_in_fib_seq(num, fibonacci_seq):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
