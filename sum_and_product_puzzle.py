# The following code solves the sum-product puzzle.
# Taken verbatim from
# https://en.wikipedia.org/wiki/Sum_and_Product_Puzzle.

# X and Y are two different whole numbers greater than 1. Their sum is
# not greater than 100, and Y is greater than X. S and P are two
# mathematicians (and consequently perfect logicians); S knows the sum
# X + Y and P knows the product X × Y. Both S and P know all the
# information in this paragraph.

# The following conversation occurs:

# S says "P does not know X and Y." (1)
# P says "Now I know X and Y." (2)
# S says "Now I also know X and Y." (3)
# What are X and Y?

# 
# Let S be the sum and P the product.

# (1) means that there is no way to write S as a sum of two
# primes. (Could it mean MORE?)

# (2) means that there is exactly one factorization WZ=P such that W+Z
# is not a sum of primes

# (3) means that there is only one way to write S as a sum of two
# numbers S = A+B such that the product AB has only one factorization
# RS=AB such that R+S is not a sum of primes

import numpy as np


#Pseudocode
# For each possible sum s=3,4...100
#   If s is not a sum of two primes:
#     Initialize root labeled s of tree.
#     Create child (a,b) of s for each pair 1<a<b s.t. a+b = s.
#     For each factorization  wz=ab with 1<w<z:
#       If w+z<=100 and w+z not a sum of two primes:
#         Create child (w,z) of (a,b)
#   If there is exactly one node (a,b) with exactly one child (w,z):
#     s=a+b works!


# For expediency, the procedure below uses a preset list of primes. Taken from
# https://miniwebtool.com/list-of-prime-numbers/?to=1000
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
          137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
          283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
          379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
          461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
          563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
          739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827,
          829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
          937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# The procedure below also checks if a number is a sum of two primes.
prime_pairs_sums = set([p+q for p in primes for q in primes if p<q])




success_flag = False
s=2
while s<=100 and success_flag == False:
    if s not in prime_pairs_sums:
        solution_tree = {s:dict()} #use dictionary to encode a tree,
                                   #leaves are stored in a list for
                                   #readability of SOLUTION_TREE
        s_children_with_unique_child = 0
        for a in range(2, s//2 + 1): 
            b =s-a
            if a<b: 
                solution_tree[s][str(a) + ' + ' + str(b) + ' = ' +str(s)]=[]
                a_b_children=0
                for w in range(2,int((a*b)**0.5)+1):
                    if (a*b) % w ==0:
                        z = (a*b) // w
                        if w+z<= 100 and w+z not in prime_pairs_sums:
                            solution_tree[s][str(a) + ' + ' + str(b) +
                                             ' = ' +
                                             str(s)].append([str(w) +
                                                             ' * ' + str(z) + ' = ' +
                                                             str(a) + ' * ' + str(b)])
                            a_b_children += 1
                if a_b_children == 1:
                    s_children_with_unique_child +=1
                    correct_a = a
                    correct_b = b
        if s_children_with_unique_child == 1 and len(solution_tree[s])>1:
            success_flag = True
            print(s,'=',correct_a,'+',correct_b, 'works!')
    s+=1


    
