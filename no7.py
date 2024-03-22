def generate_sequence(n):
    sequence = [1]
    num = 1
    for i in range(1, n):
        num += i * 1
        sequence.append(num)
    return sequence

def main():
    n = 10  # Jumlah angka dalam deret
    sequence = generate_sequence(n)
    for num in sequence:
        print(num, end=" ")

if __name__ == "__main__":
    main()
