# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


def main():
    (w, h) = (300, 300)  # 画面サイズ

    pygame.init()  # pygame初期化
    pygame.display.set_mode((300, 400), 0, 32)
    pygame.display.set_caption("8 Puzzle")  # 画面設定

    screen = pygame.display.get_surface()

    goal_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_lst = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    num_lst = [0 for _ in range(9)]
    num_rect = [0 for _ in range(9)]
    score = 0
    font = pygame.font.Font(None, 55)
    text = font.render("score : " + str(score), True, (255, 255, 255))  # 描画する文字列の設定
    space = 7
    dest = 0
    lst = [i for i in range(10)]
    for i in range(9):
        now = start_lst[i]
        pic = "num" + str(now) + ".png"
        num_lst[now - 1] = pygame.image.load(pic).convert_alpha()
        num_lst[now - 1] = pygame.transform.scale(num_lst[now - 1], (90, 90))
        num_rect[now - 1] = num_lst[now - 1].get_rect()
        num_rect[now - 1].center = (w / 6 + w / 3 * (i % 3), h / 6 + h / 3 * (i // 3) + 100)

    while 1:
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
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら中心座標を矢印の方向に移動
                score += 1
                text = font.render("score : " + str(score), True, (255, 255, 255))  # 描画する文字列の設定

                x, y = space % 3, space // 3  # 現在地の(x,y)座標
                if event.key == K_RIGHT:
                    dest = (x - 1) + y * 3
                    num_rect[start_lst[space] - 1].move_ip(-100, 0)
                    num_rect[start_lst[dest] - 1].move_ip(100, 0)
                if event.key == K_LEFT:
                    dest = (x + 1) + y * 3
                    num_rect[start_lst[space] - 1].move_ip(100, 0)
                    num_rect[start_lst[dest] - 1].move_ip(-100, 0)
                if event.key == K_DOWN:
                    dest = x + (y - 1) * 3
                    num_rect[start_lst[space] - 1].move_ip(0, -100)
                    num_rect[start_lst[dest] - 1].move_ip(0, 100)
                if event.key == K_UP:
                    dest = x + (y + 1) * 3
                    num_rect[start_lst[space] - 1].move_ip(0, 100)
                    num_rect[start_lst[dest] - 1].move_ip(0, -100)
                start_lst[dest], start_lst[space] = start_lst[space], start_lst[dest]
                space = dest

                if start_lst == goal_lst:
                    print("YEEES")
                    congrats = font.render("Congratuatino!!", True, (255, 255, 255))
                    screen.blit(congrats, [50, 50])


if __name__ == "__main__":
    main()
