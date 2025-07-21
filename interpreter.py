import time
import pygame
import sys

if len(sys.argv) == 2:
	file = open(sys.argv[1], "r").read()
else:	
	file = """++++++++++[>++++++<-]>+++++.>++++++++++.<.++"""
print(file)
if "#" in file:
    pygame.init()

    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Brainf**k Interpreter :3")

def tokenize(file):
    spfile = list(file)
    token = []
    for i in spfile:
        if i == "+" or i == "-" or i == ">" or i == "<" or i == "." or i == "," or i == "[" or i == "]" or i == "#":
            token.append(i)
    return token
def interpret(token):
    stack = [0]*255
    dp = 0
    ip = 0
    savepos = []
    fipos = []
    donepos = []
    for i in token:
        if i == "[":
            savepos.append(["[", ip])
        if i == "]":
            savepos.append(["]", ip])
        ip += 1
    print(savepos)
    for i in savepos:
        if fipos == []:
            fipos.append(i)
        if fipos[0][0] == i[0]:
            fipos.append(i)
        if fipos[len(fipos)-1][0] != i[0]:
            donepos.append([fipos[len(fipos)-1], i])
            fipos.remove(fipos[len(fipos)-1])
    print(donepos)
    ip = 0
    while ip != len(token):
        i = token[ip]
        if i == "+":
            if 1 + stack[dp] == 256:
                stack[dp] = 0
            else:
                stack[dp] += 1
        if i == "-":
            if stack[dp] - 1 == -1:
                stack[dp] = 255
            else:
                stack[dp] -= 1
        if i == "<":
            if dp == 0:
                dp = 254
            else:
                dp -= 1
        if i == ">":
            if dp == 254:
                dp = 0
            else:
                dp += 1
        if i == ".":
            print(chr(stack[dp]), end=" ")
        if i == ",":
            stack[dp] = ord(list(input())[0])
        if i == "[":
            if stack[dp] == 0:
                for i in donepos:
                    if i[0][1] == ip:
                        ip = i[1][1]
        if i == "]":
            if stack[dp] != 0:
                for i in donepos:
                    if i[1][1] == ip:
                        ip = i[0][1]
        if "#" in token:
            x = 0
            y = 0
            screen.fill((0, 0, 0))
            for i in stack:
                if i >= 1:
                    pygame.draw.rect(screen, (255, 255, 255), ((x, y), (80, 80)))
                x += 80
                if x == 640:
                    x = 0
                    y += 80
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        ip += 1
        if "#" in token:
            print(stack)
print(tokenize(file))
interpret(tokenize(file))
if "#" in file:
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
# Made in Germany by Arnotronix


