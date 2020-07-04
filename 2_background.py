import pygame

pygame.init()  # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("PANG GAME")  # 게임이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/hanseung-won/PycharmProjects/Pang_Game/background.png")
# 이벤트 루프
running = True  # 게임의 진행 여부

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False

    screen.blit(background, (0, 0))  # 이미지의 위치_좌표_왼쪽위가 0,0
    # screen.fill((0,0,255)) #RGB값으로 색 채우기
    pygame.display.update()  # 게임화면을 계속 그리기

pygame.quit()
