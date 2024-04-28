from collections import Counter

def can_form_number(number, count_x):
    count_n = Counter(str(number))
    for digit, amount in count_n.items():
        if count_x[digit] < amount:
            return False
    return True

def find_numbers(n, x):
    count_x = Counter(str(x))
    start = 10**(n-1)
    if n == 1:
        start = 0  # Включаем однозначные числа
    end = 10**n - 1
    valid_numbers = []
    
    for number in range(start, end + 1):
        if can_form_number(number, count_x):
            valid_numbers.append(number)
    
    return valid_numbers

def main():
    n = int(input("Введите N (количество цифр числа): "))
    x = int(input("Введите число X: "))
    valid_numbers = find_numbers(n, x)
    print(f"Количество подходящих чисел: {len(valid_numbers)}")
    
    show_numbers = input("Хотите ли вывести все подходящие числа? (да/нет): ").lower()
    if show_numbers == 'да':
        print("Подходящие числа:")
        print(valid_numbers)

if __name__ == "__main__":
    main()