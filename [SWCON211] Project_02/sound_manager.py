import pygame
import os
import sys

class SoundManager:
    def __init__(self):    
        self.sfx_enabled = True
        self.bgm_enabled = True
        pygame.mixer.init()
        self.load_sounds()

    def load_sounds(self):
        # PyInstaller 실행 파일 경로 확인
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
            
        self.bgm_path = os.path.join(application_path, 'sounds', 'bgm.wav')
        self.paddle_hit_path = os.path.join(application_path, 'sounds', 'paddle_hit.wav')
        self.brick_break_path = os.path.join(application_path, 'sounds', 'brick_break.wav')

        pygame.mixer.music.load(self.bgm_path)
        self.paddle_hit_sound = pygame.mixer.Sound(self.paddle_hit_path)
        self.brick_break_sound = pygame.mixer.Sound(self.brick_break_path)

    def play_bgm(self):
        if self.bgm_enabled:
            pygame.mixer.music.play(-1)  # 무한 반복

    def stop_bgm(self):
        pygame.mixer.music.stop()

    def play_sfx(self, sound):
        if self.sfx_enabled:
            if sound == 'paddle_hit':
                self.paddle_hit_sound.play()
            elif sound == 'brick_break':
                self.brick_break_sound.play()

    def toggle_sfx(self):
        self.sfx_enabled = not self.sfx_enabled

    def toggle_bgm(self):
        self.bgm_enabled = not self.bgm_enabled
        if self.bgm_enabled:
            self.play_bgm()
        else:
            self.stop_bgm()
