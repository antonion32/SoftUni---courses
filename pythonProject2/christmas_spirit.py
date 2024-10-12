quantity_decorations = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit = 0
ornament_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_decorations * ornament_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_decorations * (skirt_price + garland_price)
        total_spirit += 13
    if current_day % 5 == 0:
        total_cost += quantity_decorations * lights_price
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += skirt_price + garland_price + lights_price

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")