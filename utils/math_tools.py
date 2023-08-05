'''
这个文件放的都是数学公式
'''
import math

def solve_quadratic_equation(a, b, c):
    '''
    方法名称：solve_quadratic_equation
    功能：计算二元一次方程的不同的实数根
    参数：a,b,c
    返回值：方程的实数根
        
    '''
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return None  # 返回 None 表示没有实数根（虚根）

