
while True:
    packets = input("Ввод:\n")

    if len(packets) < 5:
        print("Ошибка! Длина строки должна быть не меньше 5 символов. Попробуйте снова.")
        continue

    if not all(char in '01' for char in packets):
        print("Неверный ввод. Используйте только символы '0' и '1'. Попробуйте снова.")
        continue

    break

total_packets = len(packets)
lost_packets = packets.count('0')

max_lost_streak = 0
current_streak = 0

for packet in packets:
    if packet == '0':
        current_streak += 1
        if current_streak > max_lost_streak:
            max_lost_streak = current_streak
    else:
        current_streak = 0

lost_percent = (lost_packets / total_packets) * 100

if lost_percent <= 1:
    quality = "отличное качество"
elif lost_percent <= 5:
    quality = "хорошее качество"
elif lost_percent <= 10:
    quality = "удовлетворительное качество"
elif lost_percent <= 20:
    quality = "плохое качество"
else:
    quality = "критическое состояние сети"

print("Вывод:")
print(f"Общее количество пакетов: {total_packets}")
print(f"Количество потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_lost_streak}")
print(f"Процент потерь: {lost_percent:.1f}%")
print(f"Качество связи: {quality}")
