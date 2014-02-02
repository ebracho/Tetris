from tetrominos import get_tetromino
from random import randint
from collections import deque

class Tetris(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.make_grid()
        self.reset_offsets()
        self.set_colors()
        self.set_shapes()
        self.set_tetromino_queue()
        self.orientation = 0
        self.points = 0
        self.game_over = False
        self.current_tetromino = None
        self.current_swap = 'e'

    """
    Init Functions
    """
    def make_grid(self):
        self.grid = []
        for y in range(self.height):
            self.grid.append([])
            for x in range(self.width):
                self.grid[y].append((y, x, '-', False))
         

    def reset_offsets(self):
        self.x_offset = self.width/2 - 2
        self.y_offset = 0

    def set_colors(self):
        # Pairs tetromino shapes with respective block colors
        self.colors = { 'i' : 'c', 'o' : 'y', 't' : 'v', 'j' : 'b',
                        'l' : 'o', 'z' : 'g', 's' : 'r' }

    def set_shapes(self):
        self.shape_list = ['i', 'o', 't', 'j', 'l', 'z', 's']

    def set_tetromino_queue(self):
        self.tetromino_queue = deque([])
        for i in range(4):
            self.tetromino_queue.append(self.shape_list[randint(0,6)])

    """
    Helper functions for moving blocks.
    """
    def in_bounds(self, y, x):
        if y < 0 or x < 0 or y >= self.height or x >= self.width: return False
        else: return True


    def space_occupied(self, y, x):
        # Returns True if specified cell contains a stationary block 
        cell = self.grid[y][x]
        if cell[3] == False and cell[2] != '-': return True
        return False

    def get_moving_blocks(self):
        moving_blocks = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x][3] == True: 
                    color = self.grid[y][x][2]
                    moving_blocks.append((y,x,color))
        return moving_blocks


    def clear_moving_blocks(self):
        moving_blocks = self.get_moving_blocks()
        for blocks in moving_blocks:
            y = blocks[0]
            x = blocks[1]
            self.grid[y][x] = (y,x,'-',False)

    def no_moving_blocks(self):
        blocks = self.get_moving_blocks()
        if not blocks: return True
        return False

    def freeze_moving_blocks(self):
        moving_blocks = self.get_moving_blocks()
        for blocks in moving_blocks:
            y = blocks[0]
            x = blocks[1]
            color = blocks[2]
            self.grid[y][x] = (y,x,color,False)
            self.reset_offsets()
            self.orientation = 0

    """
    Helper functions for static blocks.
    """
    def get_static_blocks(self):
        static_blocks = []
        for y in range(self.height):
            for x in range(self.width):
                block = self.grid[y][x]
                if block[2] != '-' and block[3] == False:
                    color = block[2]
                    static_blocks.append((y,x,color))
        return static_blocks

    def clear_static_blocks(self,threshold):
        static_blocks = self.get_static_blocks()
        for blocks in static_blocks:
            y = blocks[0]
            x = blocks[1]
            if y < threshold:
                # Replace all static blocks below threshold with an empty block
                self.grid[y][x] = (y,x,'-',False)

    def shift_down_static_blocks(self, threshold):
        static_blocks = self.get_static_blocks()
        self.clear_static_blocks(threshold)
        for blocks in static_blocks:
            y = blocks[0]
            x = blocks[1]
            color = blocks[2]
            if y < threshold:
                self.grid[y+1][x] = (y+1,x,color,False)
    
    """
    Core Functions
    """
    def insert_tetromino(self, make_new_shape = True):
        if make_new_shape == True: 
            self.current_tetromino = self.tetromino_queue.popleft()
            self.tetromino_queue.append(self.shape_list[randint(0,6)])
        tetromino = get_tetromino(self.current_tetromino, self.orientation)
        # Check if tetromino is safe to place
        for blocks in tetromino:
            y = blocks[0] + self.y_offset
            x = blocks[1] + self.x_offset
            if not self.in_bounds(y,x) or self.space_occupied(y,x): 
                # Collision in top two rows = game over
                if self.y_offset < 2: self.game_over = True
                return False

        # Remove the old tetromino (if there is one) and place the new one
        self.clear_moving_blocks()
        for blocks in tetromino:
            y = blocks[0] + self.y_offset
            x = blocks[1] + self.x_offset
            color = self.colors[self.current_tetromino]
            self.grid[y][x] = (y, x, color, True)

        return True
    
    def rotate_tetromino(self):
        self.orientation += 1
        self.orientation = self.orientation%4
        self.insert_tetromino(False)
        

    def shift_moving_blocks(self, direction):
        moving_blocks = self.get_moving_blocks()
        if not moving_blocks: return False
        if direction == 'down':
            # Check for collision
            for blocks in moving_blocks:
                y = blocks[0]
                x = blocks[1]
                if y == self.height-1 or self.space_occupied(y+1,x): 
                    self.freeze_moving_blocks() 
                    return False
            # Replace old tetromino with new shifted one
            self.clear_moving_blocks()
            for blocks in moving_blocks:
                y = blocks[0] + 1
                x = blocks[1]
                color = blocks[2]
                self.grid[y][x] = (y,x,color,True)
            self.y_offset += 1
            return True
        
        if direction == 'left':
            # Check for collision
            for blocks in moving_blocks:
                y = blocks[0]
                x = blocks[1]
                if x == 0 or self.space_occupied(y,x-1): return False
            # Replace old tetromino with new shifted one
            self.clear_moving_blocks()
            for blocks in moving_blocks:
                y = blocks[0]
                x = blocks[1] - 1
                color = blocks[2]
                self.grid[y][x] = (y,x,color,True)
            self.x_offset -= 1
            return True

        if direction == 'right':
            # Check for collision
            for blocks in moving_blocks:
                y = blocks[0]
                x = blocks[1]
                if x == self.width - 1 or self.space_occupied(y,x+1): 
                    return False
            # Replace old tetromino with new shifted one
            self.clear_moving_blocks()
            for blocks in moving_blocks:
                y = blocks[0]
                x = blocks[1] + 1
                color = blocks[2]
                self.grid[y][x] = (y,x,color,True)
            self.x_offset += 1
            return True
        
    def clear_full_rows(self, count):
        # count keeps track of number of recursive calls
        for y in range(self.height):
            row_full = True
            for x in range(self.width):
                block = self.grid[y][x]
                if block[2] == '-' or block[3] == True:
                    row_full = False
                    break
            if row_full == True:
                for x in range(self.width):
                    self.grid[y][x] = (y,x,'-',False)
                self.shift_down_static_blocks(y)
                count += 1
                self.points += 100*count
                # Will continue calling function until all rows are cleared
                return self.clear_full_rows(count) 

        return count

    def swap(self):
        pass
        # Swap current_tetromino and swap_tetromino
        self.reset_offsets()
        if self.current_swap == 'e': 
            self.current_swap = self.current_tetromino
            self.insert_tetromino()
        else:
            tmp = self.current_tetromino
            self.current_tetromino = self.current_swap
            self.current_swap = tmp
            self.insert_tetromino(False)

    def get_blocks(self):
        blocks = []
        for y in range(self.height):
            for x in range(self.width):
                blocks.append(self.grid[y][x])
        return blocks
