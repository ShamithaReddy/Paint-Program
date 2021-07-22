from utils import *

WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint-it")


def init_grid(rows,cols,colour):
    grid=[]
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(colour)
    return(grid)      

def draw_grid(window,grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pygame.draw.rect(window,grid[j][i],(i*PIXEL_SIZE,j*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(len(grid)+1):
            pygame.draw.line(window,BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))
        for j in range(len(grid[0])+1):
            pygame.draw.line(window,BLACK,(j*PIXEL_SIZE,0),(j*PIXEL_SIZE,HEIGHT-TOOLBAR_HEIGHT))


def draw(window,grid,buttons):
    window.fill(BG_COLOUR)
    draw_grid(window,grid)
    for button in buttons:
        button.draw(window)
    pygame.display.update()


def get_row_col_from_pos(pos):
    x,y=pos
    row=y//PIXEL_SIZE
    col=x//PIXEL_SIZE
    if row>=ROWS:
        raise IndexError
    return(row,col)


run=True
#every computer has some time limit to run, if your computer is fast then the below while loop may run faster than someone with samller computer
#so we need to set a time limit of while loop
clock=pygame.time.Clock()
grid=init_grid(ROWS,COLS,BG_COLOUR)
drawing_colour=BLACK


button_y=HEIGHT-TOOLBAR_HEIGHT/2-25
buttons=[
    Button(10,button_y,50,50,BLACK),
    Button(70,button_y,50,50,RED),
    Button(130,button_y,50,50,BLUE),
    Button(190,button_y,50,50,GREEN),
    Button(250,button_y,50,50,PINK),
    Button(310,button_y,50,50, YELLOW),
    Button(370,button_y,50,50,ORANGE),
    Button(430,button_y,50,50,WHITE,"Earase",BLACK),
    Button(490,button_y,50,50,WHITE,"Clear",BLACK)
]

#pygame.event.get() gives you a list of events that occur, and when the event is quit then the while loop ends until then it continuously runs
while(run):
    #so this will make sure that we are not runnin faster than 60 FPS or 60 iterations of while loop/sec
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #if left_mouse button we give 0,middle=1, right mouse_button=2
        if pygame.mouse.get_pressed()[0]:
            pos=pygame.mouse.get_pos()#this gives us the x,y position of wher ethe mouse is pressed
            try:
                row,col=get_row_col_from_pos(pos)
                grid[row][col]=drawing_colour
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_colour=button.colour
                    if button.text=="Clear":
                        grid=init_grid(ROWS,COLS,BG_COLOUR)
                        drawing_colour=BLACK
                    
                            
                        
    draw(WINDOW,grid,buttons)

pygame.quit()