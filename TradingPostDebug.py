val = 10
count = 0
aa = 0
a = 4
b = 1
c = 0
d = 0
e = 0
f = 0
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
    print('Resource values only:')
    aa = int(val / a)
    print('A:',aa)
if val <= 0:
    print('Invalid Values.')
if a > 0:
    ax = int(a * aa)
    print('AX:',ax)
    ay = val % a
    if b == 0:
        aa = 0
if b > 1:
    bx = int(ax / b)
    print('B:',bx)
    by = ax % b
    if c == 0:
        bx = 0
if c > 0:
    cx = int(ax / c)
    print('C',cx)
    cy = ax % c
    if b == 0:
        cx = 0
if d > 0:
    dx = int(ax / d)
    print('D',dx)
    dy = ax % d
    if b == 0:
        dx = 0
if e > 0:
    ex = int(ax / e)
    print('E',ex)
    ey = ax % e
    if b == 0:
        ex = 0
if f > 0:
    fx = int(ax / f)
    print('F',fx)
print('')

if val > 0:
    print('Remainder:')
if b > 0:
    by = int(ay / b)
    print('B',by)
if c > 0:
    cy = int(ay / c)
    print('C',cy)
if d > 0:
    dy = int(ay / d)
    print('D',dy)
if e > 0:
    ey = int(ay / e)
    print('E',ey)
if f > 0:
    fy = int(ay / f)
    print('F',fy)

if val > 0:
    print('')
    print('A1', aa)
    print('B1', bx)
    print('C1', cx)
    print('D1', dx)
    print('E1', ex)
    print('B2', by)
    print('C2', cy)
    print('D2', dy)
    print('E2', ey)

    print('')
    print('Total Values: ')
    print('A', aa)
    print('B', bx + by)
    print('C', cx + cy)
    print('D', dx + dy)
    print('E', ex + ey)

    print('Count:',count)
    count = count + aa + bx + cx + dx + ex + by + cy + dy + ey

    print('')
    print('Total trades:')
    print(count)
