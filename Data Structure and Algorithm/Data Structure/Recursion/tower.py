class Recursion():
    def __init__(self):
        pass

    def moveTower(self, height, fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height - 1, fromPole, withPole, toPole)
            self.moveDisk(fromPole, toPole)

            self.moveTower(height - 1, withPole, toPole, fromPole)

    def moveDisk(self, fp, tp):
        global i
        i += 1
        print(str(i) + " moving disk from", fp, "to", tp)

    # i = 0
    # moveTower(4, "1", "2", "3")
    # print(i)

    def recMC(self, coinValueList, change):
        global count
        count += 1
        minCoins = change
        if change in coinValueList:
            return 1
        else:
            for i in [c for c in coinValueList if c <= change]:
                numCoins = 1 + self.recMC(coinValueList, change - i)
                if numCoins < minCoins:
                    minCoins = numCoins
        return minCoins

    # count = 0
    # print(recMC([1,5,10,25],63))   # count 67716925
    # print(recMC([1,5,10,25],26)) # 2
    # print(count) # count 377
    # print(recMC([1,5,10,25],25))   # count 1
    # print(count)
    # print(recMC([1,5,10,25],1))   # count 1
    # print(count)
    # print(recMC([1,5,10,25],16))   # count 62
    # print(count)
    # print(recMC([1,5,10,25],21))   # count 312
    # print(count)

    def recDC_2(self, coinValueList, change, knownResults):
        global count2
        count2 += 1
        minCoins = change
        if change in coinValueList:
            knownResults[change] = 1
            return 1, knownResults
        # 前边找过最小找零次数的change 直接返回
        elif knownResults[change] > 0:
            return knownResults[change], knownResults
        else:
            for i in [c for c in coinValueList if c <= change]:
                numCoins = 1 + self.recDC_2(coinValueList, change - i,
                                            knownResults)[0]
                if numCoins < minCoins:
                    minCoins = numCoins
                    knownResults[change] = minCoins
        return minCoins, knownResults
        # 递归总次数不等于 knownResults 各项加起来

if __name__ == "__main__":
    """1 """
    for j in range(1,51):
        rec1 = Recursion()
        count2 = 0
        print("min_change_num "+str(rec1.recDC_2([1, 5, 10, 25], j, [0] *(j+1) )[0]))
        print("recursion_count " + str(count2))

        knownResults = rec1.recDC_2([1, 5, 10, 25], j, [0] * (j+1))[1]
        sum = 0
        for i in range(len(knownResults)):
            sum += knownResults[i]
        print(f"knownResults--len({len(knownResults)})--  " +str(sum))
        print(knownResults)
        print("---")

    """2 """
    min_change_num_list = []
    recursion_count_list = []
    for i in range(1, 27):
        rec = Recursion()
        count2 = 0
        min_change_num = rec.recDC_2([1, 5, 10, 25], i, [0] * (i + 1))[0]
        # print(rec.recDC_2([1,5,10,25],i,[0]*(i+1))[0])
        recursion_count_list.append(count2)
        min_change_num_list.append(min_change_num)
        # print(f"{i} --> {count2}")
    print("min_change_num_list")
    print(min_change_num_list)
    print("recursion_count_list")
    print(recursion_count_list)

