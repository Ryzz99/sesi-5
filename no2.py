def generate_sequence(n):
    sequence = []
    num = 2
    increment = 2
    for i in range(n):
        sequence.append(num)
        num += increment
        increment += 1
    return sequence

def main():
    n = 6  # Jumlah bilangan dalam deret
    sequence = generate_sequence(n)
    for num in sequence:
        print(num, end=" ")

if __name__ == "__main__":
    main()
