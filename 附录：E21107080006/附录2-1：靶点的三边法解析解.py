import numpy as np
import sympy as sy
import math

x = sy.Symbol('x')
y = sy.Symbol('y')
z = sy.Symbol('z')

anchors = [[0, 0, 1300], [5000, 0, 1700], [0, 5000, 1700], [5000, 5000, 1300]]
clear_distance = [[1320, 3950, 4540, 5760],
                  [3580, 2580, 4610, 3730],
                  [2930, 2600, 4740, 4420],
                  [2740, 2720, 4670, 4790],
                  [2980, 4310, 2820, 4320]]
disturbed_distance = [[2230, 3230, 4910, 5180],
                      [4520, 1990, 5600, 3360],
                      [2480, 3530, 4180, 5070],
                      [4220, 2510, 4670, 3490],
                      [5150, 2120, 5800, 2770]]

def equation(X, Y, Z, dis):
    return (x - X) ** 2 + (y - Y) ** 2 + (z - Z) ** 2 - dis ** 2

def calc_distance(tag, anchor):
    return math.sqrt((tag[0] - anchor[0]) ** 2 + (tag[1] - anchor[1]) ** 2 + (tag[2] - anchor[2]) ** 2)

def compare_result(calc_distance1, calc_distance2, real_distance):
    print("两个疑似点到校验锚点的距离分别为：", calc_distance1, calc_distance2)
    if abs(calc_distance1-real_distance) < abs(calc_distance2-real_distance):
        return [0,calc_distance1,abs(calc_distance1-real_distance)]
    else:
        return [1,calc_distance2,abs(calc_distance2-real_distance)]

#用于确定用哪个distance计算
data_id = 4
#用于确定用哪几个anchors计算
anchor_id1 = 0
anchor_id2 = 2
anchor_id3 = 3

res = sy.solve([equation(anchors[anchor_id1][0], anchors[anchor_id1][1], anchors[anchor_id1][2], clear_distance[data_id][anchor_id1]),
                equation(anchors[anchor_id2][0], anchors[anchor_id2][1], anchors[anchor_id2][2], clear_distance[data_id][anchor_id2]),
                equation(anchors[anchor_id3][0], anchors[anchor_id3][1], anchors[anchor_id3][2], clear_distance[data_id][anchor_id3])],
               [x, y, z])

rest_anchor = list(set([0, 1, 2, 3]) - set([anchor_id1, anchor_id2, anchor_id3]))[0]
print("校验锚点是",rest_anchor)

minium_distance = compare_result(calc_distance(res[0], anchors[rest_anchor]),
                                calc_distance(res[1], anchors[rest_anchor]),
                                clear_distance[data_id][rest_anchor])[1]

minium_tag = compare_result(calc_distance(res[0], anchors[rest_anchor]),
                            calc_distance(res[1], anchors[rest_anchor]),
                            clear_distance[data_id][rest_anchor])[0]

distance_error = compare_result(calc_distance(res[0], anchors[rest_anchor]),
                            calc_distance(res[1], anchors[rest_anchor]),
                            clear_distance[data_id][rest_anchor])[2]

print("实际的坐标是",float('%.2f' % res[minium_tag][0]),float('%.2f' % res[minium_tag][1]),float('%.2f' % res[minium_tag][2]),
      "到校验点的距离误差是",distance_error)

print(float('%.2f' % res[0][0]), " ", float('%.2f' % res[0][1]), " ", float('%.2f' % res[0][2]))
print(float('%.2f' % res[1][0]), " ", float('%.2f' % res[1][1]), " ", float('%.2f' % res[1][2]))