import pygame

pygame.init()  # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("PANG GAME")  # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/hanseung-won/PycharmProjects/Pang_Game/background.png")

# 캐릭터 불러오기
character = pygame.image.load("/Users/hanseung-won/PycharmProjects/Pang_Game/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면의 중앙
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.7
# 이벤트 루프
running = True  # 게임의 진행 여부

while running:
    dt = clock.tick(100)  # 게임화면의 초당 프레임 수를 설정(30)
    # print("fps:"+str(clock.get_fps())) #FPS출력
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False
        if event.type == pygame.KEYDOWN:  # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    # dt를 곱해줘야 FPS에 상관업이 속도 일정 (fps=이동의 부드러운 정도만 영향줌)
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 이미지의 위치_좌표_왼쪽위가 0,0
    # screen.fill((0,0,255)) #RGB값으로 색 채우기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면을 계속 그리기

pygame.quit()
