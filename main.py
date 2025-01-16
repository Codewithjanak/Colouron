level = 1

player_pos = [
[4,4],
[2,8],
[1,7],
[1,7],
[6,8],
[1,7],
[5,8],
[5,8],
[1,7],
[4,8],
[3,8],
[4,4],
[6,6],
[4,6],
[3,5],
[4,5],
[4,5],
[6,3],
[4,5],
[3,5],
[0,0]
]

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			action  = False
		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action
import pygame , random 
from pygame import mixer
from level_data import *
pygame.init()
mixer.init()
screen1 = pygame.display.set_mode((100,200))
screen  = pygame.Surface((720,1550))
screen.fill("white")

def reset_level (data,x,y):
    player.reset (x,y,80)
    white_group.empty()
    net_group.empty()
    block_group.empty()
    world = World(data)
    return world
        
class particals_ ():
    def __init__ (self):
        self.particals = []
        
    def emit (self):
        if self.particals:
            self.del_particals()
            for partical in self.particals:
                partical[0][0] += partical[2][0]
                partical[0][1] += partical[2][1]
                partical[1] -= 0.2
                col = random.sample(range(50,255),3)
                #pygame.draw.circle(screen,("black"),partical[0],int(partical[1]))
                pygame.draw.rect(screen,("black"),(partical[0][0],partical[0][1],partical[1],partical[1]))
                pygame.draw.rect(screen,("white"),(partical[0][0],partical[0][1],partical[1],partical[1]),1)
                if partical[1] < 0:
                   # self.particals = []
                    pass
                
            
    def add_particals(self,pos):
        pos_x = pos[0]
        pos_y = pos[1]
        radius = 20
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        partical_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
        self.particals.append(partical_circle)
         #2 time partucal
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        partical_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
        #self.particals.append(partical_circle)
       
        
    def del_particals(self):
        partical_copy = [partical for partical in self.particals if partical[1] > 10]
        self.particals = partical_copy

