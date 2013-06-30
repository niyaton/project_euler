nums = []
for line in open('input').readlines():
    nums.append([ int(i) for i in line.split(' ') ])

def get_products():
    for x in range(20):
        for y in range(20):
            p = [1, 1, 1, 1]
            for i in range(4):
                p[0] *= nums[x][y+i] if y + i < 20 else 0
                p[1] *= nums[x+i][y] if x + i < 20 else 0
                p[2] *= nums[x+i][y+i] if x + i < 20 and y + i < 20 else 0
                p[3] *= nums[x-i][y+i] if x - i >= 0 and y + i < 20 else 0
            for i in p:
                yield i

print max(get_products())
