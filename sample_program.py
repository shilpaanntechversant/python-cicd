
def second_largest_num(digit_list):
    print("Testing")
    digit_list.sort(reverse=True)
    print("Sorted list: ", digit_list)
    return digit_list[1]


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    digit_list = [ int(input("Enter a digit: ")) for i in range(0, n)]
    print(second_largest_num(digit_list))