

                #Answer ---------- 1

def isPowerOfTwo(n):
    if n <= 0:
        return False

    while n > 1:
        if n % 2 == 1:
            return False
        n = n // 2

    return True


print(isPowerOfTwo(1))    # Output: True
print(isPowerOfTwo(16))   # Output: True
print(isPowerOfTwo(3))    # Output: False







def sumOfNaturalNumbers(n):
    return (n * (n + 1)) // 2

print(sumOfNaturalNumbers(3))    # Output: 6
print(sumOfNaturalNumbers(5))    # Output: 15




                    #Answer ---------- 2


def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

print(factorial(5))    # Output: 120
print(factorial(4))    # Output: 24



                    #Answer ---------- 3



def exponentiation(N, P):
    return N ** P


print(exponentiation(5, 2))    # Output: 25
print(exponentiation(2, 5))    # Output: 32








                        #Answer ---------- 4




def exponentiation(N, P):
    return N ** P

print(exponentiation(5, 2))    # Output: 25
print(exponentiation(2, 5))    # Output: 32


                    #Answer ---------- 5




def findMax(arr, index):
    # Base case: If the index is at the last element of the array
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive case: Compare the current element with the maximum element of the remaining array
    return max(arr[index], findMax(arr, index + 1))

arr = [1, 4, 3, -5, -4, 8, 6]
print(findMax(arr, 0))    # Output: 8

arr = [1, 4, 45, 6, 10, -8]
print(findMax(arr, 0))    # Output: 45



        
                    #Answer ---------- 6


def findNthTerm(a, d, N):
    return a + (N - 1) * d
print(findNthTerm(2, 1, 5))    # Output: 6
print(findNthTerm(5, 2, 10))   # Output: 23





                #Answer ---------- 7

def permute(s, left, right):
    if left == right:
        print("".join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]
            permute(s, left + 1, right)
            s[left], s[i] = s[i], s[left]  # backtrack

def printPermutations(S):
    s = list(S)
    permute(s, 0, len(s) - 1)


printPermutations("ABC")
# Output: ABC, ACB, BAC, BCA, CBA, CAB

printPermutations("XY")
# Output: XY, YX




                #Answer ---------- 8


def productOfArrayElements(arr):
    product = 1
    for num in arr:
        product *= num
    return product


print(productOfArrayElements([1, 2, 3, 4, 5]))    # Output: 120
print(productOfArrayElements([1, 6, 3]))          # Output: 18






















