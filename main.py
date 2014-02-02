import sys, pygame, time
from image_loads import *
from tetris import Tetris
from collections import deque


pygame.init()

# Display Setup
WIDTH = 480
HEIGHT = 690

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tetris')
screen.fill((0,125,125))

intro_font = pygame.font.SysFont("monospace", 20)
message = "Press any key to start"
intro_label = intro_font.render(message, 1, (255,255,255))

pause_screen = pygame.Surface((WIDTH,HEIGHT))
pause_screen.fill((0,0,0))
pause_screen.set_alpha(200)

# Audio Setup
pygame.mixer.init()
pygame.mixer.music.load('sounds/bgmusic.mp3')
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound('sounds/collision.wav')
clear_1_sound = pygame.mixer.Sound('sounds/clear_1.wav')
clear_2_sound = pygame.mixer.Sound('sounds/clear_2.wav')
clear_3_sound = pygame.mixer.Sound('sounds/clear_3.wav')
clear_4_sound = pygame.mixer.Sound('sounds/clear_4.wav')
clear_sounds = { 1 : clear_1_sound, 2 : clear_2_sound, 
                 3 : clear_3_sound, 4 : clear_4_sound }

def intro_loop(screen,game):
    screen.fill((0,125,125))
    screen.blit(intro_label, (105,630))
    tick = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN: game_loop(screen,game)

        # Render blocks onto screen
        render_game(screen,game,True)

        # Block Animations
        colors = ['c','y','v','g','r','b','o']
        if tick <= 70:
            game.insert_block(tick%10,0,colors[(tick/10)%7],True)
            game.insert_block(9-(tick%10),0,colors[((tick/10)+3)%7],True)

        game.freeze_bottom_row()
        game.clear_full_rows(0)
        game.shift_moving_blocks('down', False)
        if tick == 70: tick = 0
        tick+=1
        time.sleep(.07)

def update_score(screen, game):
    score_font = pygame.font.SysFont("monospace",48)
    score_label = score_font.render("Score: %d" % game.points, 1, (255,255,255))
    screen.fill((0,125,125)) # Erase old score
    screen.blit(score_label, (95, 620))
    
def pause_loop(screen,message, reset = False):
    pygame.mixer.music.set_volume(.3)

    screen.blit(pause_screen, (0,0))

    if len(message) > 10: font_size = 700/len(message)
    else: font_size = 48
    message_font = pygame.font.SysFont("monospace", font_size)
    message_label = message_font.render(message, 1, (255,255,255))
    x_offset = WIDTH/2 - message_label.get_width()/2
    screen.blit(message_label, (x_offset,200))
    pygame.display.flip()

    # Enter infinite loop until ESC is pressed
    k_escape_pressed = False
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: sys.exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    k_escape_pressed = True
        if k_escape_pressed: break

    if reset == True: game.reset_game()
    screen.fill((0,125,125))
    pygame.mixer.music.set_volume(1)

def render_game(screen,game,grid_only = False):

    # Blocks
    block_list = game.get_blocks()
    # Score 
    if not grid_only: update_score(screen, game)
    
    for blocks in block_list[20:]:
        y_offput = 30 * blocks[0] - 60
        x_offput = 30 * blocks[1] + 90
        block_rect = BLOCK_RECT_KEYS[blocks[2]]
        block_image = BLOCK_KEYS[blocks[2]]
        screen.blit(block_image, (x_offput,y_offput), block_rect)


    # Swap Image
    if not grid_only:
        swap_image = SWAP_KEYS[game.current_swap]
        swap_rect = SWAP_RECT_KEYS[game.current_swap]
        screen.blit(swap_image, (0,0), swap_rect)

        # Tetromino Queue
        for i in range(4):
            tetromino = game.tetromino_queue[i]
            queue_image = QUEUE_KEYS[tetromino]
            queue_rect = QUEUE_RECT_KEYS[tetromino]
            screen.blit(queue_image, (390, 87*i), queue_rect)
            
    pygame.display.flip()

def game_loop(screen,game):
    quick_pause = False
    game.reset_game()
    swap_count = 0
    tick = 0

    # Input processing
    k_left_pressed = False
    k_right_pressed = False
    k_down_pressed = False
    k_up_pressed = False
    k_space_pressed = False
    k_lshift_pressed = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: k_left_pressed = True
                if event.key == pygame.K_RIGHT: k_right_pressed = True
                if event.key == pygame.K_DOWN: k_down_pressed = True
                if event.key == pygame.K_UP: k_up_pressed = True
                if event.key == pygame.K_SPACE: k_space_pressed = True
                if event.key == pygame.K_LSHIFT: k_lshift_pressed = True
                if event.key == pygame.K_ESCAPE: pause_loop(screen,"pause")
               

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: k_left_pressed = False
                if event.key == pygame.K_RIGHT: k_right_pressed = False
                if event.key == pygame.K_DOWN: k_down_pressed = False
                if event.key == pygame.K_UP: k_up_pressed = False
                if event.key == pygame.K_SPACE: k_space_pressed = False
                if event.key == pygame.K_LSHIFT: k_lshift_pressed = False

        if quick_pause == 2: 
            time.sleep(.16)
            quick_pause = 0
        if quick_pause == 1: quick_pause += 1

        # Rendering
        render_game(screen,game)

        # Game processing
        if game.game_over == True: pause_loop(screen,"Game Over: Press ESC to try again", True)
        rows_cleared = game.clear_full_rows(0)
        if rows_cleared: clear_sounds[rows_cleared].play()

        if k_up_pressed == True: game.rotate_tetromino()
        elif k_down_pressed == True: game.shift_moving_blocks('down')
        elif k_left_pressed == True: 
            if not game.shift_moving_blocks('left'): collision_sound.play()

        elif k_right_pressed == True: 
            if not game.shift_moving_blocks('right'): collision_sound.play()

        elif k_space_pressed == True: 
            while game.shift_moving_blocks('down'): pass
            quick_pause = True # Helps avoid accidently flooring next tetromino

        elif k_lshift_pressed == True: 
            if swap_count == 0: # 1 swap per insert
                game.swap()
                swap_count += 1
        
        if tick == 4:
            game.shift_moving_blocks('down')
            if game.no_moving_blocks(): 
                game.insert_tetromino()
                swap_count = 0
            tick = 0

        time.sleep(.08)
        tick += 1

game = Tetris(10,22)

intro_loop(screen,game)
