import math

# 从用户那里获取AB和CD的长度
AB = float(input())
CD = float(input())

# 计算AD的长度
AD = AB / 2

# 计算圆的半径OA
OA = (AD**2 + CD**2) / (2 * CD)

# 计算圆心角∠AOB
sin_angle_half = AD / OA
angle_AOB = 2 * math.degrees(math.asin(sin_angle_half))

# 计算扇形AOB的面积
sector_area = (angle_AOB / 360) * math.pi * OA**2

# 计算三角形△AOB的面积
triangle_area = 0.5 * OA**2 * math.sin(math.radians(angle_AOB))

# 计算弓形ABC的面积
arch_area = sector_area - triangle_area

# 输出结果，保留两位小数
print(f"{arch_area:.2f}")