class World():
    def __init__(self,data):
        self.data = data
        self.tile_list =[ ]
        self.tile_list_ = []
        self.shecking = False
        self.sheck = random.randint(-1,1)
        #load img
        row_count =0
        for row in self.data:
            col_count=0
            for tile in row:
                if tile == 35 :
                    block = Block(col_count * tile_size,row_count*tile_size)
                    block_group.add(block)
                    #temp
                    white = White_(col_count * tile_size,row_count*tile_size)
                    white__group.add(white)
                    img= pygame.image.load(f"img2/tile_032.png")
                    img=pygame.transform.scale(img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x= col_count * tile_size
                    img_rect.y= row_count * tile_size
                    tile = (img , img_rect)
                    self.tile_list_.append(tile)
                elif tile == 36 :
                    block2 = Block2(col_count * tile_size,row_count*tile_size)
                    block_group2.add(block2)
                    #temp
                    white = White_(col_count * tile_size,row_count*tile_size)
                    white__group.add(white)
                    img= pygame.image.load(f"img2/tile_032.png")
                    img=pygame.transform.scale(img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x= col_count * tile_size
                    img_rect.y= row_count * tile_size
                    tile = (img , img_rect)
                    self.tile_list_.append(tile)
                elif tile == 34 :
                    net = Net(col_count * tile_size,row_count*tile_size,2)
                    net_group.add(net)
                elif tile == 17 :
                    net = Net(col_count * tile_size,row_count*tile_size,0)
                    net_group.add(net)
                elif tile == 8 :
                    net = Net(col_count * tile_size,row_count*tile_size,1)
                    net_group.add(net)
                elif tile == 32 :
                    white = White(col_count * tile_size,row_count*tile_size)
                    white_group.add(white)
                    img= pygame.image.load(f"img2/tile_032.png")
                    img=pygame.transform.scale(img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x= col_count * tile_size
                    img_rect.y= row_count * tile_size
                    tile = (img , img_rect)
                    self.tile_list_.append(tile)
                elif tile != 0:
                    img= pygame.image.load(f"img2/tile_0{data[row_count][col_count]}.png")
                    img=pygame.transform.scale(img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x= col_count * tile_size
                    img_rect.y= row_count * tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count +=1
            
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            
        for tile_ in self.tile_list_:
            screen.blit(tile_[0],tile_[1])

class White (pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img2/tile_033.png")
            self.image = pygame.transform.scale(img,(80,80))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y  
            
class White_ (pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img2/tile_033.png")
            self.image = pygame.transform.scale(img,(80,80))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y                                      

class Block (pygame.sprite.Sprite):
        def __init__(self,x,y):
            self.block_pos = 1
            #block event
            self.block_event=pygame.USEREVENT + 1
            pygame.time.set_timer(self.block_event,2000)
            self.x = x
            self.y = y
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img2/tile_035.png")
            self.image = pygame.transform.scale(img,(80,80))
            self.rect = self.image.get_rect()
            
        def update (self,block_pos):
                    
            if  block_pos >= 0 :       
                self.rect.x = self.x
                self.rect.y = self.y
            else :
                 self.rect.x = -100
                 self.rect.y = 0     

class Block2 (pygame.sprite.Sprite):
        def __init__(self,x,y):
            self.block_pos = 1
            #block event
            self.block_event=pygame.USEREVENT + 1
            pygame.time.set_timer(self.block_event,2000)
            self.x = x
            self.y = y
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img2/tile_035.png")
            self.image = pygame.transform.scale(img,(80,80))
            self.rect = self.image.get_rect()
            
        def update (self,block_pos):
                    
            if  block_pos >= 0 :       
                self.rect.x = self.x
                self.rect.y = self.y
            else :
                 self.rect.x = -100
                 self.rect.y = 0                            
            
class Net (pygame.sprite.Sprite):
        def __init__(self,x,y,option):
            pygame.sprite.Sprite.__init__(self)
            if option == 0 :
                img = pygame.image.load("img2/tile_017.png")
            if option == 1 :
                img = pygame.image.load("img2/tile_08.png")
            if option == 2 :
                img = pygame.image.load("img2/tile_034.png")
            if option == 3:
                img = pygame.image.load("colour/colour_bomb.png")
            self.image = pygame.transform.scale(img,(80,80))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y                

class Player():
    def __init__(self, x, y,num):
        self.reset(x,y,num)
        
    def reset (self,x,y,num):
           img = pygame.image.load("img2/tile_031.png")
           self.image = pygame.transform.scale(img, (num,num))
           self.rect = self.image.get_rect()
           self.width = self.image.get_width()
           self.height = self.image.get_height()
           self.rect.x = x *num
           self.rect.y = y *num
           self.clicked = False
           self.level = 1
           self.dx = 0
           self.dy = 0
           self.move = self.dx + self.dy
           self.game = 1
           self.shacking = False
           
    
    def update (self,point):
           #movement speed
           self.shacking = False
           speed = 40
           janak = self.rect.x, self.rect.y, self.width, self.height
           but_J = pygame.Surface((103,180),pygame.SRCALPHA)
           but_J.fill((0,0,0,0))
           but_j = pygame.Surface((180,103),pygame.SRCALPHA)
           but_j.fill((0,0,0,0))
           
           #button
           but_1=Button(310,1050,but_J, 1)
           but_2=Button(310,1350,but_J, 1)
           but_3=Button(100,1240,but_j, 1)
           but_4=Button(430,1240,but_j, 1)
           
           if but_1 .draw(screen) and self.dx == 0 and self.dy == 0 :
               self.dy = -speed
               
           if but_2.draw(screen)and self.dx == 0 and self.dy == 0:
               self.dy = speed
               
           if but_3.draw(screen)and self.dx == 0 and self.dy == 0:
               self.dx = -speed
               
           if but_4.draw(screen)and self.dx == 0 and self.dy == 0:
               self.dx = speed
               
           
           if pygame.mouse.get_pressed()[0]== False :
               self.clicked = False
           
           # draw  good looking button    
           pygame.draw.rect(screen,(0,0,0),(100,1240,180,103),10,30)
           pygame.draw.rect(screen,(0,0,0),(430,1240,180,103),10,30)
           pygame.draw.rect(screen,(0,0,0),(310,1050,103,180),10,30)
           pygame.draw.rect(screen,(0,0,0),(310,1350,103,180),10,30)    
           for tile in world.tile_list:
            # Check for x/y axis collision
                 if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                     partical1.add_particals((self.rect.x + 30,self.rect.y + 30))
                     self.dy = 0
                     tap_fx.play()
                     self.shacking = True
                     
                 if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                     partical1.add_particals((self.rect.x + 30,self.rect.y + 30))
                     self.dx = 0
                     tap_fx.play()
                     self.shacking = True
          
                   
           if pygame.sprite.spritecollide(self,net_group,False):
               hit_fx.play()
               self.game = 0
             
           # white colour fill      
           if pygame.sprite.spritecollide(self,white_group,True):
               point += 1
               hit_fx.play()
               
           #temp white block
           if pygame.sprite.spritecollide(self,white__group,True):
               pass
               
            # check block collision
           #self.shacking = False
           for block in block_group2 :
               if block.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height) or block.rect.colliderect(self.rect.x, self.rect.y +self.dy , self.width, self.height):
                   partical1.add_particals((self.rect.x + 30,self.rect.y + 30))
                   self.dx = 0
                   self.dy = 0
                   tap_fx.play()
                   self.shacking = True
                           
           for block in block_group :
               if block.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height) or block.rect.colliderect(self.rect.x, self.rect.y +self.dy , self.width, self.height):
                   partical1.add_particals((self.rect.x + 30,self.rect.y + 30))
                   self.dx = 0
                   self.dy = 0
                   tap_fx.play()
                   self.shacking = True
               
           self.rect.y += self.dy
           self.rect.x += self.dx
           screen.blit(self.image,self.rect)
           return point                                 

def home(game):
    font = pygame.font.Font("freesansbold.ttf",100)
    font1 = pygame.font.Font("freesansbold.ttf",150)
    but_J = pygame.Surface((540,130),pygame.SRCALPHA)
    but_J.fill((0,0,0,100))
    but_0 = Button(90, 750, but_J, 1)
    but_1 = Button(90, 900, but_J, 1)
    if but_0.draw(screen):
        game = 100
    if but_1.draw(screen):
        game = 90
    pygame.draw.rect(screen, ("black"),(90,750,540,130),10)
    pygame.draw.rect(screen, ("black"),(90,900,540,130),10)    
    text = font.render("play game",False,("White"))
    screen.blit(text,(110,760))
    text = font.render("credit",False,("White"))
    screen.blit(text,(190,920))
    text = font1.render("Colouron",False,("black"))
    screen.blit(text,(10,330))
        
    return game
                
#load player img
player_img = pygame.image.load("img2/tile_031.png")
player_img = pygame.transform.scale(player_img, (600,600))

#reset png
reset_png = pygame.image.load("assets/reset.png").convert_alpha()
reset_png = pygame.transform.scale(reset_png,(100,100))

#load menu img
menu_png = pygame.image.load("assets/home.png").convert_alpha()
menu_png = pygame.transform.scale(menu_png,(720,1612))

#reset button 
but = pygame.Surface((100,100),pygame.SRCALPHA)
but .fill((0,0,0,00))
but_1=Button(30,1050,but, 1)

#back button 
but1= pygame.Surface((120,50),pygame.SRCALPHA)
but1 .fill((0,0,0,100))
but_2=Button(30,30,but1, 1)

#sounds 
level_fx = pygame.mixer.Sound("sounds/level.wav")
tap_fx = pygame.mixer.Sound("sounds/tap.wav") 
hit_fx = pygame.mixer.Sound("sounds/hit.wav")
out_fx = pygame.mixer.Sound("sounds/out.wav")           
                              


playerx = 4
playery = 4

# 4x4 ,2x8 
point = 0
win_point = 0
skip = 0

# count total point
world_data = world_data_list[0]
for data in world_data:
     point = data.count(j)
     win_point += point

#sprite Group 
white_group = pygame.sprite.Group()
white__group = pygame.sprite.Group()
net_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
block_group2 = pygame.sprite.Group()
block_pos = 5
block_pos2 = 10


#particals
partical1 = particals_()

#world data load
world = World(world_data)

player = Player(playerx,playery,num)
clock = pygame.time.Clock()

#fonts
font = pygame.font.Font("freesansbold.ttf",50)
font1 = pygame.font.Font("freesansbold.ttf",500)
font2 = pygame.font.Font("freesansbold.ttf",200)
font3 = pygame.font.Font("freesansbold.ttf",80)
font4 = pygame.font.Font("freesansbold.ttf",150)

credit = " janak katariya" 

game = 70
game1 = True

s = 0
s2 = 0

shack = 0

 
while game1:
    screen.fill("white")
    
    #count second 
    s += 1
    s2 += 1
    
    dtext= font.render(f"j{win_point},{point},{level},{game,block_pos}",False,(255,0,0))
   # screen.blit(dtext,(10,10))
    playerx,playery = player_pos[level-1][0], player_pos[level-1][1]
    
    if s == 120 :
        block_pos *= -1
        s = 0
    if s2 == 180 :
        block_pos2 *= -1
        s2 = 0
    
    # congratulations for game complete 
    if len(player_pos) == level :
        screen.fill("black")
        dtext= font3.render(f"congratulations",False,("white"))
        screen.blit(dtext,(40,100))
        dtext= font3.render(f"game ",False,("white"))
        screen.blit(dtext,(40,250))
        dtext= font2.render(f"100%",False,("white"))
        screen.blit(dtext,(150,350))
        dtext= font3.render(f"complete",False,("white"))
        screen.blit(dtext,(350,550))
        dtext= font.render("made by janak katariya",False,("white"))
        screen.blit(dtext,(0,1450))
        screen.blit(player_img,(50,700))
        
        #credit screen
    elif game == 90:
        screen.blit(menu_png,(0,-60))
        text = font4.render("Colouron",False,("black"))
        screen.blit(text,(10,330))
        dtext= font.render(f" {credit}",False,("black"))
        screen.blit(dtext,(150,750))
        if but_2.draw(screen):
            game = 70
        dtext= font.render(f"back",False,("white"))
        screen.blit(dtext,(30,30))
      
      # home screen  
    elif game == 70 :
        screen.blit(menu_png,(0,-60))
        game = home(game)      

   #draw level screen   
    elif game == 100 :
        l_x = 200
        if level > 9 :
            l_x = 75
        screen.fill("black")
        dtext= font1.render(f"{level}",False,("white"))
        screen.blit(dtext,(l_x,300))
        dtext= font2.render("Level",False,("white"))
        screen.blit(dtext,(100,800))
        #if pygame.mouse.get_pressed()[0]:
        skip += 1
        pygame.draw.circle(screen,("white"),(350,750),900,skip * 30)
        if skip == 35 :
            skip = 0
            game = level
            
    #reset level        
    elif game == 0 :
        skip += 1
        pygame.draw.circle(screen,("black"),(350,750),900,skip * 30)
        if skip == 35 :
            skip = 0
            world = reset_level(world_data,playerx,playery)
            point = 0
            win_point = 0
            for data in world_data_list[level-1]:
                 point_ = data.count(j)
                 win_point += point_
            game = 1
        
#levels and load world data
    elif level > 1 and game > 1:
        point = 0
        win_point = 0
        world_data = world_data_list[level-1]
        world = reset_level(world_data,playerx,playery)
        for data in world_data:
             point_ = data.count(j)
             win_point += point_
        game = 1   
   
      
#animation                                          
    elif game == -2:  
        screen.fill("black")
        skip += 1
        pygame.draw.circle(screen,("white"),(350,750),900,skip * 30)
        if skip == 35 :
            skip = 0
            game = 2
           
#main game loop         
    elif game != 0 :
        #screen.fill("white")
        world.draw()
        
        #sprite groups
        white_group.draw(screen)
        white__group.draw(screen)
        net_group.draw(screen)
        
        
        #block_pos *=-1
        block_group.update(block_pos)
        block_group.draw(screen)
        block_group2.update(block_pos2)
        block_group2.draw(screen)
        
        
        
        point = player.update(point)
        game = player.game
        
        #draw particals
        partical1.emit()
        
        #reset button 
        if but_1.draw(screen):
            game = 0
        pygame.draw.rect(screen,(0,0,0),(30,1050,100,100),0,20)
        screen.blit(reset_png,(30,1050))
        
        #reset game and animation 
        if point == win_point :
            skip += 1
            pygame.draw.circle(screen,(0,0,0),(350,750),900,skip * 30)
            if skip == 40 :
                point = 0
                win_point = 0
                skip = 0
                level += 1
                level_fx.play()
                game =  100
                
    #shacking for sometime        
    shack_xy = (0,0)
    if shack > 0:
        shack -= 1
        shack_xy = (
        random.randint(-3,4),
        random.randint(-3,4))
    if player.shacking :
        shack = 5
    
    screen1.blit(screen,(shack_xy))
    
    pygame.display.update()
    clock.tick(60)
     

    
    