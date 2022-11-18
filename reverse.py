class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x>0):
            Y=[]
            j=10
            k=0

            while(x>0):
                r=x%j
                Y.append(r)
                x=(x-r)/j

            m=len(Y)
            for i in range(len(Y)):
                m=m-1
                k=k+(10**m)*Y[i]

            if k >= 2 ** 31 - 1 or k <= -2 ** 31:
                return 0
            else: return int(k)

        elif(x<0):
            x=-x
            Y=[]
            j=10
            k=0

            while(x>0):
                r=x%j
                Y.append(r)
                x=(x-r)/j

            m=len(Y)
            for i in range(len(Y)):
                m=m-1
                k=k+(10**m)*Y[i]

            if k >= 2 ** 31 - 1 or k <= -2 ** 31:
                return 0
            else: return int(-k)

        elif(x==0):
            return 0
