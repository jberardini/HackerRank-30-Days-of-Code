def bubble_sort(arr):
    num_swaps = 0
        
    for i in range(len(arr)-1, 0, -1):
        counter = 0
        for n in range(i):
            if arr[n] > arr[n+1]:
                counter += 1
                arr[n], arr[n+1] = arr[n+1], arr[n]
        if counter == 0:
            break
        else:
            num_swaps += counter
            print num_swaps
        
    print "Array is sorted in {} swaps.".format(num_swaps)
    print "First element: {}".format(arr[0])
    print "Last element: {}".format(arr[-1])


print bubble_sort([3,2,1])