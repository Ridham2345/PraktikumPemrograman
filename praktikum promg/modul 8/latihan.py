def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower == keyword.lower():
            print(f"keyword{keyword} has found indeks {i}") 
            return i
        
    print(f"keyword{keyword}`not found!")
    return -1

data = [35, 8, 45, 23, 62, 26, 46]


def bubble_sort(data):
    for i in range (len(data)):
        for j in range (len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def binary_search(keyword,data):
    sorted_data = bubble_sort(data)
    print(f"data (sorted) = {sorted_data}")
    left = 0
    right =len(sorted_data) - 1
    while left <= right :
        mid = (left  + right)//2
        str_data = str(sorted_data[mid]).lower()
        if str_data > keyword.lower() :
            right = mid - 1
        elif str_data < keyword.lower():
            left = mid + 1
        else:
            print (f"keyword {keyword} has found at  indeks {mid}:")
            return mid
        
   
    print (f"keyword {keyword} not found")
    return - 1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("input keyword : ")
binary_search(keyword,data)
            
def linear_search(keyword,data):
    for i in range (len(data)):
        if str (data[i]).lower() == keyword.lower():
            print(f"keyword {keyword} has found at index(3)")
            return i
    print(f"keyword {keyword} not found")
    return - 1

data= [23,3,4,78,9,10,32]
keyword = input("input keyword: ")
linear_search(keyword,data)


def linear_search(keyword,data):
    for i in range (len(data)):
        if str (data[i]).lower() == keyword.lower():
            print(f"keyword {keyword} has found at index(3)")
            return i
    print(f"keyword {keyword} not found")
    return - 1

data= [23,3,4,78,9,10,32]
keyword = input("input keyword: ")
linear_search(keyword,data)


def linear_search(keyword,data):
    for i in range (len(data)):
        if str (data[i]).lower() == keyword.lower():
            print(f"keyword {keyword} has found at index(3)")
            return i
    print(f"keyword {keyword} not found")
    return - 1

data= [23,3,4,78,9,10,32]
keyword = input("input keyword: ")
linear_search(keyword,data)



def bubble_sort(data):
    for i in range (len(data)):
        for j in range (len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def binary_search(keyword,data):
    sorted_data = bubble_sort(data)
    print(f"data (sorted) = {sorted_data}")
    left = 0
    right =len(sorted_data) - 1
    while left <= right :
        mid = (left  + right)//2
        str_data = str(sorted_data[mid]).lower()
        if str_data > keyword.lower() :
            right = mid - 1
        elif str_data < keyword.lower():
            left = mid + 1
        else:
            print (f"keyword {keyword} has found at  indeks {mid}:")
            return mid
        
   
    print (f"keyword {keyword} not found")
    return - 1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("input keyword : ")
binary_search(keyword,data)