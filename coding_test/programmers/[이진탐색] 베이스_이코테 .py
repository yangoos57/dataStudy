### 떡볶이 떡 만들기 
# https://www.youtube.com/watch?v=94RC-DsGMLo

# 이진탐색 기본

def bin_search(len_d,search_num,items) :
    # idx 
    left = 0
    right = max(items)

    # left > right 종료
    while left <= right :
        middle = (left+right) // 2
        print(left,middle,right)

        # 조건 생성하기
        rest = 0
        for d in items :
            if d - middle > 0 :
                rest += d-middle
        
        # 조건이 맞다면 최적화 
        # S > M
        if search_num > rest :
            right = middle - 1
        # S < M
        elif search_num < rest :
            left = middle + 1
        # S = M
        else :
            return middle
    return -1

print(bin_search(4,6,[19,15,10,17]))
