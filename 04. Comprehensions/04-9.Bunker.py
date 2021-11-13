categories = {x: [] for x in input().split(', ')}
n = int(input())
suma = 0
average = 0
for i in range(n):
    category, item_name, props = input().split(' - ')
    quantity = int(props.split(';')[0].split(':')[1])
    quality = int(props.split(';')[1].split(':')[1])
    if item_name not in categories[category]:
        categories[category].append(item_name)
        suma += quantity
        average += quality
print(f'Count of items: {suma}')
print(f'Average quality: {average/len(categories):.2f}')
{print(f"{k} -> {', '.join(v)}") for (k, v) in categories.items()}
