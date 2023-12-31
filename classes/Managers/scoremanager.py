import pygame as pg
import pickle
import os

class ScoreManager():
    def __init__(self, directory_path):
        self.scores = None
        
        self.save_path = os.path.join(directory_path, 'save_data.pkl')

        # 파일 존재 여부
        if not os.path.isfile(self.save_path):
            self.scores = [('', 0) for _ in range(10)]
            with open(self.save_path, 'wb') as file:
                pickle.dump(self.scores, file)
        else:
            with open(self.save_path, 'rb') as file:
                self.scores = pickle.load(file)
        
    def calculate_score(self,level, coins_collected, time_left):
        return level * 10 + coins_collected*100 + int(time_left)*80
    
    def save_score(self, username, score):
        with open(self.save_path, 'rb') as file:
            self.scores = pickle.load(file)
    
        self.scores.append((username, score))

        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.scores.pop()

        with open(self.save_path, 'wb') as file:
            pickle.dump(self.scores, file)

    def load_high_scores(self):
        with open(self.save_path, 'rb') as file:
            self.scores = pickle.load(file)
        return self.scores