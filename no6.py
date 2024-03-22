def generate_fibonacci_sequence(n):
    fibonacci_sequence = [1, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def main():
    n = 10  # Jumlah angka dalam deret Fibonacci
    fibonacci_sequence = generate_fibonacci_sequence(n)
    for num in fibonacci_sequence:
        print(num, end=" ")

if __name__ == "__main__":
    main()
