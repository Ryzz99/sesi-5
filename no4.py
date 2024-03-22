def generate_multiplication_table():
    number = 7
    for i in range(6, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    generate_multiplication_table()

if __name__ == "__main__":
    main()
