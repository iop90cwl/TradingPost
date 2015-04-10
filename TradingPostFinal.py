val = 836
count = 0
aa = 0
a = 180
b = 36
c = 12
d = 4
e = 2
f = 1
ax = 0
bx = 0
cx = 0
dx = 0
ex = 0
fx = 0
gx = 0
ay = 0
by = 0
cy = 0
dy = 0
ey = 0
fy = 0


count = count + 1 #Adds 1 to the total trades for first trade
if a > 0:
    aa = int(val / a)
if val <= 0:
    print('Invalid Values.')
if a > 0:
    ax = int(a * aa)
    ay = val % a
    if b == 0:
        aa = 0
if b > 0:
    bx = int(ax / b)
    by = ax % b
    if c == 0:
        bx = 0
if c > 0:
    cx = int(ax / c)
    cy = ax % c
    if b == 0:
        cx = 0
if d > 0:
    dx = int(ax / d)
    dy = ax % d
    if b == 0:
        dx = 0
if e > 0:
    ex = int(ax / e)
    ey = ax % e
    if b == 0:
        ex = 0
if f > 0:
    fx = int(ax / f)

if b > 0:
    by = int(ay / b)
if c > 0:
    cy = int(ay / c)
if d > 0:
    dy = int(ay / d)
if e > 0:
    ey = int(ay / e)
if f > 0:
    fy = int(ay / f)

if val > 0:
    count = count + aa + bx + cx + dx + ex + by + cy + dy + ey
    print(count)
