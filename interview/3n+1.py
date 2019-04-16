"""
一个数n
若为奇数3n+1
若为偶数n/2
得到1 需要几步
"""

def main():
    def n31(a):# a = initial number
        c = 0
        l = [a]
        while a != 1:
            if a % 2 == 0:#if even divide it by 2
                a = a // 2
            elif a % 2 == 1:#if odd 3n+1
                a = 3*a +1
            c += 1#counter
            l += [a]

        return l , c
    print(n31(43))
    
    print(n31(98))
    print(n31(98)[0][-1])# = a
    
    print(n31(13))
    print("It took {0} steps.".format(n31(13)[1]))#optional finish

if __name__ == '__main__':
    main()
    
    
# ([43, 130, 65, 196, 98, 49, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 29)
# ([98, 49, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 25)
# 1
# ([13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 9)
# It took 9 steps.
