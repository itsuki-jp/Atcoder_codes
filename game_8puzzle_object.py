# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import queue

# 参考http://www.nct9.ne.jp/m_hiroi/light/pyalgo27.html#list1

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

pygame.init()  # pygame初期化
(w, h) = (300, 300)  # 画面サイズ
pygame.display.set_mode((300, 400), 0, 32)
pygame.display.set_caption("8 Puzzle")  # 画面設定
screen = pygame.display.get_surface()
font = pygame.font.Font(None, 55)


class State:
    def __init__( self, board, space, prev, way, trial ):
        self.board = board
        self.space = space
        self.prev = prev
        self.way = way
        self.trial = trial


def solvable_check( check_lst ):
    number = 0
    space = check_lst.index(0)
    check_lst[space] = 9
    goal = [i for i in range(1, 10)]
    lst = check_lst[::1]
    while check_lst != goal:
        for i in range(1, 10):
            num = lst[i - 1]
            if num != i:
                lst[i - 1] = lst[num - 1]
                lst[num - 1] = num
                number += 1
            check_lst = lst[::1]
    x = 2 - space % 3
    y = 2 - space // 3
    if number % 2 == ((x + y) % 2):
        return True
    else:
        return False


def create_puzzle():
    TF = True
    number_lst = [0] * 9
    while TF:
        lst = [i for i in range(9)]
        for i in range(9):
            num = random.randrange(0, 9 - i)
            number_lst[i] = lst[num]
            lst.remove(lst[num])
        if solvable_check(number_lst):
            TF = False
    print(number_lst)
    return number_lst


def hint( start ):
    start[start.index(9)] = 0
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
                    return get_ans(a, c)
            else:
                c = State(b, x, a, a.way, a.trial + 1)
                q.put(c)
                table[key] = c


def print_first( x ):
    if x.trial == 0:
        return [1, 2, 3, 4, 5, 6, 7, 8, 0]
    while x.trial != 1:
        x = x.prev
    return x.board


def get_ans( a, b ):
    if a.way == FORE:
        num = print_first(a)
    else:
        num = print_first(b)
    num[num.index(0)] = 9
    return num, (a.trial + b.trial + 1)


def show_congrats( lst ):
    if [1, 2, 3, 4, 5, 6, 7, 8, 9] == lst:
        congrats = font.render("Congrats!!", True, (255, 255, 255))
        screen.blit(congrats, [50, 50])


