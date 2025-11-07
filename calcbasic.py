def add(nums):
    return sum(nums)

def subtraction(nums):
    result = nums[0]
    for num in nums[1:]:
        result -=num
    return result 

def multiply(nums):
    result =1 
    for num in nums:
        result *= num
    return result

def division(nums):
    result = nums[0]
    for num in nums[1:]:
        if num == 0:
            return "div by zero is not possible"
        result /= num
    return result 

print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.division")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))

        if choice == '1':
            print("Result:", add(numbers))
        elif choice == '2':
            print("Result:", subtraction(numbers))
        elif choice == '3':
            print("Result:", multiply(numbers))
        elif choice == '4':
            print("Result:", division(numbers))

        next_calculation = input("Do another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid input")