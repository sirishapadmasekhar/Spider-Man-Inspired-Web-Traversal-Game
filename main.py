import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

spiderman = pygame.image.load("spiderman.png").convert_alpha()
spiderman = pygame.transform.scale(spiderman, (60, 60))

# Player
player = {"x": 100, "y": HEIGHT - 120, "vx": 0, "vy": 0}
target = None

# Stars
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT//2), random.randint(1,3)) for _ in range(100)]

# Buildings
buildings = [
    pygame.Rect(80, 250, 120, 450),
    pygame.Rect(260, 180, 140, 520),
    pygame.Rect(480, 220, 180, 480),
    pygame.Rect(750, 140, 150, 560)
]

# 🚗 Vehicles (visual only)
vehicles_right = [{"x": random.randint(0, WIDTH), "speed": random.randint(2,4),
                   "color": (255,200,0)} for _ in range(2)]

vehicles_left = [{"x": random.randint(0, WIDTH), "speed": random.randint(2,4),
                  "color": random.choice([(200,50,50),(50,200,200),(200,200,50)])} for _ in range(2)]

def draw_background():
    screen.fill((0, 0, 30))
    for x, y, r in stars:
        pygame.draw.circle(screen, (255,255,255), (x,y), r)

    pygame.draw.circle(screen, (230,230,255), (850,100), 40)
    pygame.draw.circle(screen, (0,0,30), (865,90), 35)

def draw_buildings():
    for b in buildings:
        pygame.draw.rect(screen, (20,20,30), b)

        for x in range(b.left+10, b.right-10, 20):
            for y in range(b.top+10, b.bottom-10, 25):
                if random.random() > 0.7:
                    pygame.draw.rect(screen, (255,215,100), (x,y,6,10))

def draw_road():
    road_y = HEIGHT - 80

    pygame.draw.rect(screen, (30,30,30), (0, road_y, WIDTH, 80))

    for x in range(0, WIDTH, 40):
        pygame.draw.rect(screen, (200,200,200), (x, road_y+35, 20, 5))

    pygame.draw.rect(screen, (80,80,80), (0, road_y-20, WIDTH, 20))

    return road_y

def draw_vehicles(road_y):
    # Right lane
    for v in vehicles_right:
        v["x"] += v["speed"]
        if v["x"] > WIDTH:
            v["x"] = -60

        y = road_y + 45
        pygame.draw.rect(screen, v["color"], (v["x"], y, 60, 20))
        pygame.draw.circle(screen, (0,0,0), (int(v["x"]+10), y+20), 5)
        pygame.draw.circle(screen, (0,0,0), (int(v["x"]+50), y+20), 5)

    # Left lane
    for v in vehicles_left:
        v["x"] -= v["speed"]
        if v["x"] < -60:
            v["x"] = WIDTH

        y = road_y + 10
        pygame.draw.rect(screen, v["color"], (v["x"], y, 60, 20))
        pygame.draw.circle(screen, (0,0,0), (int(v["x"]+10), y+20), 5)
        pygame.draw.circle(screen, (0,0,0), (int(v["x"]+50), y+20), 5)

def get_hand():
    return (player["x"]+10, player["y"]-10)

running = True
while running:
    draw_background()
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Only buildings clickable
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buildings:
                if b.collidepoint(mx, my):
                    target = (mx, my)
                    player["vy"] = -6
                    break

    # Movement
    if target:
        dx = target[0] - player["x"]
        dy = target[1] - player["y"]
        dist = math.hypot(dx, dy)

        if dist < 10:
            target = None
        else:
            player["vx"] += dx * 0.02
            player["vy"] += dy * 0.02

    # Gravity
    player["vy"] += 0.3

    # Move
    player["x"] += player["vx"]
    player["y"] += player["vy"]

    # Damping
    player["vx"] *= 0.92
    player["vy"] *= 0.92

    # Landing
    for b in buildings:
        if player["x"] > b.left and player["x"] < b.right:
            if player["vy"] > 0 and player["y"] + 30 > b.top:
                player["y"] = b.top - 30
                player["vy"] = 0

    if player["y"] > HEIGHT - 100:
        player["y"] = HEIGHT - 100
        player["vy"] = 0

    # Bounds
    player["x"] = max(20, min(WIDTH-20, player["x"]))
    player["y"] = max(20, min(HEIGHT-20, player["y"]))

    # Draw world
    draw_buildings()
    road_y = draw_road()
    draw_vehicles(road_y)

    # Web
    if target:
        pygame.draw.line(screen, (255,255,255), get_hand(), target, 2)

    # Spider-Man
    angle = math.degrees(math.atan2(player["vy"], player["vx"]))
    img = pygame.transform.rotate(spiderman, -angle)
    rect = img.get_rect(center=(player["x"], player["y"]))
    screen.blit(img, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()