def draw_puzzle( lst ):
    num_lst = [0 for _ in range(9)]
    num_rect = [0 for _ in range(9)]
    for i in range(9):
        now = lst[i]
        pic = "num" + str(now) + ".png"
        num_lst[now - 1] = pygame.image.load(pic).convert_alpha()
        num_lst[now - 1] = pygame.transform.scale(num_lst[now - 1], (90, 90))
        num_rect[now - 1] = num_lst[now - 1].get_rect()
        num_rect[now - 1].center = (w / 6 + w / 3 * (i % 3), h / 6 + h / 3 * (i // 3) + 100)
    return num_lst, num_rect


def draw_start():
    title = font.render("8 Puzzle", True, (255, 255, 255))
    start_btn = pygame.Rect(100, 150, 100, 50)
    start_text = font.render("Start", True, (255, 255, 255))
    how_to_btn = pygame.Rect(80, 230, 150, 50)
    how_to_text = font.render("How To", True, (255, 255, 255))
    quit_btn = pygame.Rect(100, 310, 100, 50)
    quit_text = font.render("QUIT", True, (255, 255, 255))
    while 1:
        pygame.display.update()
        pygame.time.wait(30)  # 更新時間間隔
        screen.fill((0, 0, 0, 0))  # 画面の背景色
        screen.blit(title, [70, 50])
        pygame.draw.rect(screen, (255, 0, 0), start_btn)
        screen.blit(start_text, [100, 150])
        pygame.draw.rect(screen, (255, 0, 0), how_to_btn)
        screen.blit(how_to_text, [80, 230])
        pygame.draw.rect(screen, (255, 0, 0), quit_btn)
        screen.blit(quit_text, [100, 310])
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    main()
                if how_to_btn.collidepoint(event.pos):
                    draw_how_to()
                if quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def draw_how_to():
    pass


def main():
    org_lst = create_puzzle()
    start_lst = org_lst[::1]
    print("-------")
    score = 0
    text = font.render("score : " + str(score), True, (255, 255, 255))  # 描画する文字列の設定
    space = start_lst.index(9)
    num_lst, num_rect = draw_puzzle(start_lst)

    while 1:
        show_congrats(start_lst)  # 完成したか確認
        screen.blit(text, [50, 50])  # 文字列の表示位置
        pygame.display.update()  # 画面更新
        pygame.time.wait(30)  # 更新時間間隔
        screen.fill((0, 20, 0, 0))  # 画面の背景色
        for i in range(9):
            screen.blit(num_lst[i], num_rect[i])  # プレイヤー画像の描画
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                print(start_lst)
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら中心座標を矢印の方向に移動
                score += 1
                text = font.render("score : " + str(score), True, (255, 255, 255))  # 描画する文字列の設定

                x, y = space % 3, space // 3  # 現在地の(x,y)座標
                if event.key == K_RIGHT:
                    dest = (x - 1) + y * 3
                    if not dest in adjacent[space]:
                        continue
                    num_rect[start_lst[space] - 1].move_ip(-100, 0)
                    num_rect[start_lst[dest] - 1].move_ip(100, 0)
                    start_lst[dest], start_lst[space] = start_lst[space], start_lst[dest]
                    space = dest
                if event.key == K_LEFT:
                    dest = (x + 1) + y * 3
                    if not dest in adjacent[space]:
                        continue
                    num_rect[start_lst[space] - 1].move_ip(100, 0)
                    num_rect[start_lst[dest] - 1].move_ip(-100, 0)
                    start_lst[dest], start_lst[space] = start_lst[space], start_lst[dest]
                    space = dest
                if event.key == K_DOWN:
                    dest = x + (y - 1) * 3
                    if not dest in adjacent[space]:
                        continue
                    num_rect[start_lst[space] - 1].move_ip(0, -100)
                    num_rect[start_lst[dest] - 1].move_ip(0, 100)
                    start_lst[dest], start_lst[space] = start_lst[space], start_lst[dest]
                    space = dest
                if event.key == K_UP:
                    dest = x + (y + 1) * 3
                    if not dest in adjacent[space]:
                        continue
                    num_rect[start_lst[space] - 1].move_ip(0, 100)
                    num_rect[start_lst[dest] - 1].move_ip(0, -100)
                    start_lst[dest], start_lst[space] = start_lst[space], start_lst[dest]
                    space = dest
                if event.key == K_r:  # もし「リセット」が押されたら
                    print("-------")
                    num_lst, num_rect = draw_puzzle(org_lst)
                    space = org_lst.index(9)
                    start_lst = org_lst[::1]
                    score = 0
                if event.key == K_s:  # もし「シhャッフル」が押されたら
                    main()
                if event.key == K_h:  # もし「ヒント」が押されたら
                    start_lst, min_way = hint(start_lst)
                    num_lst, num_rect = draw_puzzle(start_lst)
                    space = start_lst.index(9)
                    score += 4
                text = font.render("score : " + str(score), True, (255, 255, 255))


if __name__ == "__main__":
    draw_start()

# 表示するもの
"""
*リセットボタン（一番最初の盤面）
*シャッフルボタン（新しい盤面を作成）
*現在のスコア
*最短で何手か表示
*ヒントボタンを作成→次の最適手に切り替わる→最短手数も変更
  スコア→Maxを100、一手ごとに-1
  ヒントを使うと－5
"""
