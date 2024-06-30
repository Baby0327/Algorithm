def solution(my_string):
    answer = sum( list( map( int, "".join( [i if i.isdigit() else " " for i in my_string] ).split() ) ) )
    return answer