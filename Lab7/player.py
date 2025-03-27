import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
s1, s2, s3 = "Cat.mp3", "cisum-sinep.mp3", "podlaya-evrejskaya-muzyka.mp3"
current = s1
last = s1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.mixer.music.load(current)
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_d:
                if pygame.mixer.music.get_busy(): 
                    pygame.mixer.music.stop()
                    srazu = True
                else:
                    srazu = False
                if current == s1: current = s2
                elif current == s2: current = s3
                else: current = s1
                if srazu: 
                    pygame.mixer.music.load(current)
                    pygame.mixer.music.play(-1)
            elif event.key == pygame.K_a:
                if pygame.mixer.music.get_busy(): 
                    pygame.mixer.music.stop()
                    srazu = True
                else:
                    srazu = False
                if current == s1: current = s3
                elif current == s2: current = s1
                else: current = s2
                if srazu:
                    pygame.mixer.music.load(current)
                    pygame.mixer.music.play(-1)