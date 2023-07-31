import pygame

class SoundManager:
    _instance = None

    def __new__(cls, sound_files):
        if cls._instance is None:
            cls._instance = super(SoundManager, cls).__new__(cls)
            
            # pygame 초기화
            pygame.mixer.init()
            
            # 각 사운드를 담을 딕셔너리
            cls._instance.sounds = {}
            
            for name, file_path in sound_files.items():
                sound = pygame.mixer.Sound(file_path)
                cls._instance.sounds[name] = sound

        return cls._instance

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
