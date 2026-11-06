def validate_card_number(card_number: str) -> bool:
    cleaned = card_number.replace(" ", "").replace("-", "")

    if not cleaned.isdigit() or len(cleaned) == 0:
        return False

    total_sum = 0
    digits = [int(d) for d in reversed(cleaned)]

    for idx, digit in enumerate(digits):
        if idx % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit

    return total_sum % 10 == 0


card = input("Введите номер кредитной карты для проверки: ")

if validate_card_number(card):
    print("Вывод: Карта валидна (Номер корректен)")
else:
    print("Вывод: Карта невалидна (Ошибка в номере)")
