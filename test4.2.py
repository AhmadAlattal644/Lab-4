items_data = {
    'r': {'name': 'rifle', 'size': 3, 'survival_points': 25},
    'p': {'name': 'pistol', 'size': 2, 'survival_points': 15},
    'a': {'name': 'ammo', 'size': 2, 'survival_points': 15},
    'm': {'name': 'medkit', 'size': 2, 'survival_points': 20},
    'i': {'name': 'inhaler', 'size': 1, 'survival_points': 5},
    'k': {'name': 'knife', 'size': 1, 'survival_points': 15},
    'x': {'name': 'axe', 'size': 3, 'survival_points': 20},
    't': {'name': 'talisman', 'size': 1, 'survival_points': 25},
    'f': {'name': 'flask', 'size': 1, 'survival_points': 15},
    'd': {'name': 'antidot', 'size': 1, 'survival_points': 10},
    's': {'name': 'supplies', 'size': 2, 'survival_points': 20},
    'c': {'name': 'crossbow', 'size': 2, 'survival_points': 20}
}

bag_capacity = 3 * 3

def knapsack(items_data, bag_capacity):
    dp = [0] * (bag_capacity + 1)
    item_choice = [None] * (bag_capacity + 1)

    mandatory_items = ['i', 'd']
    mandatory_points = sum(items_data[item]['survival_points'] for item in mandatory_items)

    for item in items_data:
        size = items_data[item]['size']
        survival_points = items_data[item]['survival_points']

        for j in range(bag_capacity, size - 1, -1):
            if dp[j - size] + survival_points > dp[j]:
                dp[j] = dp[j - size] + survival_points
                item_choice[j] = item

    selected_items = set(mandatory_items)
    current_capacity = bag_capacity
    current_capacity -= items_data['i']['size']
    current_capacity -= items_data['d']['size']

    while current_capacity > 0 and item_choice[current_capacity]:
        selected_items.add(item_choice[current_capacity])
        current_capacity -= items_data[item_choice[current_capacity]]['size']

    total_survival_points = dp[bag_capacity] + mandatory_points

    sorted_items = sorted(items_data.items(), key=lambda x: x[1]['survival_points'], reverse=True)

    remaining_capacity = bag_capacity - len(selected_items)

    for item, details in sorted_items:
        if item not in selected_items and remaining_capacity > 0:
            size = details['size']
            if remaining_capacity >= size:
                selected_items.add(item)
                remaining_capacity -= size

    inventory_layout: list[list[str]] = [['' for _ in range(3)] for _ in range(3)]
    index = 0
    for i in range(3):
        for j in range(3):
            if index < len(selected_items):
                inventory_layout[i][j] = list(selected_items)[index]
                index += 1

    while index < 9:
        remaining_items = [item for item in items_data if item not in selected_items]
        if remaining_items:
            inventory_layout[i][j] = remaining_items[0]
            selected_items.add(remaining_items[0])
            index += 1
        else:
            break

    return inventory_layout, total_survival_points

inventory_layout, total_survival_points = knapsack(items_data, bag_capacity)

for row in inventory_layout:
    print(row)
print(f"Очки_выживания: {total_survival_points}")
