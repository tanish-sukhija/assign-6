class SumToZero:
    def __init__(self, arr):
        self.arr = arr

    def find_triplets(self):
        triplets = []
        arr = self.arr
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                if s == 0:
                    triplets.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
print(SumToZero(arr).find_triplets())