nums = []
for line in open('input').readlines():
    line = line.strip()
    nums.append([ int(i) for i in line.split(' ') ])

products = []
for x in range(20):
    for y in range(20):
        p = [1, 1, 1, 1]
        for i in range(4):
            if y + i >= 20:
                p[0] = 0
            else:
                p[0] *= nums[x][y+i]
            if x + i >= 20:
                p[1] = 0
            else:
                p[1] *= nums[x+i][y]
            if x + i >= 20 or y + i >= 20:
                p[2] = 0
            else:
                p[2] *= nums[x+i][y+i]
            if x - i< 0 or y + i >= 20:
                p[3] = 0
            else:
                p[3] *= nums[x-i][y+i]
        products.extend(p)

print max(products)

