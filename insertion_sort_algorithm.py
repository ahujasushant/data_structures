def sort_using_insertion_sort(records):
    for i in range(1, len(records)):
        j = i - 1
        while records[j] > records[j+1] and j >= 0:
            temp = records[j]
            records[j] = records[j+1]
            records[j + 1] = temp
            j -= 1
    return records


numbers = [9, 4, 5, 8, 2, 3]
print(sort_using_insertion_sort(numbers))