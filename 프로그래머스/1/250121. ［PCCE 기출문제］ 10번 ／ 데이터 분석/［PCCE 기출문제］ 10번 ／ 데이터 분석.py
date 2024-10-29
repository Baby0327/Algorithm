def solution(data, ext, val_ext, sort_by):
    l = ["code", "date", "maximum", "remain"]
    answer = sorted([i for i in data if i[l.index(ext)] < val_ext], key=lambda x : x[l.index(sort_by)])
    return answer