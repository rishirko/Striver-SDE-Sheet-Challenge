class Solution:
    def nextPermutation(self, List: List[int]) -> None:
        i=len(List)-1
        first=-1
        while i>0:
            if List[i]>List[i-1]:
                first=i-1
                break
            i-=1.
        if first==-1:
            List.reverse()
        i=len(List)-1
        last=-1
        while i>0:
            if List[first]<List[i]:
                last=i
                break
            i-=1
        f=first
        List[last],List[first]=List[first],List[last]
        print(List)
        temp=List[f+1:]
        temp.sort()
        print(temp)
        i=0
        while f<len(List)-1:
            List[f+1]=temp[i]
            i+=1
            f+=1
