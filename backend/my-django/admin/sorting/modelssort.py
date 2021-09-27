from dataclasses import dataclass


class Sorting(object):

    random_array : []

    @property
    def random_array(self) -> []: return self._random_array

    @random_array.setter
    def random_array(self, random_array): self._random_array = random_array


    def bubble_sort(self):
        n = len(self.random_array)
        arr = self.random_array
        for i in range(n-1): #앞으로 전진하는 카운트
            for j in range(n-i-1): #
                if self.random_array[j] > self.random_array[j+1]:
                    self.random_array[j],self.random_array[j+1] = self.random_array[j+1], self.random_array[j]
        return arr

    @staticmethod
    def merge_sort(param: []):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        arr1 = Sorting.merge_sort(arr[:mid])
        arr2 = Sorting.merge_sort(arr[mid:])
        merge_arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merge_arr.append(arr1[i])
                i += 1
            else:
                merge_arr.append(arr2[j])
                j += 1
        merge_arr += arr1[i:]
        merge_arr += arr2[j:]
        return merge_arr


    @staticmethod
    def quick_sort(param: []):
        arr = param
        if len(arr) <= 1:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], []
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)


