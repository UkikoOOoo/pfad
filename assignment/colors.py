import numpy as np

def hsl_to_hex(h, s, l):
    """Convert HSL to HEX color."""
    c = (1 - abs(2 * l - 1)) * s
    h_prime = h / 60
    x = c * (1 - abs(h_prime % 2 - 1))
    m = l - c / 2
    
    if 0 <= h_prime < 1:
        r, g, b = c, x, 0
    elif 1 <= h_prime < 2:
        r, g, b = x, c, 0
    elif 2 <= h_prime < 3:
        r, g, b = 0, c, x
    elif 3 <= h_prime < 4:
        r, g, b = 0, x, c
    elif 4 <= h_prime < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return f'#{r:02X}{g:02X}{b:02X}'

def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = (i * 360 / num_colors) % 360  # 使色相均匀分布
        saturation = 0.9  # 饱和度
        lightness = 0.5 + (0.5 * (i % 2)) * 0.2  # 随机的明度，可以变化
        hex_color = hsl_to_hex(hue, saturation, lightness)
        colors.append(hex_color)
    return colors

# 生成100种颜色
num_colors = 44
color_list = generate_colors(num_colors)

# 打印结果
for color in color_list:
    print(color)