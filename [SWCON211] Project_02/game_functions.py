import pygame
from settings import *
import os
from sound_manager import SoundManager

sound_manager = SoundManager()

def handle_paddle_movement(keys, paddle):
    if keys[pygame.K_LEFT]:
        paddle.move('left')
    if keys[pygame.K_RIGHT]:
        paddle.move('right')

def handle_ball_movement(ball, paddle):
    # 공 이동
    ball.move()
    
    # 공과 벽 충돌
    if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
        ball.speed_x *= -1
    if ball.rect.top <= 0:
        ball.speed_y *= -1
    if ball.rect.bottom >= SCREEN_HEIGHT:
        return False  # 게임 종료 조건

    # 공과 패들 충돌
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1

    return True

def check_collisions(ball, bricks, score):
    # 공과 벽돌 충돌
    for brick in bricks[:]:
        if ball.rect.colliderect(brick.rect):
            bricks.remove(brick)
            ball.speed_y *= -1
            score += 1  # 점수 증가
            sound_manager.play_sfx('brick_break')
            break

    return score

def get_high_score_file_path():
    home_dir = os.path.expanduser('~')  # 사용자의 홈 디렉토리 경로
    file_path = os.path.join(home_dir, 'high_score.txt')  # 홈 디렉토리에 파일 경로 생성
    return file_path

def save_high_score(new_score):
    file_path = get_high_score_file_path()

    try:
        with open(file_path, "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0

    if new_score > high_score:
        with open(file_path, "w") as file:
            file.write(str(new_score))
        return new_score
    return high_score

def load_high_score():
    file_path = get_high_score_file_path()

    try:
        with open(file_path, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0