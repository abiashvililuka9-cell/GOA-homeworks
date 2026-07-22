user_info = lambda name, surname, age: f"name: {name}, surname: {surname}, age: {age}"

print(user_info("Luka", "abiashvili", 16))






average = lambda numbers: sum(numbers) / len(numbers)

print(average([10, 20, 30, 40, 50]))







is_palindrome = lambda text: text == text[::-1]

print(is_palindrome("ara"))
print(is_palindrome("hello"))






check_number = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))







multiply_by_two = lambda numbers: [num * 2 for num in numbers]

print(multiply_by_two([1, 2, 3, 4, 5]))








filter_strings = lambda words: [word for word in words if len(word) > 5]

print(filter_strings(["apple", "banana", "car", "elephant", "dog"]))








negative_numbers = lambda numbers: [num for num in numbers if num < 0]

print(negative_numbers([10, -5, 3, -8, 0, -1, 7]))