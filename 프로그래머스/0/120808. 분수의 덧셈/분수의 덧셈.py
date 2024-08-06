def solution(numer1, denom1, numer2, denom2):
    top = numer1*denom2 + numer2*denom1
    bottom = denom1*denom2
    i = 2
    
    while i <= min(denom1, denom2):
        if top % i == 0 and bottom % i == 0:
            top //= i
            bottom //= i
        else:
            i += 1
            
    return [top, bottom]