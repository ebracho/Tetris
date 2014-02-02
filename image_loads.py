import sys, pygame

# Block Images
CYAN_BLOCK = pygame.image.load('blocks/cyanblock.png')
YELLOW_BLOCK = pygame.image.load('blocks/yellowblock.png')
VIOLET_BLOCK = pygame.image.load('blocks/violetblock.png')
RED_BLOCK = pygame.image.load('blocks/redblock.png')
GREEN_BLOCK = pygame.image.load('blocks/greenblock.png')
BLUE_BLOCK = pygame.image.load('blocks/blueblock.png')
ORANGE_BLOCK = pygame.image.load('blocks/orangeblock.png')
EMPTY_BLOCK = pygame.image.load('blocks/emptyblock.png')

# Block Rects
CYAN_BLOCK_RECT = CYAN_BLOCK.get_rect()
YELLOW_BLOCK_RECT = YELLOW_BLOCK.get_rect()
VIOLET_BLOCK_RECT = VIOLET_BLOCK.get_rect()
RED_BLOCK_RECT = RED_BLOCK.get_rect()
GREEN_BLOCK_RECT = GREEN_BLOCK.get_rect()
BLUE_RECT = BLUE_BLOCK.get_rect()
ORANGE_RECT = ORANGE_BLOCK.get_rect()
EMPTY_BLOCK_RECT = EMPTY_BLOCK.get_rect()

# Swap Images
I_SWAP = pygame.image.load('swap_images/swap_i.png')
O_SWAP = pygame.image.load('swap_images/swap_o.png')
T_SWAP = pygame.image.load('swap_images/swap_t.png')
S_SWAP = pygame.image.load('swap_images/swap_s.png')
Z_SWAP = pygame.image.load('swap_images/swap_z.png')
J_SWAP = pygame.image.load('swap_images/swap_j.png')
L_SWAP = pygame.image.load('swap_images/swap_l.png')
EMPTY_SWAP = pygame.image.load('swap_images/swap_e.png')

# Swap Rects
I_SWAP_RECT = I_SWAP.get_rect()
O_SWAP_RECT = O_SWAP.get_rect()
T_SWAP_RECT = T_SWAP.get_rect()
S_SWAP_RECT = S_SWAP.get_rect()
Z_SWAP_RECT = Z_SWAP.get_rect()
J_SWAP_RECT = J_SWAP.get_rect()
L_SWAP_RECT = L_SWAP.get_rect()
EMPTY_SWAP_RECT = EMPTY_SWAP.get_rect()

# Queue Images
I_QUEUE = pygame.image.load('queue_images/queue_i.png')
O_QUEUE = pygame.image.load('queue_images/queue_o.png')
T_QUEUE = pygame.image.load('queue_images/queue_t.png')
S_QUEUE = pygame.image.load('queue_images/queue_s.png')
Z_QUEUE = pygame.image.load('queue_images/queue_z.png')
J_QUEUE = pygame.image.load('queue_images/queue_j.png')
L_QUEUE = pygame.image.load('queue_images/queue_l.png')

# Queue Rects
I_QUEUE_RECT = I_QUEUE.get_rect()
O_QUEUE_RECT = O_QUEUE.get_rect()
T_QUEUE_RECT = T_QUEUE.get_rect()
S_QUEUE_RECT = S_QUEUE.get_rect()
Z_QUEUE_RECT = Z_QUEUE.get_rect()
J_QUEUE_RECT = J_QUEUE.get_rect()
L_QUEUE_RECT = L_QUEUE.get_rect()

BLOCK_KEYS = { 'c': CYAN_BLOCK,
               'y': YELLOW_BLOCK,
               'v': VIOLET_BLOCK,
               'r': RED_BLOCK,
               'g': GREEN_BLOCK,
               'b': BLUE_BLOCK,
               'o': ORANGE_BLOCK,
               '-': EMPTY_BLOCK }

BLOCK_RECT_KEYS = { 'c': CYAN_BLOCK_RECT,
                    'y': YELLOW_BLOCK_RECT,
                    'v': VIOLET_BLOCK_RECT,
                    'r': RED_BLOCK_RECT,
                    'g': GREEN_BLOCK_RECT,
                    'b': BLUE_RECT,
                    'o': ORANGE_RECT,
                    '-': EMPTY_BLOCK_RECT }

SWAP_KEYS = { 'i': I_SWAP,
              'o': O_SWAP,
              't': T_SWAP,
              's': S_SWAP,
              'z': Z_SWAP,
              'j': J_SWAP,
              'l': L_SWAP, 
              'e': EMPTY_SWAP }

SWAP_RECT_KEYS = { 'i': I_SWAP_RECT,
                   'o': O_SWAP_RECT,
                   't': T_SWAP_RECT,
                   's': S_SWAP_RECT,
                   'z': Z_SWAP_RECT,
                   'j': J_SWAP_RECT,
                   'l': L_SWAP_RECT,
                   'e': EMPTY_SWAP_RECT }
        
QUEUE_KEYS = { 'i': I_QUEUE,
              'o': O_QUEUE,
              't': T_QUEUE,
              's': S_QUEUE,
              'z': Z_QUEUE,
              'j': J_QUEUE,
              'l': L_QUEUE, }

QUEUE_RECT_KEYS = { 'i': I_QUEUE_RECT,
                   'o': O_QUEUE_RECT,
                   't': T_QUEUE_RECT,
                   's': S_QUEUE_RECT,
                   'z': Z_QUEUE_RECT,
                   'j': J_QUEUE_RECT,
                   'l': L_QUEUE_RECT, }

