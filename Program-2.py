def generate_series():
    try:
        a = int(input("Enter an integer (a): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if a <= 0:
        print("Input must be a positive integer.")
        return

    series = []
    n = 1
    for _ in range(a):
        series.append(str(n))
        n += 2

    print(", ".join(series))

if __name__ == "__main__":
    generate_series()
