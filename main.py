# y'=(y^3 + x + 1) / (3y^2), y(0) = -1.24, (0 <= x <= 8)

def f(x, y):
    return (y ** 3 + x + 1) / (3 * y ** 2)


def euler_method(f, x0, y0, x_end, h):
    x = x0
    y = y0
    result = [(x, y)]
    while x <= x_end:
        y = y + h * f(x, y)
        x = x + h
        result.append((x, y))
    return result


x0 = 0
y0 = -1.24
x_end = 8
h = 0.1

result = euler_method(f, x0, y0, x_end, h)

for elem in result:
    print(elem, end='\n')
