class ListNone:
    def __init__(self, x):
        self.val = x
        self.next = None

class Merge_prac(object):

    @staticmethod
    def merge_prac(param: []):
        arr = param
        if len(arr) < 2 : # 재귀호출을 하는 경우 블레이크 가 필요하다
            return arr
        mid = len(arr) // 2 # 배열을 쪼갤 pivot 설정
        arr1 = Merge_prac.merge_prac(arr[:mid]) # 재귀호출을 통해 계속 쪼갠다
        arr2 = Merge_prac.merge_prac(arr[mid:])
        merge_sum = []
        i = j = 0 # 인덱스 번호를 계속 초기화 해준다
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merge_sum.append(arr1[i])
                i += 1
            else:
                merge_sum.append(arr2[j])
                j += 1
        merge_sum += arr1[i:]
        merge_sum += arr2[j:]
        return merge_sum

    def merge_case2(self, l1: ListNone, l2: ListNone) -> ListNone:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1




