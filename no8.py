def print_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("1", end=" ")
        print()

def main():
    rows = 4  # Jumlah baris
    print_pattern(rows)

if __name__ == "__main__":
    main()
