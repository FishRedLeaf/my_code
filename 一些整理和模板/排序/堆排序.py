# https://www.cnblogs.com/chengxiao/p/6129630.html

def heapify(unsorted, index, heap_size):
    largest = index
    print(unsorted, largest, heap_size)
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        # 此时，index对应的节点一定比左右节点大，但是需要对调整后的largest节点进行heapify，使这个节点也满足大顶堆性质
        # 调整大顶堆从下往上，从左往右调整。
        # 例如，4,6,8,5,9->4,9,8,5,6；顶点9本身满足比左右子节点大，但是右节点交换过了，需要对这个交换过的子节点heapify
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    # 构造初始大顶堆，从第一个非叶子节点到根节点，将每个节点都调整为左右子节点中最大的
    for i in range(n // 2 - 1, -1, -1):
        print('###')
        heapify(unsorted, i, n)
    # 每次只需要将顶部元素调整为最大
    for i in range(n - 1, 0, -1):
        print('***')
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

print(heap_sort([4,6,8,5,9]))

'''
4,6,8,5,9
###
[4, 6, 8, 5, 9] 1 5
[4, 9, 8, 5, 6] 4 5
###
[4, 9, 8, 5, 6] 0 5
[9, 4, 8, 5, 6] 1 5
[9, 6, 8, 5, 4] 4 5
***
[4, 6, 8, 5, 9] 0 4
[8, 6, 4, 5, 9] 2 4
***
[5, 6, 4, 8, 9] 0 3
[6, 5, 4, 8, 9] 1 3
***
[4, 5, 6, 8, 9] 0 2
[5, 4, 6, 8, 9] 1 2
***
[4, 5, 6, 8, 9] 0 1
[4, 5, 6, 8, 9]
'''