
# https://www.runoob.com/design-pattern/adapter-pattern.html
from abc import ABCMeta, abstractmethod


class AdvancedMediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play_vlc(self, file_name: str):
        pass

    @abstractmethod
    def play_mp4(self, file_name: str):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str):
        print(f"play vlc: {file_name}")

    def play_mp4(self, file_name: str):
        pass


class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str):
        pass

    def play_mp4(self, file_name: str):
        print(f"play mp4: {file_name}")


class MediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass


class MediaPlayerAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        self.player = None
        if audio_type == "vlc":
            self.player = VlcPlayer()
        if audio_type == "mp4":
            self.player = Mp4Player()

    def play(self, audio_type: str, file_name: str):
        if audio_type == "vlc":
            self.player.play_vlc(file_name=file_name)
        if audio_type == "mp4":
            self.player.play_mp4(file_name=file_name)


class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.player = None

    def play(self, audio_type: str, file_name: str):
        if audio_type == "mp3":
            print(f"play mp3: {file_name}")
        elif audio_type in ["vlc", "mp4"]:
            self.player = MediaPlayerAdapter(audio_type)
            self.player.play(audio_type, file_name)
        else:
            print(f"media type {audio_type} not supported")


if __name__ == '__main__':
    audio_player = AudioPlayer()
    audio_player.play("vlc", "vlc_file")
    audio_player.play("mp4", "mp4_file")
    audio_player.play("mp3", "mp3_file")
    audio_player.play("mp5", "mp5_file")
