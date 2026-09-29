arr = [1, 2, 3, 4, 2 , 4 , 5 , 1 , 6 , 3]
duplicates = []
seen = set()
for num in arr:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)