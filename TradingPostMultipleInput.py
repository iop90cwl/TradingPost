runs = int(input('Input number of tests: '))
print('')

while runs != 0: #Loop for multiple runs
    print('Input values below. If there are less than 6 resource values, input unneeded value inputs as zero.')
    print('')
    val = int(input('Input total item value: '))
    count = 0
    aa = 0
    a = int(input('Input first resource value: ')) #First resource value (Diamond)
    b = int(input('Input second resource value: ')) #Second resource value (Iron)
    c = int(input('Input third resource value: ')) #Third resource value (Coal)
    d = int(input('Input fourth resource value: ')) #Fourth resource value (Cobblestone)
    e = int(input('Input fifth resource value: ')) #Fifth resource value (Wood)
    f = int(input('Input final resource value: ')) #Sixth resource value (Dirt)
    #Program can be repeated as needed for more resources, it currently has 6

#Running values for initial integer division
    ax = 0 
    bx = 0
    cx = 0
    dx = 0
    ex = 0
    fx = 0
    gx = 0

#Running values for remainder
    ay = 0
    by = 0
    cy = 0
    dy = 0
    ey = 0
    fy = 0


    count = count + 1 #Adds 1 to the total trades for first trade
    if a > 0:
        aa = int(val / a) #Whole value divided by first resource value, with no remainder
    if a > 0:
        ax = int(a * aa)
        ay = val % a #Takes remainder and deals with it below at 'ay'
        if b == 0:
            aa = 0 #Sets aa to zero if b is zero
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
    if val <= 0:
        print('Invalid Value(s). Try again.')#If total item value is zero, it stops the program
        runs = runs - 1
    if val > 0:
        count = count + aa + bx + cx + dx + ex + by + cy + dy + ey #Adds total trades plus initial trade
        print('')
        if count == 1:
            print('It will take',count,'trade to convert your item into dirt blocks.')#1 = TRADE
        elif count > 1:
            print('It will take',count,'trades to convert your item into dirt blocks.')#2 or more = TRADES
    runs = runs - 1
    print('')
    print('---------------------------------------------------------------------------') #Separator between runs
    print('')
