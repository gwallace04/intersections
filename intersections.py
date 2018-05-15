"""
Program that counts the number of interior intersections
"""

import random 

def main():
    list1 = generateRandomPermutaion(7)
    print(list1)
    print(countIntersections(list1))
    
    

def generateRandomPermutaion(n):
    perm_list = list(range(0, n))
    random.shuffle(perm_list)
    first_element = perm_list[0]
    perm_list.append(first_element)
    return perm_list

def countIntersections(perm_list):
    n = len(perm_list) - 1
    ints = 0
    for i in range(len(perm_list) - 1):
        a = min(perm_list[i], perm_list[i + 1])
        b = max(perm_list[i], perm_list[i + 1])
        a_list = list(range(a + 1, b))
        b_list = list(range(b + 1, a + n)) 
        b_list = list(map(lambda x: x % n, b_list))
        inside = a_list if len(a_list) < len(b_list) else b_list        
        outside = list(filter(lambda x: x not in inside and x != a and x != b, perm_list))
        for j in inside:
            v = perm_list.index(j)
            #This has to be in this order or else it will double count end points
            if j == perm_list[0] and perm_list[1] in outside:
                ints += 1 
            elif perm_list[v + 1] in outside:
                ints += 1
            if j == perm_list[0] and perm_list[-2] in outside:
                ints += 1
            elif perm_list[v - 1] in outside:
                ints += 1
    return ints / 2

    
if __name__ == "__main__":
    main()
