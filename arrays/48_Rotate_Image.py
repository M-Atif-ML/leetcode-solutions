class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        # res = []
        n = len(arr[0])
        for i in range(n):
            for j in range(i+1,n):
                if i != j:
                    arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
        for i in range(n):
            arr[i].reverse()
# time:O(n*n/2) or O(n^2)
# space: O(1)
