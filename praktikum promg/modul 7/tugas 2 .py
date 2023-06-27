import timeit

def data_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    stop = timeit.default_timer()
    print(f"selection sort seccessful! elapsed time: {stop - start}")

    return array

list = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print("Nama anggota organisasi")
print("data : {list}")
print(f"sorted data :{data_sort(list)}")

