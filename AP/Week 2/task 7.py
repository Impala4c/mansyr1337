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
print("Sorted by frequency:")
m_count2= 0
for i in counter:
    if counter[i]>m_count2:
        m_count2 = counter[i]
for i in range(m_count2,0,-1):
    for j in counter:
        if counter[j]== i:
            print(j,counter[j])