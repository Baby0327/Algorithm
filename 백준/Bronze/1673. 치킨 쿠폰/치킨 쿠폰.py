"""
치킨 쿠폰
"""

import sys

while True:
    try:
        n, k = map(int, input().split())
        stamp = n * k
        chicken = 0

        while stamp >= k:
            chicken += stamp // k
            stamp = stamp % k + stamp // k

        sys.stdout.write(str(chicken) + "\n")
    except:
        break