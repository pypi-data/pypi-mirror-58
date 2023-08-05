from .kernel import kernel
from .info import VERSION
from .vec2 import vec2

import colorama
import pygame
from time import sleep
from datetime import datetime

width = 256
height = 256

_screen = None
_cached_fonts = {}

_pr_font = None
_pr_stroke = (255, 255, 255)
_pr_strokeWeight = 1
_pr_fill = (255, 255, 255)
_pr_noFill = False

def splash():
    if datetime.now().month == 12:
        print(
f"""\033[91m
 --------------\033[32m piefish 0.1.8a \033[91m----------------\033[97m
 Happy holidays from the PyVis developer!  :3
   For help, please check the documentation   
           at the GitHub repository.          \033[91m
 -------------------------------------------- \033[39;49m
""")
    else:
        print(
f"""\033[94m
 -------------\033[97m piefish 0.1.8a \033[94m--------------\033[36m
    Hello from the PyVis developer!  :3
 For help,  please check the documentation 
         at the GitHub repository.         \033[94m
 ----------------------------------------- \033[39;49m
""")

def init():
    """Init function for PyVis (run this at the beginning of your program)"""
    global _screen
    pygame.init()
    colorama.init()
    _screen = pygame.display.set_mode((256, 256))
    _pr_font = pygame.font.SysFont("arial", 18)
    splash()
def size(x: int, y: int):
    """
    Changes the size of the window
    """
    global _screen, width, height
    _screen = pygame.display.set_mode((x, y))
    width = x
    height = y

def framerate(v):
    """
    Changes the framerate.
    """
    kernel._pr_framerate = v
    kernel._pr_frame_interval = 1 / v

def stroke(r: int, g: int = -1, b: int =-1):
    """
    Changes the stroke color to a grayscale value if 1 argument 
    is given or a rgb color value if 3 arguments are given.
    """
    global _pr_stroke
    _pr_stroke = (r, r, r) if g == -1 else (r, g, b)

def noStroke():
    """
    Disables the stroke around objects. Note: lines will not draw with stroke disabled.
    """
    global _pr_strokeWeight
    _pr_strokeWeight = 0

def strokeWeight(w):
    """
    Changes the width of the stroke (0 indicates no stroke).
    """
    global _pr_strokeWeight
    _pr_strokeWeight = w

def fill(r: int, g: int = -1, b: int = -1):
    """
    Changes the fill color to a grayscale value if 1 argument 
    is given or a rgb-color value if 3 arguments are given.
    """
    global _pr_fill, _pr_noFill
    if _pr_noFill:
        _pr_noFill = False
    _pr_fill = (r, r, r) if g == -1 else (r, g, b)

def noFill():
    """
    Disables the fill.
    """
    global _pr_noFill
    _pr_noFill = True

def background(r: int, g: int = -1, b: int = -1):
    """
    Fills the screen with the given color (grayscale or rgb).
    """
    pygame.draw.rect(_screen, (r, r, r) if g == -1 else (r, g, b), pygame.Rect(0, 0, width, height))

def line(x1: int, y1: int, x2: int, y2: int, aa = True):
    """
    Draws a line between two points `(x1, y1)` and `(x2, y2)`.
    
    Keyword Arguments:
    - `aa [bool]` -- Enables or disables anti-aliasing (default: `True`)
    """
    if _pr_strokeWeight == 0:
        return
    if aa:
        pygame.draw.aaline(_screen, _pr_stroke, (x1, y1), (x2, y2), _pr_strokeWeight)
    else:
        pygame.draw.line(_screen, _pr_stroke, (x1, y1), (x2, y2), _pr_strokeWeight)

def rect(x: int, y: int, w: int, h: int):
    """
    Draws a rectangle at point `(x,y)` with a given width (`w`) and height (`h`).
    """
    if not _pr_noFill:
        pygame.draw.rect(_screen, _pr_fill, pygame.Rect(x, y, w, h))
    if _pr_strokeWeight > 0:
        pygame.draw.rect(_screen, _pr_stroke, pygame.Rect(x, y, w, h), _pr_strokeWeight)

def polygon(points):
    """Draws a polygon from an array of points.
    
    Arguments:
    - `points [list(tuple(int, int))]` -- list of 2D integer tuples representing the points.
    """
    if not _pr_noFill:
        pygame.draw.polygon(_screen, _pr_fill, points)
    if _pr_strokeWeight > 0:
        pygame.draw.polygon(_screen, _pr_stroke, points, _pr_strokeWeight)

def ellipse(x: int, y: int, w: int, h: int):
    """
    Draws an ellipse at point `(x,y)` with a given width (`w`) and height (`h`).
    """
    if not _pr_noFill:
        pygame.draw.ellipse(_screen, _pr_fill, pygame.Rect(x, y, w, h))
    if _pr_strokeWeight > 0:
        pygame.draw.ellipse(_screen, _pr_stroke, pygame.Rect(x, y, w, h), _pr_strokeWeight)

def circle(x: int, y: int, r: int):
    """
    Draws a circle at point `(x,y)` with a given radius (`r`).
    """
    if not _pr_noFill:
        pygame.draw.circle(_screen, _pr_fill, (x, y), r)
    if _pr_strokeWeight > 0:
        pygame.draw.circle(_screen, _pr_stroke, (x, y), r, _pr_strokeWeight)

centered_tmp_feature_warning = True
def label(x: int, y: int, text: str, aa = True, centered = False):
    """
    Draws a text label at point `(x,y)` with a given text string (`text`)

    Keyword Arguments:
    - `aa [bool]` -- Enables or disables anti-aliasing (default: `True`)
    """
    global centered_tmp_feature_warning
    if centered:
        if centered_tmp_feature_warning:
            kernel.log("The 'centered' argument is temporary, and will be replaced by an alignment argument in the future.",2)
            centered_tmp_feature_warning = False

        text_surf = _pr_font.render(text, aa, _pr_fill)
        w = text_surf.get_rect().width
        _screen.blit(text_surf, (x - (w // 2), y))
    else:
        _screen.blit(_pr_font.render(text, aa, _pr_fill), (x, y))

def font(name: str, size: int, bf = False, it = False):
    """Sets the font used for labels.
    
    Arguments:
        `name [str]` -- Name of the font
        `size [int]` -- Size of the font in pt
    
    Keyword Arguments:
        `bf [bool]` -- makes the text bold (default: False)
        `it [bool]` -- makes the text slanted (default: False)
    """
    global _pr_font
    
    font_id = f'{name}-{size}'
    font_id += ('-bf' if bf else '') + ('-it' if it else '')
    if font_id in _cached_fonts:
        _pr_font = _cached_fonts[font_id]
    else:
        kernel.log(f"Requesting font [{font_id}] from system", 1)
        _pr_font = pygame.font.SysFont(name, size, bf, it)
        _cached_fonts[font_id] = _pr_font

def caption(t: str):
    """
    Sets the title of the application window.
    """
    pygame.display.set_caption(t)

def fullscreen(w=0, h=0):
    
    """
    Enables fullscreen rendering. Use size() to go back to windowed mode.
    The fullscreen resolution will be the same as it was previously, unless
    otherwise specified.
    """
    screen = pygame.display.set_mode(
        (width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)