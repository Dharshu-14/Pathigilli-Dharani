def generate_series_odd_input():
    try:
        a = int(input("Enter an integer (a): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if a <= 0:
        print("Input must be a positive integer.")
        return

    if a % 2 == 0:
        count = a - 1
    else:
        count = a

    series = []
    n = 1
    for _ in range(count):
        series.append(str(n))
        n += 2

    print(", ".join(series))

if __name__ == "__main__":
    generate_series_odd_input()
