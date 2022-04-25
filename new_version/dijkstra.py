#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   glx_dijkstra.py
@Time    :   2022/04/25 16:51:43
@Author  :   glx 
@Version :   1.0
@Contact :   18095542g@connect.polyu.hk
@Desc    :   None
'''

# here put the import lib


# here put the import lib
import os
parent_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(parent_path)
print(os.getcwd())

import numpy as np
import math 
import pandas as pd
import matplotlib.pyplot as plt

class city:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flag = 0

    def reach(self):
        self.flag = 1 
    
    def if_reached(self):
        return self.flag    


class TSP_Solver():
    
    def __init__(self, input_data) -> None:
        self.points = [city(x,y) for x,y in zip(input_data[0], input_data[1])] # 城市坐标
        self.route = []
        self.total_city = len(self.points)
        self.total_length = 0
        self.transfer_matrix = [[0] * self.total_city for _ in range(self.total_city)]
    
    def get_transfer_matrix(self):
        for i in range(self.total_city):
            for j in range(self.total_city):
                if i == j:
                    self.get_transfer_matrix[i][j] = float("inf")
                else:
                    self.get_transfer_matrix[i][j] = math.sqrt(self.points[i].x-self.points[j].x) ** 2 + (self.points[i].y-self.points[j].y) ** 2
        
        return self.get_transfer_matrix
    
    def run():
        pass



    def show_results(self): 
        plt.figure(figsize=(10, 10))
        x_list = [self.points[i].x for i in self.route]
        y_list = [self.points[i].y for i in self.route]
        plt.scatter(x_list, y_list)
        
        for i in range(len(x_list)-1):

            dx = x_list[i+1] - x_list[i]
            dy = y_list[i+1] - y_list[i]
            plt.quiver(x_list[i], y_list[i], dx, dy, angles='xy', scale=1.03, scale_units='xy', width=0.005, color = "b")
        plt.show()

if __name__ == "__main__":
    
    import timeit
    with open(r"data\verify_order_position_10.csv") as f:
        data = pd.read_csv(f,names=['index','lat','lon'])
        city_x = data['lat'].tolist()
        city_y = data['lon'].tolist()
    demo = TSP_Solver([city_x, city_y])
    demo.run()

    # 测试运行时间
    t = timeit.timeit("TSP_Solver([city_x, city_y]).run()", "from __main__ import TSP_Solver", globals=globals(), number=1000)    
    demo.report(t)
