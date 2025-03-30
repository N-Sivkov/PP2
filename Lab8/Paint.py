import pygame

def main():
    """
    Y, B, and W to change colors (yellow, blue and white respectively); 
    click LMB to assign borders for figures; 
    R or C to draw a rectangle or a circle within the set borders respectively; 
    E to switch the eraser mode on/off"
    """
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    YELLOW, BLUE, WHITE = (255, 255, 0), (0, 0, 255), (255, 255, 255)
    color = YELLOW # predefined colors and one set by default

    radius = 15
    x = 0
    y = 0
    mode = '' #repurposed for defining the drawing mode selected
    points = []
    pos = [] # positions for future figure drawing
    figs = [] # list of parameters for existing figures
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    if len(pos) == 2: mode = 'rect'
                elif event.key == pygame.K_c:
                    if len(pos) == 2: mode = 'circle'
                elif event.key == pygame.K_e:
                    if mode == 'erase':
                        mode = ''
                    else:
                        mode = 'erase'
                    pos = []
                    points = [] # clear the green trace

                # color picker
                if event.key == pygame.K_y:
                    color = YELLOW
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_w:
                    color = WHITE
                
                if event.key == pygame.K_UP: # radius adjustments reassigned for arrow keys
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    pos.append(event.pos)
                    if len(pos) > 2: pos = pos[-2:] # only two points are required
                elif event.button == 3: # right click shrinks radius
                    pos = [] # clear the positions
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                if mode == "erase":
                    figs.append(["erase", position, radius])
                else:
                    points = points + [position]
                    points = points[-64:]
                
        screen.fill((0, 0, 0))
        
        # checking for current active mode
        if mode == "rect" and len(pos) == 2:
            figs.append(["rect", pos, color])
            pos = []
            mode = ""
        elif mode == "circle" and len(pos) == 2:
            figs.append(["circle", pos, color])
            pos = []
            mode = ""

        # re-applying all the user's actions
        for fig in figs:
            if fig[0] == "rect":
                drawRect(screen, fig[1], fig[2])
            elif fig[0] == "circle":
                drawCircle(screen, fig[1], fig[2])
            elif fig[0] == "erase":
                pygame.draw.circle(screen, (0, 0, 0), fig[1], fig[2]) # since this op-s scale is tied to the current value of the radius variable, no separate function for it

        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius)
            i += 1

        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRect(screen, pos, color):
    x1, x2, y1, y2 = min(pos[0][0], pos[1][0]), max(pos[0][0], pos[1][0]), min(pos[0][1], pos[1][1]), max(pos[0][1], pos[1][1])
    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, x2 - x1, y2 - y1))

def drawCircle(screen, pos, color):
    x1, x2, y1, y2 = min(pos[0][0], pos[1][0]), max(pos[0][0], pos[1][0]), min(pos[0][1], pos[1][1]), max(pos[0][1], pos[1][1])
    center = ((x2 + x1) // 2, (y2 + y1) // 2)
    radius = min((x2 - x1), (y2 - y1))
    pygame.draw.circle(screen, color, center, radius)

main()