import pygame as pg
import os
import sys
import pickle

# 텍스트 그리는 함수
def draw_text(screen ,text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def resource_path(relative_path):
    # exe 파일을 위한 절대경로 반환
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)