import timeit

def urut_ips_mahasiswa(array):
    start = timeit.default_timer()

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j],  array[j + 1] = array[j + 1], array[j]
    
    stop = timeit.default_timer()
    print(f"bubble sort successful! elapsed time: {stop - start}")

    return array

list = [3.8, 2.9, 3.3, 4.0, 2.7]
print ("<=== program mengurutkan IPS mahasiswa ===> ")
print(f"data sebelum diurut  : {list}")
print("setelah diurut(descending) :'", urut_ips_mahasiswa(list))


