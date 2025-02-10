#def remove_element(nuns, val):
#    k = 0

#    for i in range(len(nuns)):
#        if nuns[i] != val:
  #          nuns[k] = nuns[i]
   #         k += 1

   # return k

#nums = [3, 2, 2, 3]
#val = 3
#k = remove_element(nums, val)
#print(k)
#print(nums[:k])

class Solution:
    def removeElement(self, nums, val):
        k = 0  # Contador para o número de elementos que não são iguais a val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Mover o elemento para a posição k
                k += 1  # Incrementar o contador

        return k  # Retornar o número de elementos que não são iguais a val

# Exemplo de uso
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  # Saída: 2
print(nums[:k])  # Saída: [2, 2]
