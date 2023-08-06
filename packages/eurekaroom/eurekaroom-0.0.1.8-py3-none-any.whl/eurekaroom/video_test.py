import unittest
import tkinter as Tk
from video import Player

class PlayerTest(unittest.TestCase):
    
    def test_video_is_playing(self):
        
        player = Player(parent=Tk.Tk(), video=".media/Videos/Planet_Success.mp4")
        Not_Playing = player.player.is_playing()
        player.Play()

        self.assertNotEqual(player.player.is_playing(), Not_Playing)

    def test_non_video_dosnt_play(self):
       
       player = Player(parent=Tk.Tk(), video=".media/Videos/Non_Existent.mp4")
       Not_Playing = player.player.is_playing()
       player.Play()
       self.assertIs(player.player.is_playing(), Not_Playing)

if __name__ == "__main__":
    unittest.main()