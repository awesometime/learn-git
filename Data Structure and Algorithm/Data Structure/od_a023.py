"""
https://blog.csdn.net/2401_86417859/article/details/140936169
一个图像有n个像素点，存储在一个长度为n的数组img里，每个像素点的取值范围[0,255]的正整数。
请你给图像每个像素点值加上一个整数k（可以是负数），得到新图newImg，使得新图newImg的所有像素平均值最接近中位值128。
请输出这个整数k
备注
• 1 <= n <= 100
• 如有多个整数k都满足，输出小的那个k；
• 新图的像素值会自动截取到[0,255]范围。当新像素值<0，其值会更改为0；当新像素值>255，其值会更改为255；

例如newImg=”-1 -2 256″,会自动更改为”0 0 255″

解题思路
计算初始平均值：首先计算输入像素点的初始平均值。
寻找合适的k：为了使新图像的平均值最接近128，我们需要计算每个像素加上k后的值，并限制在[0, 255]范围内。
计算最佳k：通过遍历可能的k值，找到使新平均值最接近128的k，并在有多个k满足条件时选择最小的k。
"""

import sys

old_image = []
for line in sys.stdin:
    old_image = line.split()
n = len(old_image)
best_k_value = float("-255")
best_avg_value = float("256")
for k in range(-255, 256):
    new_image_sum = 0
    for old_value in old_image:
        new_value = int(old_value) + k
        new_value = max(0, min(new_value, 255))
        new_image_sum += new_value
    new_avg = new_image_sum / n
    cur_avg = abs(new_avg - 128)
    if cur_avg < best_avg_value or (cur_avg == best_avg_value and k < best_k_value):
        best_avg_value = cur_avg
        best_k_value = k
print(best_k_value)
