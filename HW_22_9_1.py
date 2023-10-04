def binary_search(arr, element, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if arr[middle - 1] < element <= arr[middle]:
        return [middle - 1]
    elif element < arr[middle]:
        return binary_search(arr, element, left, middle - 1)
    elif element == arr[middle - 1]:
        return binary_search(arr, element, left, middle - 1)
    else:
        return binary_search(arr, element, middle + 1, right)

arr = list(map(int, input("Введите несколько чисел от 1 до 10 через пробел:").split()))

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

element = int(input("Введите число от 1 до 10:"))

left = int(arr[0])
right = int(arr[-1])
if element < left or element > right:
    print("Введенное число находится вне дипазона")
else:
    print("Индекс числа, который меньше введённого:", binary_search(arr, element, 0, len(arr) - 1))
