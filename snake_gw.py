'''
file for gamewindow of snake game
for all that stuff
'''

from snake_misc import *


class GameWindow(pygame.Surface):
    def __init__(self, sidelen):
        super().__init__((sidelen, sidelen))
        self.fill(GW_COLOR)

        self.snake = Snake(0, 0)
        self.food = None

        self.place_food()
    
    def place_food(self):
        coord = self.snake.fruitCoords()
        self.food = Fruit(coord)
    
    def update_gw(self, key):
        self.snake.update_segs(key)

        fruit, len, lose = 0, self.snake.length, False

        if self.snake.head.rect.colliderect(self.food.rect):
            self.snake.add()
            fruitCoord = self.snake.fruitCoords()
            self.food = Fruit(fruitCoord)
            fruit += 1

        if self.snake.head.rect.left < 0 or self.snake.head.rect.right > GW_SIZE or self.snake.head.rect.top < 0 or self.snake.head.rect.bottom > GW_SIZE:
            lose = True
        
        if self.snake.snake_hit():
            print('hi?')
            lose = True

        self.fill(GW_COLOR)

        self.snake.draw(self)
        self.food.draw(self)

        return fruit, len, lose
        




class Segment:
    def __init__(self, dir, x, y, start=True):
        self.surf = pygame.Surface( (SEGMENT_SIZE, SEGMENT_SIZE) )
        self.surf.fill( SNAKE_COLOR )
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)

        self.x = x
        self.y = y

        self.start = start

        self.next_dir = None
        self.direction = dir
        self.next = None
    

    def update(self, new_dir=None):
        if not self.start:
            return

        if new_dir:
            self.next_dir = new_dir

        dx, dy = DIRECTIONS[self.direction]
        self.rect.move_ip(dx, dy)
        
        if self.next:
            self.next.update(self.direction)

        x, y = self.rect.centerx, self.rect.centery
        if x % GRID_MID == 0 and y % GRID_MID == 0 and x % GRID_SIZE != 0 and y % GRID_SIZE != 0:
            self.x, self.y = backCoord(x, y)

            if self.next and not self.next.start:
                self.next.start = True

            if self.next_dir is not None:
                self.direction = self.next_dir
                self.next_dir = None
    
    def add(self):
        if self.next:
            self.next.add()
        else:
            new_x = self.rect.centerx
            new_y = self.rect.centery
            self.next = Segment(self.direction, new_x, new_y, False)
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)

        if self.next:
            self.next.draw(screen)
    
    def goodCoords(self, coords):
        if coords == (self.x, self.y):
            return False
        elif self.next:
            return self.next.goodCoords(coords)
        else:
            return True


class Snake:
    def __init__(self, x_coord, y_coord):
        x, y = coord(x_coord, y_coord)
        self.head = Segment(K_RIGHT, x, y)
        self.length = 1

        self.add()
    
    def update_segs(self, new_dir=None):
        self.head.update(new_dir)
    
    def draw(self, screen):
        self.head.draw(screen)
    
    def add(self):
        self.length += 1
        self.head.add()
    
    def fruitCoords(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        
        while not self.head.goodCoords( (x, y) ):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        
        return x, y

    def snake_hit(self):
        if self.length < 2:
            return False

        current = self.head.next.next

        if current and current.start == False:
            return False

        while current:
            if self.head.rect.colliderect(current.rect):
                return True
            current = current.next
        
        return False
        

class Fruit:
    def __init__(self, coords):
        self.surf = pygame.Surface((SEGMENT_SIZE, SEGMENT_SIZE), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        self.rect.center = coord(coords[0], coords[1])

        pygame.draw.circle(self.surf, FOOD_COLOR, (25, 25), SEGMENT_SIZE // 2 - 5 )
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)