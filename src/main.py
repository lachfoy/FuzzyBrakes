import pygame
import fuzzy
import cars

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def drawText(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text = font.render(text, True, (0,0,0))
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    screen.blit(text, textRect)

# Initialise sim variables 
leadCar = cars.LeadCar()
targetCar = cars.TargetCar(leadCar)
brakeStrength = 0

# Run until the user asks to quit
running = True
while running:
    # Update data
    leadCar.updatePos()
    brakeStrength = fuzzy.computeBraking(targetCar.speed, targetCar.posFromLead)
    targetCar.updateSpeed(brakeStrength)
    targetCar.updatePos()

    # Draw screen
    screen.fill((255, 255, 255))

    line = 40
    pad = 4
    drawText(screen, "Tickrate: "       + str(int(clock.get_fps())),    32, pad, pad)
    drawText(screen, "Target Speed: "   + str(targetCar.speed),         32, pad, 1 * line + pad)
    drawText(screen, "Lead Speed: "     + str(leadCar.speed),           32, pad, 2 * line + pad)
    drawText(screen, "Distance: "       + str(targetCar.posFromLead),   32, pad, 3 * line + pad)
    drawText(screen, "Brake: "          + str(brakeStrength),           32, pad, 4 * line + pad)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30) # Limit tickrate
    pygame.display.update()

# Done! Time to quit.
pygame.quit()