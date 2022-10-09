import tkinter
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH

def death_screen():
    death_screen = Tk()
    death_screen.title('dead')
    death_screen.geometry("100x100")

def win_screen():
    win_screen = Tk()
    win_screen.title('win')
    win_screen.geometry("100x100")


def stopwatch(sec):
    seconds = int(sec / 100 % 60)
    minutes = int(sec / 6000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=sec, seconds=seconds)
    return out
