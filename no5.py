def print_pattern(baris, kolom):
    for i in range(1, baris + 1):
        for j in range(kolom):
            print(i, end=" ")
        print()

def main():
    baris = 3  # Jumlah baris
    kolom = 4  # Jumlah kolom
    print_pattern(baris, kolom)

if __name__ == "__main__":
    main()
