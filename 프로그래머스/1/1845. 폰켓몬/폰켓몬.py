def solution(nums):
    pkm = len(set(nums))
    choice = len(nums)//2
    return pkm if choice >= pkm else choice