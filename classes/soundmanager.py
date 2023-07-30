import pygame

class SoundManager:
    def __init__(self, sound_files):
        # pygame 초기화
        pygame.mixer.init()
        
        # 각 사운드를 담을 딕셔너리
        self.sounds = {}
        
        # 사운드 파일로부터 Sound 객체 생성 및 딕셔너리에 저장
        for name, file_path in sound_files.items():
            sound = pygame.mixer.Sound(file_path)
            self.sounds[name] = sound

    def play(self, sound_name):
        # 사운드 이름이 딕셔너리에 없으면 에러 발생
        if sound_name not in self.sounds:
            raise ValueError(f"Sound '{sound_name}' not found in the sounds dictionary.")
        
        # 사운드 재생
        self.sounds[sound_name].play()

    def stop(self, sound_name):
        # 사운드 이름이 딕셔너리에 없으면 에러 발생
        if sound_name not in self.sounds:
            raise ValueError(f"Sound '{sound_name}' not found in the sounds dictionary.")
        
        # 사운드 정지
        self.sounds[sound_name].stop()

# 사용 예시
if __name__ == "__main__":
    sound_files = {
        "background_music": "background_music.wav",
        "gunshot": "gunshot.wav",
        "explosion": "explosion.wav"
    }

    manager = SoundManager(sound_files)

    try:
        manager.play("background_music")
        input("Background music playing. Press Enter to stop...")
        manager.stop("background_music")

        manager.play("gunshot")
        input("Gunshot sound playing. Press Enter to stop...")
        manager.stop("gunshot")

        manager.play("explosion")
        input("Explosion sound playing. Press Enter to stop...")
        manager.stop("explosion")
    except ValueError as e:
        print(e)
