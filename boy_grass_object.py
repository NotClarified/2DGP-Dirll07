from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(41,800-41), 599
        self.image = load_image('ball41x41.png')
    def update(self):
        self.y -= random.randint(5,15)
        if self.y < 30+41:
            self.y = 30+41

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(21,800-21), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        self.y -= random.randint(5,15)
        if self.y < 30+21:
            self.y = 30+21
    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
def reset_world():
    global running
    global grass
    global team
    running = True
    grass = Grass()
    team = [Boy() for i in range(10)]
    # big_ball = BigBall()
def update_world():
    grass.update()
    for boy in team:
        boy.update()
    pass
def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

# game main loop code
open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
close_canvas()
