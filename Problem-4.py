def count_multiples():
    input_str = input("Enter a list of numbers separated by commas (e.g., 1,2,8,9,12): ")
    try:
        numbers = [int(x.strip()) for x in input_str.split(',') if x.strip()]
    except ValueError:
        print("Invalid input. Please ensure all items are integers.")
        return

    divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result_dict = {}

    for d in divisors:
        count = 0
        for num in numbers:
            if num % d == 0:
                count += 1
        result_dict[d] = count

    print(result_dict)

if __name__ == "__main__":
    count_multiples()
