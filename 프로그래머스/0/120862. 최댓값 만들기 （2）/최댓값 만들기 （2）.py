def solution(numbers):
    srt = sorted(numbers)
    return max(srt[0] * srt[1], srt[-1] * srt[-2])