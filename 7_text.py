import pygame
#############################################################
# 기본 초기화 ( 반드시 해야 하는 것들 )
pygame.init()  # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("GAME")  # 게임이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 .. )

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

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/hanseung-won/PycharmProjects/Pang_Game/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2  # 화면의 중앙
enemy_y_pos = screen_height / 2 - enemy_height / 2

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트,크기), None = 디폴트 폰트

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick 을 받아옴

# 이벤트 루프
running = True  # 게임의 진행 여부
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정(30)
    # print("fps:"+str(clock.get_fps())) #FPS출력

#############################################################
# 2. 이벤트 처리 ( 키보드, 마우스 .. )
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

#############################################################
# 3. 게임 캐릭터 위치 정의
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

#############################################################
# 4. 충돌 처리

    # 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # rect 정보를 실제 캐릭터의 위치로 업데이트
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):  # 사각형기준으로 충돌이 있는지 확인하는 함수
        print("충돌!")
        running = False
#############################################################
# 5. 화면에 그리기

    screen.blit(background, (0, 0))  # 이미지의 위치_좌표_왼쪽위가 0,0
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리

    # 타이머 집어 넣기
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과시간 계산, 경과시간(ms)을 1000으로 나누어서 초(s)단위로 표시
    timer = game_font.render("제한 시간:" + str(int(total_time - elapsed_time)) + "초", True, (255, 255, 255))
    # render(출력할 글자, True, 글자 색상 )
    # 남은시간 표시, render : 화면에 표시
    screen.blit(timer, (10, 10))

    # 만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃 ")
        running = False

    #꼭 필요
    pygame.display.update()  # 게임화면을 계속 그리기

# 종료 전 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기 (2000ms)
pygame.quit()
