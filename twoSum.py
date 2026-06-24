class Brute:
    def find_indices(self, numbers, target):
        total_num = len(numbers)
        for i in range(total_num):
            for second_index in range(i+1,total_num):
                if numbers[i]+numbers[second_index]==target:
                    return [i,second_index] 
                
                
class Brut:
    def find_ind(self,numbers, target):
        n= len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i]+ numbers[j] ==target:
                    return [i,j]
                
class BetterTwoSum:
    #sorting then pointers
    def find_ind(self,numbers, target):
        indexed_numbers = [(value,index) for index, value in enumerate(numbers)]
        indexed_numbers.sort()
        left, right=0, len(indexed_numbers)-1
        
        while left<right:
            current_sum= indexed_numbers[left][0] + indexed_numbers[right][0]
            if current_sum ==target: 
                return indexed_numbers[left][1], indexed_numbers[right][1]
            if current_sum<target:
                left +=1
            else: 
                right-=1
                

                
if __name__ =="__main__":
    solver=BetterTwoSum()
    print(solver.find_ind([2,7,11,15],9))


