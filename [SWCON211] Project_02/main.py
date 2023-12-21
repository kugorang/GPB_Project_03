import os
import pygame
from sound_manager import SoundManager
from settings import *
from game_objects import Paddle, Ball
from game_functions import *
from levels import *

# 현재 스크립트의 디렉토리로 작업 디렉토리 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Pygame 초기화
pygame.init()

# SoundManager 인스턴스 생성 및 배경음악 재생
sound_manager = SoundManager()
sound_manager.play_bgm()

def run_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("벽돌깨기 - 2015104167 김현우")

    # 게임 오브젝트 초기화
    paddle = Paddle()
    ball = Ball()
    #bricks = level_1()

    # 레벨 초기화
    level_data = load_map_from_file(MAP_SAVE_PATH)
    bricks = create_bricks_from_data(level_data)

    # 점수 초기화
    score = 0
    font = pygame.font.SysFont("malgungothic", 36)

    # 게임 루프
    high_score = load_high_score()
    current_level = 1
    max_level = 3  # 최대 레벨 설정
    
    
    # 게임 루프
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle)
        running = handle_ball_movement(ball, paddle)
        score = check_collisions(ball, bricks, score)
        
        # 공과 패들의 충돌 감지
        if ball.rect.colliderect(paddle.rect):
            sound_manager.play_sfx('paddle_hit')  # 패들 충돌 효과음 재생
        
        # 모든 벽돌이 제거되면 다음 레벨로 전환
        if not bricks:
            current_level += 1
            if current_level > max_level:
                # 모든 레벨 완료 시 게임 종료
                show_game_over_screen(screen, score, high_score, "성공!")  # 게임 클리어 메시지
                break
            # elif current_level == 2:
            #     # 두 번째 레벨 로드
            #     bricks = level_2()
            # elif current_level == 3:
            #     # 세 번째 레벨 로드
            #     bricks = level_3()

        # 화면 그리기
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle.rect)
        pygame.draw.ellipse(screen, WHITE, ball.rect)
        for brick in bricks:
            pygame.draw.rect(screen, brick.color, brick.rect)

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # 현재 레벨 표시
        level_text = font.render(f"Level: {current_level}", True, WHITE)
        screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))  # 우측 상단에 위치

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    # 게임 종료 후 결과 화면
    final_score = score
    high_score = save_high_score(final_score)
    
    # 게임 오버 화면 표시 및 사용자의 선택 대기
    if not running:
        retry = show_game_over_screen(screen, score, high_score, "실패!")

        if retry:
            run_game()  # 게임 재시작
        else:
            return  # 게임 종료
    
def show_game_over_screen(screen, score, high_score, message):
    font1 = pygame.font.SysFont("malgungothic", 36)
    font2 = pygame.font.SysFont("malgungothic", 20)
    
    game_over_text = font1.render(message, True, WHITE)  # 메시지 동적 처리
    high_score_text = font2.render(f"High Score: {high_score}", True, WHITE)
    score_text = font2.render(f"Your Score: {score}", True, WHITE)
    retry_text = font2.render("다시 하려면 R키를, 종료하려면 아무 키나 누르세요", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 125))
    pygame.display.flip()

    # 결과 화면에서 사용자의 입력을 기다림
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # 게임 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # 게임 재시작
                else:
                    pygame.quit()
                    return False  # 게임 종료

if __name__ == '__main__':
    run_game()