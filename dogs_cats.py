def dogs_and_cats():
    N, D, C, M = map(int, raw_input().strip().split())
    S = raw_input().strip()

    for c in S:
        if c == 'D':
            if D == 0 or C < 0:
                return "NO"
            D -= 1
            C += M
        else:
            C -= 1
    return "YES"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, dogs_and_cats())
