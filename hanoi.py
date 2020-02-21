import pygame

# pygame globals
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tower of Hanoi')
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")
black = (0, 0, 0)

# number of levels
n = 3

# the space between the 3 bars
bar_width = 10
bar_height = 250
space_between = (screen_width / (n+1))
stand_height = (screen_height / 6)
bottom_height = screen_height - stand_height

#disks
disk_width = 100
disk_height = 20
start_desk_x = space_between - disk_width/2 + bar_width/2

#each disk data coordinates
a_x = -100
a_y = -100
b_x = -100
b_y = -100
c_x = -100
c_y = -100

# bars lists
list_1 = [1, 2, 3]
list_2 = []
list_3 = []

# status variables
over = False
clicked = False
disk = 0
watch = False
win = False

def render_list(my_list, num):
    global a_x, a_y, b_x, b_y, c_x, c_y

    size = len(my_list)

    j = 0

    # setting the offset(x,y) of each disk in the bar(list) according to the "num" of bar horizontally
    # and the number of disks in each bar
    for disk_type in my_list:
        if disk_type == 1:
            a_x = start_desk_x + (space_between*(num-1))
            a_y = bottom_height - disk_height*(size-j)
        if disk_type == 2:
            b_x = (start_desk_x - 50/2) + (space_between*(num-1))
            b_y = bottom_height - disk_height*(size-j)
        if disk_type == 3:
            c_x = (start_desk_x - 100/2) + (space_between*(num-1))
            c_y = bottom_height - disk_height*(size-j)
        j += 1

def update_lists(my_list):
    global disk, clicked, list_1, list_2, list_3

    # routing so it can be easy to handle
    if my_list == list_1:
        list_a = list_1
        list_b = list_2
        list_c = list_3
    elif my_list == list_2:
        list_a = list_2
        list_b = list_1
        list_c = list_3
    elif my_list == list_3:
        list_a = list_3
        list_b = list_1
        list_c = list_2

    # if there's nothing in the bar or there's a desk that's bigger than the selected one then add it to this bar
    # and remove it from other bars (lists)
    if disk == 1 or disk == 2 or disk == 3:
        if len(list_a) == 0 or disk <= list_a[0]:
            if disk not in list_a:
                list_a.insert(0, disk)
                if disk in list_b: list_b.remove(disk)
                if disk in list_c: list_c.remove(disk)

    # set each original list to it's corresponding one
    if my_list == list_1:
        list_1 = list_a
        list_2 = list_b
        list_3 = list_c
    elif my_list == list_2:
        list_2 = list_a
        list_1 = list_b
        list_3 = list_c
    elif my_list == list_3:
        list_3 = list_a
        list_1 = list_b
        list_2 = list_c

# displaying text when the player is winning
def font():
        pygame.font.init()
        my_font = pygame.font.SysFont('arial', 90)
        my_font2 = pygame.font.SysFont('arial', 40)
        text_surface = my_font.render(str("congratulations!"), True, (250, 250, 250))
        text_surface2 = my_font2.render(str("Press [space] to play again!"), True, (250, 250, 250))
        screen.blit(text_surface, (screen_width/2 - 260, screen_height/2 - 250))
        screen.blit(text_surface2, (screen_width/2 - 200, screen_height/2 - 147))
        
# to set the frames of the game
clock = pygame.time.Clock()

while not over:

    # the x-axis and y-axis of the mouse cursor inside the game window
    x_pos = pygame.mouse.get_pos()[0]
    y_pos = pygame.mouse.get_pos()[1]
    
    for event in pygame.event.get():
        #if exit button of window is clicked or escape button on keyboard then quite the game
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and win:
                # reset the game
                list_1 = [1, 2, 3]
                list_2 = []
                list_3 = []
                watch = False
                win = False

        # if left mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # if the player pressed on the top desk then select it
            if a.collidepoint(pygame.mouse.get_pos()):
                clicked = True
                disk = 1
                
            # if the player pressed on the middle desk then select it if nothing is on top of it
            elif b.collidepoint(pygame.mouse.get_pos()) and not a.collidepoint(b.x + (disk_width+50)/2, b.y-1):
                clicked = True
                disk = 2
                
            # if the player pressed on the bottom desk then select it if nothing is on top of it
            elif c.collidepoint(pygame.mouse.get_pos()) and not (a.collidepoint(c.x + (disk_width+100)/2, c.y-1) or b.collidepoint(c.x + (disk_width+100)/2, c.y-1)):
                clicked = True
                disk = 3

        # if left mouse button is released
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # bar_1 logic
            if x_pos >= bar_1.x - 20 and x_pos <= bar_1.x + bar_width + 20 and y_pos >= bar_height and y_pos <= bottom_height and clicked:
                update_lists(list_1)

            # bar_2 logic
            if x_pos >= bar_2.x - 20 and x_pos <= bar_2.x + bar_width + 20 and y_pos >= bar_height and y_pos <= bottom_height and clicked:
                update_lists(list_2)

            # bar_3 logic
            if x_pos >= bar_3.x - 20 and x_pos <= bar_3.x + bar_width + 20 and y_pos >= bar_height and y_pos <= bottom_height and clicked:
                update_lists(list_3)

            # reset so the desk doesn't follow the cursor anymore
            clicked = False
            disk = 0

                
    screen.fill((230, 230, 230))
    
    # to add the background after the solid white fill
    screen.blit(background, (0, 0))

    # rendering each list(disks) into bars
    if len(list_1) > 0:
        render_list(list_1, 1)
    if len(list_2) > 0:
        render_list(list_2, 2)
    if len(list_3) > 0:
        render_list(list_3, 3)

    # the 3 bars
    bar_1 = pygame.draw.rect(screen, black, pygame.Rect(space_between, bottom_height - bar_height, bar_width , bar_height))
    bar_2 = pygame.draw.rect(screen, black, pygame.Rect(space_between*2, bottom_height- bar_height, bar_width , bar_height))
    bar_3 = pygame.draw.rect(screen, black, pygame.Rect(space_between*3, bottom_height - bar_height, bar_width , bar_height))

    # the stand
    pygame.draw.rect(screen, black, pygame.Rect(0, bottom_height, screen_width, stand_height))

    # when clicking on a desk select it if possible
    if clicked and disk == 1:
        a_x = x_pos - 100/2
        a_y = y_pos - 20/2
    elif clicked and disk == 2:
        b_x = x_pos - 150/2
        b_y = y_pos - 20/2
    elif clicked and disk == 3:
        c_x = x_pos - 200/2
        c_y = y_pos - 20/2

    # disks
    a = pygame.draw.rect(screen, (247, 143, 179), pygame.Rect(a_x, a_y, disk_width, disk_height))
    b = pygame.draw.rect(screen, (198, 91, 123), pygame.Rect(b_x, b_y, disk_width+50, disk_height))
    c = pygame.draw.rect(screen, (138, 91, 143), pygame.Rect(c_x, c_y, disk_width+100, disk_height))

    # wach when all disks are moved from bar 1 so the next complete bar will be the answer
    # and stop when there's a complete bar (to prevent infinity loop of watch = true)
    if len(list_1) == 0 and len(list_2) < 3 and len(list_3) < 3:
        watch = True

    if (len(list_1) == 3 or len(list_2) == 3 or len(list_3) == 3) and watch == True:
        font()
        win = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
