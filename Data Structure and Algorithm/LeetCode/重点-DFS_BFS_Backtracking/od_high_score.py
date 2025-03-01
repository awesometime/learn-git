"""
https://blog.csdn.net/hxyh888/article/details/144686438
3344567

单张       n
两张 三张  2*n*2  3*n*2
五顺      (n1..n5)*2
四炸      4*n*3
"""

cards = "33445677"
# 不同牌出现次数,第一个值无用
card_count = [0] * 14
# 牌张数
total_card_count = 0

# 牌面值转数值
for char in cards:
    total_card_count += 1
    if char == '0':
        card_count[10] += 1
    elif char == 'J':
        card_count[11] += 1
    elif char == 'Q':
        card_count[12] += 1
    elif char == 'K':
        card_count[13] += 1
    else:
        card_count[int(char)] += 1
cur_card_index = 1
max_high_score = 0


def high_score(total_card_count, card_count, cur_card_index, score):
    global max_high_score
    if total_card_count == 0:
        if max_high_score < score:
            max_high_score = score
        return
    while cur_card_index <= 13 and card_count[cur_card_index] == 0:
        cur_card_index += 1
    if cur_card_index > 13:
        return
    if card_count[cur_card_index] >= 1:
        if cur_card_index <= 9:
            canPlay = True
            for i in range(5):
                if card_count[cur_card_index + i] <= 0:
                    canPlay = False
                    break
            if canPlay:
                for i in range(5):
                    card_count[cur_card_index + i] -= 1
                extra_score = (5 * cur_card_index + 10) * 2
                high_score(total_card_count - 5, card_count, cur_card_index, score + extra_score)
                for i in range(5):
                    card_count[cur_card_index + i] += 1
    card_count[cur_card_index] -= 1
    high_score(total_card_count - 1, card_count, cur_card_index, score + cur_card_index)
    card_count[cur_card_index] += 1
    i = 2
    while (i <= 4):
        if card_count[cur_card_index] <= i:
            card_count[cur_card_index] -= i
            if i == 4:
                high_score(total_card_count - i, card_count, cur_card_index, score + cur_card_index* i * 3)
            else:
                high_score(total_card_count - i, card_count, cur_card_index, score + cur_card_index* i * 2)
            card_count[cur_card_index] += i
        i+=1

print(card_count)
#[0, 0, 0, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0]
high_score(total_card_count, card_count, cur_card_index, 0)
