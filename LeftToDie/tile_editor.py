import pygame
import tile_matrix
import os
pygame.display.init()
SCREEN_X_NS = 1024 #screen width w/o sidebar
SCREEN_X = 1224 #screen width w/ sidebar
SCREEN_Y = 768
BOX_SIZE = 32
H_BOXES =  32
V_BOXES =  24
surf = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
tile = pygame.image.load(os.path.join('Art','tileBlockNormal.png'))
spikes = pygame.image.load(os.path.join('Art','tileSpikeNormal.png'))
sidebar = pygame.image.load(os.path.join('Art', 'sidebar.png'))
def draw_grid(surface):
    for i in range(1,H_BOXES):
        pygame.draw.line(surface, pygame.Color(255,255,255,255), (i*BOX_SIZE,0),(i*BOX_SIZE,SCREEN_Y))
    for i in range(1,V_BOXES):
        pygame.draw.line(surface, pygame.Color(255,255,255,255),(0,i*BOX_SIZE),(SCREEN_X_NS,i*BOX_SIZE))
    pygame.display.update()
draw_grid(surf)
tm = tile_matrix.TileMatrix(H_BOXES,V_BOXES)
surf.blit(sidebar, pygame.Rect(SCREEN_X_NS, 0 , 200, SCREEN_Y))
pygame.display.update()

running = True
# X is erase, B is Block, S is spikes, I is Iniitial (start point), V is Victory (goal)
current_mode = "B" 
while(running):
    #get mouse click
    #find out which box it's in
    #draw rectangle in the box that's correct color
    #change matrix accordingly
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                current_mode = "B"
                print(current_mode)
            elif event.key == pygame.K_s:
                current_mode = "S"
                print(current_mode)
            elif event.key == pygame.K_d:
                current_mode = "X"
                print(current_mode)
            elif event.key == pygame.K_f:
                current_mode = "I"
            elif event.key == pygame.K_g:
                current_mode = "V"
            elif event.key == pygame.K_z:
                tm.save_to_file()
            elif event.key == pygame.K_q:
                pygame.display.quit()
        if pygame.mouse.get_pos()[0] <= SCREEN_X_NS:
            if pygame.mouse.get_pressed()[0]:
                box_x = pygame.mouse.get_pos()[0] // BOX_SIZE
                box_y = pygame.mouse.get_pos()[1] // BOX_SIZE
                start_x = box_x * BOX_SIZE
                start_y = box_y * BOX_SIZE

            #print(start_x,start_y,end_x,end_y)
                tm.change_cell(box_x, box_y, current_mode)
                print(box_x + 1, box_y+1)
                if current_mode == "B":
                    surf.blit(tile,pygame.Rect(start_x, start_y, BOX_SIZE, BOX_SIZE))
                    #color = pygame.Color(0,0,150,255)
                if current_mode == "S":
                    color = pygame.Color(0,0,0,255)
                    pygame.draw.rect(surf,color,(start_x,start_y,BOX_SIZE,BOX_SIZE))
                    surf.blit(spikes,pygame.Rect(start_x, start_y, BOX_SIZE, BOX_SIZE))
                    #color = pygame.Color(150,0,0,255)
                if current_mode == "X":
                    color = pygame.Color(0,0,0,255)
                    pygame.draw.rect(surf,color,(start_x,start_y,BOX_SIZE,BOX_SIZE))
                if current_mode == "I":
                    color = pygame.Color(255,255,255, 255)
                    pygame.draw.rect(surf, color, (start_x, start_y, BOX_SIZE, BOX_SIZE))
                if current_mode == "V":
                    color = pygame.Color(0,150,0,255)
                    pygame.draw.rect(surf, color, (start_x, start_y, BOX_SIZE, BOX_SIZE))


                draw_grid(surf)
                pygame.display.update()



            
    
    



