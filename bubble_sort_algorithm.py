def sort_using_bubble_sort(records):
    for i in range(0, len(records) - 1):
        for j in range(0, len(records) - 1 - i):
            if records[j] > records[j+1]:
                temp = records[j]
                records[j] = records[j+1]
                records[j + 1] = temp
    return records


numbers = [9, 4, 5, 8, 2, 3]
print(sort_using_bubble_sort(numbers))