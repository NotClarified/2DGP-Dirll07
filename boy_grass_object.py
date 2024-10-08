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
        self.y -= random.randint(1,20)
        if self.y < 30+ 41:
            self.y = 30+ 41

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y,41,41)
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(21,800-21), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        self.y -= random.randint(1,15)
        if self.y < 30+ 21 + 10:
            self.y = 30+ 21 + 10
    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y,21,21)
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
    global fall_big_balls, fall_small_balls
    global boy, small_ball, big_ball

    running = True
    grass = Grass()
    team = [Boy() for i in range(10)]
    boy =Boy()
    small_ball = SmallBall()
    big_ball = BigBall()

    # 공 개수 20개 크기 랜덤으로 조절
    big_ball_num = random.randint(1,19)
    small_ball_num = 20 - big_ball_num
    fall_big_balls = [BigBall() for i in range(big_ball_num)]
    fall_small_balls = [SmallBall() for i in range(small_ball_num)]
def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for small_ball in fall_small_balls:
        small_ball.update()
    for big_ball in fall_big_balls:
        big_ball.update()
    pass
def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for small_ball in fall_small_balls:
        small_ball.draw()
    for big_ball in fall_big_balls:
        big_ball.draw()
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
