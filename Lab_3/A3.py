
prev = int(input("Введите предыдущее показание: "))
curr = int(input("Введите текущее показание: "))

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

cost = 0.0

if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21.0 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.0 + (600 - 300) * 0.06 + (used - 600) * 0.04
else:
    cost = 21.0 + (600 - 300) * 0.06 + (800 - 600) * 0.04 + (used - 800) * 0.025

if used > 0:
    avg_price = cost / used
else:
    avg_price = 0.0

print(f"{'Предыдущее':<15}{'Текущее':<15}{'Использовано':<15}{'К оплате':<15}{'Ср. цена m^3':<15}")
print(f"{prev:<15}{curr:<15}{used:<15}{cost:<15.2f}{avg_price:<15.2f}")
