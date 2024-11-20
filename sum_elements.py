#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def get_number_of_elements():
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX}): "))
            if 1 <= n <= MAX:
                return n
            else:
                print(f"Invalid input. Please provide a number ranging from 1 to {MAX}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_elements(n):
    elements = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Enter element {i + 1}: "))
                elements.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return elements

def main():
    n = get_number_of_elements()
    elements = get_elements(n)
    total_sum = calculate_sum(elements)
    print(f"The sum of the elements is: {total_sum}")

if __name__ == "__main__":
    main()

