import queue
import time

adjacent = (
    (1, 3),  # 0
    (0, 2, 4),  # 1
    (1, 5),  # 2
    (0, 4, 6),  # 3
    (1, 3, 5, 7),  # 4
    (2, 4, 8),  # 5
    (3, 7),  # 6
    (4, 6, 8),  # 7
    (5, 7)  # 8
)
SIZE = 181440
GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]
FORE = 1
BACK = 0


class State:
    def __init__( self, board, space, prev, way, trial ):
        self.board = board
        self.space = space
        self.prev = prev
        self.way = way
        self.trial = trial


def bf_search( start ):
    case = -1
    q = queue.Queue()
    table = {}
    temp = State(start, start.index(0), None, FORE, 0)
    q.put(temp)
    table[tuple(start)] = temp
    temp = State(GOAL, GOAL.index(0), None, BACK, 0)
    q.put(temp)
    table[tuple(GOAL)] = temp
    while not q.qsize() == 0:
        a = q.get()
        case += 1
        for x in adjacent[a.space]:
            b = list(a.board)
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table:
                c = table[key]  # 同じ盤面のSTATE
                if c.way != a.way:
                    print_answer1(a, c)
                    temp = ":"
                    print(f"探した盤面数　: {case}")
                    return
            else:
                c = State(b, x, a, a.way, a.trial + 1)
                q.put(c)
                table[key] = c


# 手順の表示
def print_answer( x ):
    if x is not None:
        print_answer(x.prev)
        print(x.board)


def print_answer_goal( a ):
    while a is not None:
        print(a.board)
        a = a.prev


def print_answer1( a, b ):
    if a.way == FORE:
        print_answer(a)
        print_answer_goal(b)
    else:
        print_answer(b)
        print_answer_goal(a)
    print(f"最短手数　　　: {a.trial + b.trial + 1}")


st = time.time()
bf_search([int(i) for i in list(input())])
#bf_search([8, 6, 7, 2, 5, 4, 3, 0, 1])
ft = time.time()
print(f"実行時間　　　: {ft - st}")

#　参考http://www.nct9.ne.jp/m_hiroi/light/pyalgo27.html#list1