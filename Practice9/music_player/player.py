import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.tracks = self.load_tracks()
        self.current = 0
        self.is_playing = False

    def load_tracks(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        return files

    def play(self):
        if not self.tracks:
            return
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.tracks:
            return
        self.current = (self.current + 1) % len(self.tracks)
        self.play()

    def prev_track(self):
        if not self.tracks:
            return
        self.current = (self.current - 1) % len(self.tracks)
        self.play()

    def get_current_track(self):
        if not self.tracks:
            return "No tracks"
        return os.path.basename(self.tracks[self.current])