def banana_bunches():
    N, K = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())

    INF = len(B)+1
    dp = {0:0}
    result = INF
    for i in xrange(len(B)):
        curr = 0
        for j in xrange(i, len(B)):
            curr += B[j]
            if curr > K:
                break
            if K-curr not in dp:
                continue
            v = (j-i+1) + dp[K-curr]
            if v < result:
                result = v
        curr = 0
        for j in reversed(xrange(i+1)):
            curr += B[j]
            if curr > K:
                break
            v = i-j+1
            if curr not in dp or dp[curr] > v:
                dp[curr] = v
    return result if result != INF else -1

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, banana_bunches())
