import random
import time

n = int(input("Введите количество примеров: "))

correct_count = 0
total_time = 0.0

for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")

    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_answer = a * b

    while True:
        start_time = time.time()
        user_input = input(f"{a} * {b} = ")
        end_time = time.time()

        time_spend = end_time - start_time

        try:
            answer = int(user_input)
            total_time += time_spend
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    if answer == correct_answer:
        print(f"Верно! (Время: {time_spend:.1f} сек)")
        correct_count += 1
    else:
        print(f"Неверно! Правильно: {correct_answer} (Время: {time_spend:.1f} сек)")

percent = (correct_count / n) * 100 if n > 0 else 0.0
avg_time = total_time / n if n > 0 else 0.0

print("========================================")
print("СТАТИСТИКА:")
print("========================================")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {avg_time:.1f} сек")
print(f"Правильных ответов: {correct_count}/{n}")
print(f"Процент правильных: {percent:.1f}%")
