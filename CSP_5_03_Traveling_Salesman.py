import math
import random
import pygame
import itertools


def getDistance(spot1, spot2):
    # Given two coordinates in a plane return the distance between those two points.
    return math.sqrt((spot1[0] - spot2[0]) ** 2 + (spot1[1] - spot2[1]) ** 2)


def getPathDistance(places: list):
    # Given a list of x,y coordinates return the distance it would take
    # to go to each coordinate in order and then back to the start.
    dist = 0
    for i in range(len(places) - 1):
        dist += getDistance(places[i], places[i + 1])

    if len(places) > 1:
        dist += getDistance(places[-1], places[0])

    return dist


def generatePermutations(places: list):
    # a function that given a list will return all possible permutations of the list.
    return list(itertools.permutations(places))


def full_TSP(places: list):
    # Check the distance of all possible different paths one could take
    # and return the path with the shortest distance
    # Print out the number of distance calculations you had to do.

    bestRoute = []
    bestDistance = float("inf")
    calculations = 0

    for perm in generatePermutations(places):
        calculations += 1
        dist = getPathDistance(list(perm))
        if dist < bestDistance:
            bestDistance = dist
            bestRoute = list(perm)

    print(f"there were {calculations} calculations for full TSP")
    return bestRoute


def hueristic_TSP(places: list):
    # Perform a heuristic calculation for traveling salesman.
    # Nearest-neighbor approach

    if not places:
        return []

    calculations = 0
    path = [places.pop(0)]

    while places:
        current = path[-1]
        closest = None
        closestDist = float("inf")

        for spot in places:
            calculations += 1
            d = getDistance(current, spot)
            if d < closestDist:
                closestDist = d
                closest = spot

        path.append(closest)
        places.remove(closest)

    print(f"there were {calculations} calculations for hueristic TSP")
    return path


def generate_RandomCoordinates(n):
    # Creates a list of random coordinates
    newPlaces = []
    for i in range(n):
        newPlaces.append([random.randint(10, 790), random.randint(10, 590)])
    return newPlaces


places = [[80, 75], [100, 520], [530, 300], [280, 200], [350, 150], [700, 120], [400, 500]]


def DrawExample(places):
    # Draws the TSP showcase to the screen.

    TSP = full_TSP(places.copy())
    Hueristic = hueristic_TSP(places.copy())

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))
    font = pygame.font.SysFont(None, 36)
    text_rect = pygame.Rect(0, 740, 800, 50)

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Draw full TSP (red)
        for i in range(len(TSP) - 1):
            pygame.draw.line(
                screen, (255, 0, 0),
                (TSP[i][0], TSP[i][1]),
                (TSP[i + 1][0], TSP[i + 1][1]),
                8
            )
        if len(TSP) >= 1:
            pygame.draw.line(
                screen, (255, 0, 0),
                (TSP[0][0], TSP[0][1]),
                (TSP[-1][0], TSP[-1][1]),
                8
            )

        # Draw heuristic TSP (blue)
        for i in range(len(Hueristic) - 1):
            pygame.draw.line(
                screen, (0, 0, 255),
                (Hueristic[i][0], Hueristic[i][1]),
                (Hueristic[i + 1][0], Hueristic[i + 1][1]),
                4
            )
        if len(Hueristic) >= 1:
            pygame.draw.line(
                screen, (0, 0, 255),
                (Hueristic[0][0], Hueristic[0][1]),
                (Hueristic[-1][0], Hueristic[-1][1]),
                4
            )

        # Draw points
        for spot in places:
            pygame.draw.circle(screen, (0, 0, 0), (spot[0], spot[1]), 10)

        # Draw legend
        text_surface = font.render(
            "Red = Full TSP (Optimal)   Blue = Heuristic (Fast)",
            True,
            (0, 0, 0)
        )
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


DrawExample(places)
# DrawExample(generate_RandomCoordinates(5))  # Do not go above ~9 points