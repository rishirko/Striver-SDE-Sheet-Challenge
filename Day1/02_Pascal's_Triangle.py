#Rishi's Solution

# take a 2D dummy array to store the values as expected in output.
# initialize the dummy with [[1]] for input=1 or [[1],[1,1]]  for input=2.
# now the real solution is for input greater than or equal to 3.
# now for every value we will append a temp_array to dummy.
# take a temp_array with all its element =1.
# and traverse the prev array to take sum of every 2 elemet and keep updating temp. then after calculating temp, append it to dummy.

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dummy=[[1]]
        if n==1:
            return dummy
        dummy=[[1],[1,1]]
        if n==2:
            return dummy
        for i in range(3,n+1):
            temp=[1]*i
            x=1
            for j in range(len(dummy[i-2])-1):
                temp[x]=dummy[i-2][j]+dummy[i-2][j+1]
                x+=1
            dummy.append(temp)
        return dummy
        
        
                
