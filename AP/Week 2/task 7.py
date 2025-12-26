def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


items = input().split()
counter = {}
for i in items:
    if i in counter:
        counter[i]+=1
    else:
        counter[i] = 1
print("Purchase Frequency:")
m_product = 0
m_count = 0
for i in counter:
    if counter[i]>m_count:
        m_count = counter[i]
        m_product = i
        
print("Most popular item:",m_product)
print("Purchased Once:")
for i in counter:
    if counter[i]== 1:
        print(i)
freq_list = list(counter.items())
print("Sorted by frequency:")
sorted_items = merge_sort(freq_list)
for item, count in sorted_items:
    print(item, count)
