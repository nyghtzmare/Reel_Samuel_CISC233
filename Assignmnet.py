class buble_sort:
    def __init__(self):
        self.sorted = True

    def sort(self, l_list):
        for x in range(len(l_list)-1, 0, -1):
            self.sorted = True
            for i in range(x):
                if l_list[i] > l_list[i+1]:
                    holder = l_list[i]
                    l_list[i]  = l_list[i+1]
                    l_list[i+1] = holder
                    self.sorted = False

            if self.sorted == True:
                break


        return l_list

call = buble_sort()
print call.sort([9, 2, 5, 6, 1, 8, 0, 7, 3, 10])
print call.sort([1, 2, 3, 4, 6, 5, 7, 8, 9, 10])