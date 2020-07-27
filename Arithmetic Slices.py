class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if(len(A)<3):
            return 0
        diff = A[1]-A[0]
        seq = [0 for _ in range(len(A))]
        seq[0] = 0
        seq[1] = 1
        count = 0
        for i in range(2,len(A)):
            if(A[i]-A[i-1]==diff and seq[i-1]>=1):
                seq[i] = seq[i-1]+1
                count+=seq[i]-1
            else:
                diff = A[i]-A[i-1]
                seq[i] = 1
                seq[i-1] =0
            # print(seq)       
        return count