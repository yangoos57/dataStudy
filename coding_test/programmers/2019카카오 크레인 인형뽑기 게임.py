## 크레인 인형뽑기 게임


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    moves = list(map(lambda x: x - 1, moves))
    N = len(board)
    item = [0]
    answer = 0
    for i in moves:
        for j in range(N):
            if board[j][i] != 0:
                if item[-1] == board[j][i]:
                    answer += 2
                    item.pop()
                else:
                    item.append(board[j][i])
                board[j][i] = 0
                break

    return answer


solution(board, moves)
