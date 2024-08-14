import pygame
import button

pygame.init()
run = True
game_state = 'main'
music_state = True
sounds_state = True

font72 = pygame.font.Font("Fonts/HitandRun.otf", 36)
click = pygame.mixer.Sound("Sounds/tick.mp3")
pygame.mixer.music.load("Sounds/bgr_music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

WIDTH = 640
HEIGHT = 640
size_of_board = 450
dot_color = (222, 208, 182)
edge_color = (96, 114, 116)
hover_edge_color = (178, 165, 155)
score_color = (255, 255, 255)

number_of_dots = 3
dot_width = 0
edge_width = 0
distance_between_dots = 0


def update_board():
    global dot_width, edge_width, distance_between_dots
    dot_width = (0.25 * size_of_board / number_of_dots) / 2
    edge_width = int(dot_width * 2)
    distance_between_dots = size_of_board / number_of_dots

number_of_player = 2
curr_player = 1
player_list = [1, 2]
winner = []

player1_color = (59, 168, 215)
player1_color_light = (133, 178, 191)
player1_score = 0
player1_box = []

player2_color = (248, 49, 87)
player2_color_light = (227, 119, 127)
player2_score = 0
player2_box = []

player3_color = (136, 171, 142)
player3_color_light = (175, 200, 173)
player3_score = 0
player3_box = []

player4_color = (255, 227, 130)
player4_color_light = (255, 247, 138)
player4_score = 0
player4_box = []

hr_line_arr = []
vr_line_arr = []

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes")

BG = pygame.image.load("Assets/background.png")
MENU = pygame.image.load("Assets/menu.png")
OPTIONS = pygame.image.load("Assets/options.png")
PLAY_BACKGROUND = pygame.image.load("Assets/play_bgr.png")
HOW_TO_PLAY = pygame.image.load("Assets/howtoplay.png")
SETTINGS = pygame.image.load("Assets/settings.png")
X = pygame.image.load("Assets/x.png")
RESULT_BACKGROUND = pygame.image.load("Assets/result_bgr.png")

PLAYER1 = pygame.image.load("Assets/p1.png")
PLAYER2 = pygame.image.load("Assets/p2.png")
PLAYER3 = pygame.image.load("Assets/p3.png")
PLAYER4 = pygame.image.load("Assets/p4.png")

player1_score_bgr = pygame.image.load("Assets/p1_point.png")
player2_score_bgr = pygame.image.load("Assets/p2_point.png")
player3_score_bgr = pygame.image.load("Assets/p3_point.png")
player4_score_bgr = pygame.image.load("Assets/p4_point.png")

player1_turn = pygame.image.load("Assets/p1_turn.png")
player2_turn = pygame.image.load("Assets/p2_turn.png")
player3_turn = pygame.image.load("Assets/p3_turn.png")
player4_turn = pygame.image.load("Assets/p4_turn.png")

play_button_img = pygame.image.load("Assets/play_btn.png").convert_alpha()
start_button_img = pygame.image.load("Assets/start_btn.png").convert_alpha()
howtoplay_button_img = pygame.image.load("Assets/howtoplay_btn.png").convert_alpha()
settings_button_img = pygame.image.load("Assets/settings_btn.png").convert_alpha()
back_button_img = pygame.image.load("Assets/back.png").convert_alpha()
on_button_img = pygame.image.load("Assets/on_btn.png").convert_alpha()
off_button_img = pygame.image.load("Assets/off_btn.png").convert_alpha()
left_arrow_button_img = pygame.image.load("Assets/left_arrow_btn.png").convert_alpha()
right_arrow_button_img = pygame.image.load("Assets/right_arrow_btn.png").convert_alpha()
play_again_button_img = pygame.image.load("Assets/play_again_btn.png").convert_alpha()
menu_button_img = pygame.image.load("Assets/menu_btn.png").convert_alpha()

play_button = button.Button(132.1, 305.8, play_button_img)
start_button = button.Button(168.5, 445.2, start_button_img)
howtoplay_button = button.Button(132.1, 431.9, howtoplay_button_img)
settings_button = button.Button(566.7, 15, settings_button_img)
back_button = button.Button(15, 15, back_button_img)
music_on_button = button.Button(375.9, 257, on_button_img)
music_off_button = button.Button(375.9, 257, off_button_img)
sounds_on_button = button.Button(375.9, 408, on_button_img)
sounds_off_button = button.Button(375.9, 408, off_button_img)
player_decrease_button = button.Button(311.7, 232.2, left_arrow_button_img)
player_increase_button = button.Button(458.3, 232.2, right_arrow_button_img)
size_decrease_button = button.Button(311.7, 353.6, left_arrow_button_img)
size_increase_button = button.Button(458.3, 353.6, right_arrow_button_img)
play_again_button = button.Button(168.5,444.6, play_again_button_img)
menu_button = button.Button(168.5, 539.2, menu_button_img)


def draw_dots():
    update_board()
    dots_arr = []
    for i in range(number_of_dots):
        temp_arr = []
        for j in range(number_of_dots):
            x = 95 + i * distance_between_dots + distance_between_dots / 2
            y = 95 + j * distance_between_dots + distance_between_dots / 2
            pygame.draw.circle(WIN, dot_color, (int(x), int(y)), int(dot_width))
            temp_arr.append((x, y))
        dots_arr.append(temp_arr)
    return dots_arr


def hover_edge(no_of_dots):
    dots_arr = draw_dots()
    mouse_pos = pygame.mouse.get_pos()

    for i in range(no_of_dots - 1):
        for j in range(no_of_dots):
            cord = dots_arr[i][j]
            next_cord = dots_arr[i + 1][j]

            if ([cord, next_cord] not in hr_line_arr
                    and cord[0] + 10 < mouse_pos[0] < next_cord[0] - 10
                    and cord[1] - dot_width < mouse_pos[1] < cord[1] + dot_width):
                pygame.draw.line(WIN, hover_edge_color,
                                 (cord[0], cord[1] - 1),
                                 (next_cord[0], next_cord[1] - 1), int(edge_width))

    for i in range(no_of_dots):
        for j in range(no_of_dots - 1):
            cord = dots_arr[i][j]
            next_cord = dots_arr[i][j + 1]

            if ([cord, next_cord] not in vr_line_arr
                    and cord[1] + 10 < mouse_pos[1] < next_cord[1] - 10
                    and cord[0] - dot_width < mouse_pos[0] < cord[0] + dot_width):
                pygame.draw.line(WIN, hover_edge_color,
                                 (cord[0] - 1, cord[1]),
                                 (next_cord[0] - 1, next_cord[1]), int(edge_width))


def draw_edge():
    for cord_arr in hr_line_arr:
        pygame.draw.line(WIN, edge_color,
                         (cord_arr[0][0], cord_arr[0][1] - 1),
                         (cord_arr[1][0], cord_arr[1][1] - 1), int(edge_width))
    for cord_arr in vr_line_arr:
        pygame.draw.line(WIN, edge_color,
                         (cord_arr[0][0] - 1, cord_arr[0][1]),
                         (cord_arr[1][0] - 1, cord_arr[1][1]), int(edge_width))


def score(start_x, start_y, width, height):
    global player1_score, player2_score, player3_score, player4_score
    if curr_player == 1:
        player1_score += 1
        player1_box.append((start_x, start_y, width, height))
    elif curr_player == 2:
        player2_score += 1
        player2_box.append((start_x, start_y, width, height))
    elif curr_player == 3:
        player3_score += 1
        player3_box.append((start_x, start_y, width, height))
    elif curr_player == 4:
        player4_score += 1
        player4_box.append((start_x, start_y, width, height))


def game_play(no_of_dots):
    dots_arr = draw_dots()
    global hr_line_arr, vr_line_arr, run
    global curr_player
    global player1_box, player2_box, player3_box, player4_box
    line_arr = hr_line_arr + vr_line_arr
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(no_of_dots - 1):
                for j in range(no_of_dots):
                    cord = dots_arr[i][j]
                    next_cord = dots_arr[i + 1][j]

                    if ((cord[0] + 10 < event.pos[0] < next_cord[0] - 10
                         and cord[1] - dot_width < event.pos[1] < cord[1] + dot_width)
                            and [cord, next_cord] not in hr_line_arr):
                        change_player = True
                        hr_line_arr.append([cord, next_cord])
                        if sounds_state:
                            click.play()

                        if (j != (no_of_dots - 1)
                                and [dots_arr[i + 1][j], dots_arr[i + 1][j + 1]] in line_arr
                                and [dots_arr[i][j + 1], dots_arr[i + 1][j + 1]] in line_arr
                                and [dots_arr[i][j], dots_arr[i][j + 1]] in line_arr):
                            start_x = dots_arr[i][j][0]
                            start_y = dots_arr[i][j][1]
                            width = distance_between_dots
                            height = distance_between_dots

                            change_player = False
                            score(start_x, start_y, width, height)

                        if (j != 0
                                and [dots_arr[i][j - 1], dots_arr[i][j]] in line_arr
                                and [dots_arr[i][j - 1], dots_arr[i + 1][j - 1]] in line_arr
                                and [dots_arr[i + 1][j - 1], dots_arr[i + 1][j]] in line_arr):
                            start_x = dots_arr[i][j - 1][0]
                            start_y = dots_arr[i][j - 1][1]
                            width = distance_between_dots
                            height = distance_between_dots

                            change_player = False
                            score(start_x, start_y, width, height)

                        change(change_player)

            for i in range(no_of_dots):
                for j in range(no_of_dots - 1):
                    cord = dots_arr[i][j]
                    next_cord = dots_arr[i][j + 1]

                    if ((cord[1] + 10 < event.pos[1] < next_cord[1] - 10
                         and cord[0] - dot_width < event.pos[0] < cord[0] + dot_width)
                            and [cord, next_cord] not in vr_line_arr):
                        change_player = True
                        vr_line_arr.append([cord, next_cord])
                        if sounds_state:
                            click.play()

                        if (i != 0
                                and [dots_arr[i - 1][j], dots_arr[i][j]] in line_arr
                                and [dots_arr[i - 1][j], dots_arr[i - 1][j + 1]] in line_arr
                                and [dots_arr[i - 1][j + 1], dots_arr[i][j + 1]] in line_arr):
                            start_x = dots_arr[i - 1][j][0]
                            start_y = dots_arr[i - 1][j][1]
                            width = distance_between_dots
                            height = distance_between_dots

                            change_player = False
                            score(start_x, start_y, width, height)

                        if (i != (no_of_dots - 1)
                                and [dots_arr[i][j], dots_arr[i + 1][j]] in line_arr
                                and [dots_arr[i + 1][j], dots_arr[i + 1][j + 1]] in line_arr
                                and [dots_arr[i][j + 1], dots_arr[i + 1][j + 1]] in line_arr):
                            start_x = dots_arr[i][j][0]
                            start_y = dots_arr[i][j][1]
                            width = distance_between_dots
                            height = distance_between_dots

                            change_player = False
                            score(start_x, start_y, width, height)

                        change(change_player)
    return run


def shade_box(screen, color, boxes):
    for box in boxes:
        start_x, start_y, width, height = box
        pygame.draw.rect(screen, color,
                         pygame.Rect(start_x + edge_width / 2,
                                     start_y + edge_width / 2,
                                     width - edge_width + 2,
                                     height - edge_width + 2))


def score_turn():
    for player_num in player_list:
        if player_num == 1:
            WIN.blit(player1_score_bgr, (64, 582))

            player1_text = font72.render(str(player1_score), True, score_color)
            player1_text_rect = player1_text.get_rect()
            player1_text_rect.topleft = (131.5, 580)
            WIN.blit(player1_text, player1_text_rect)
        if player_num == 2:
            WIN.blit(player2_score_bgr, (194.9, 582))

            player2_text = font72.render(str(player2_score), True, score_color)
            player2_text_rect = player2_text.get_rect()
            player2_text_rect.topleft = (261.5, 580)
            WIN.blit(player2_text, player2_text_rect)
        if player_num == 3:
            WIN.blit(player3_score_bgr, (325.9, 582))

            player3_text = font72.render(str(player3_score), True, score_color)
            player3_text_rect = player3_text.get_rect()
            player3_text_rect.topleft = (391.5, 580)
            WIN.blit(player3_text, player3_text_rect)
        if player_num == 4:
            WIN.blit(player4_score_bgr, (456.8, 582))

            player4_text = font72.render(str(player4_score), True, score_color)
            player4_text_rect = player4_text.get_rect()
            player4_text_rect.topleft = (521.5, 580)
            WIN.blit(player4_text, player4_text_rect)

    if curr_player == 1:
        WIN.blit(player1_turn, (236.5, 0))
    elif curr_player == 2:
        WIN.blit(player2_turn, (236.5, 0))
    elif curr_player == 3:
        WIN.blit(player3_turn, (236.5, 0))
    elif curr_player == 4:
        WIN.blit(player4_turn, (236.5, 0))


def change(change_player):
    global number_of_player, curr_player
    if number_of_player == 2:
        if curr_player == 1 and change_player:
            curr_player = 2
        elif change_player:
            curr_player = 1

    if number_of_player == 3:
        if curr_player == 1 and change_player:
            curr_player = 2
        elif curr_player == 2 and change_player:
            curr_player = 3
        elif curr_player == 3 and change_player:
            curr_player = 1

    if number_of_player == 4:
        if curr_player == 1 and change_player:
            curr_player = 2
        elif curr_player == 2 and change_player:
            curr_player = 3
        elif curr_player == 3 and change_player:
            curr_player = 4
        elif curr_player == 4 and change_player:
            curr_player = 1


def options():
    global number_of_player, player_list
    global number_of_dots
    if number_of_player == 2:
        player_decrease_button.draw(WIN)
        if player_increase_button.draw(WIN):
            number_of_player += 1
            player_list.append(3)
    elif number_of_player == 3:
        if player_decrease_button.draw(WIN):
            number_of_player -= 1
            player_list.remove(3)
        if player_increase_button.draw(WIN):
            number_of_player += 1
            player_list.append(4)
    elif number_of_player == 4:
        if player_decrease_button.draw(WIN):
            number_of_player -= 1
            player_list.remove(4)
        player_increase_button.draw(WIN)

    num_player_text = font72.render(str(number_of_player), True, (0, 151, 178))
    num_player_rect = num_player_text.get_rect()
    num_player_rect.topleft = (395, 231)
    WIN.blit(num_player_text, num_player_rect)

    if number_of_dots == 3:
        size_decrease_button.draw(WIN)
        if size_increase_button.draw(WIN):
            number_of_dots += 2
    elif 3 < number_of_dots < 13:
        if size_decrease_button.draw(WIN):
            number_of_dots -= 2
        if size_increase_button.draw(WIN):
            number_of_dots += 2
    else:
        if size_decrease_button.draw(WIN):
            number_of_dots -= 2
        size_increase_button.draw(WIN)

    num_dots_text = font72.render(str(number_of_dots) + "  " + str(number_of_dots), True, (0, 151, 178))
    num_dots_rect = num_dots_text.get_rect()
    num_dots_rect.midtop = (403, 353)
    WIN.blit(num_dots_text, num_dots_rect)
    WIN.blit(X, (387, 361))


def play():
    global game_state
    global number_of_dots
    shade_box(WIN, player1_color_light, player1_box)
    shade_box(WIN, player2_color_light, player2_box)
    shade_box(WIN, player3_color_light, player3_box)
    shade_box(WIN, player4_color_light, player4_box)
    draw_edge()
    draw_dots()
    hover_edge(number_of_dots)
    game_play(number_of_dots)
    score_turn()
    line_arr = hr_line_arr + vr_line_arr
    if len(line_arr) == (2 * number_of_dots * (number_of_dots - 1)):
        game_state = 'finish'

def show_winner():
    all_score = (player1_score, player2_score, player3_score, player4_score)
    highest_score = max(all_score)
    if player1_score == highest_score and 1 not in winner:
        winner.append(1)
    if player2_score == highest_score and 2 not in winner:
        winner.append(2)
    if player3_score == highest_score and 3 not in winner:
        winner.append(3)
    if player4_score == highest_score and 4 not in winner:
        winner.append(4)

    if len(winner) == 1:
        if winner[0] == 1:
            WIN.blit(PLAYER1, (265, 191.7))
        if winner[0] == 2:
            WIN.blit(PLAYER2, (265, 191.7))
        if winner[0] == 3:
            WIN.blit(PLAYER3, (265, 191.7))
        if winner[0] == 4:
            WIN.blit(PLAYER4, (265, 191.7))
    elif len(winner) == 2:
        for idx, i in enumerate(winner):
            win = "Assets/p" + str(i) + ".png"
            winner_img = pygame.image.load(win)
            x_cord = 170 + 180 * idx
            WIN.blit(winner_img, (x_cord, 191.7))

    elif len(winner) == 3:
        for idx, i in enumerate(winner):
            win = "Assets/p" + str(i) + ".png"
            winner_img = pygame.image.load(win)
            x_cord = 125 + 135 * idx
            WIN.blit(winner_img, (x_cord, 191.7))

def reset():
    global hr_line_arr, vr_line_arr, curr_player
    global player1_box, player2_box, player3_box, player4_box, winner
    global player1_score, player2_score, player3_score, player4_score
    hr_line_arr = []
    vr_line_arr = []
    curr_player = 1

    winner = []

    player1_box = []
    player2_box = []
    player3_box = []
    player4_box = []

    player1_score = 0
    player2_score = 0
    player3_score = 0
    player4_score = 0

def menu():
    global game_state, music_state, sounds_state

    WIN.blit(BG, (0, 0))
    if game_state == 'main':
        WIN.blit(MENU, (0, 0))
        if play_button.draw(WIN):
            game_state = 'options'
        if howtoplay_button.draw(WIN):
            game_state = 'how_to_play'
        if settings_button.draw(WIN):
            game_state = 'settings'

    elif game_state == 'options':
        WIN.blit(OPTIONS, (0, 0))
        options()
        if start_button.draw(WIN):
            game_state = 'play'
        if back_button.draw(WIN):
            game_state = 'main'

    elif game_state == 'play':
        WIN.blit(PLAY_BACKGROUND, (0, 0))
        play()
        if back_button.draw(WIN):
            game_state = 'options'
            reset()

    elif game_state == 'how_to_play':
        WIN.blit(HOW_TO_PLAY, (0, 0))
        if back_button.draw(WIN):
            game_state = 'main'

    elif game_state == 'settings':
        WIN.blit(SETTINGS, (0, 0))
        if music_state:
            if music_on_button.draw(WIN):
                music_state = False
                pygame.mixer.music.stop()
        else:
            if music_off_button.draw(WIN):
                music_state = True
                pygame.mixer.music.play(-1)

        if sounds_state:
            if sounds_on_button.draw(WIN):
                sounds_state = False
        else:
            if sounds_off_button.draw(WIN):
                sounds_state = True

        if back_button.draw(WIN):
            game_state = 'main'

    elif game_state == 'finish':
        WIN.blit(RESULT_BACKGROUND, (0, 0))
        show_winner()
        if play_again_button.draw(WIN):
            game_state = 'play'
            reset()
        if menu_button.draw(WIN):
            game_state = 'main'
            reset()

    pygame.display.update()


def main():
    global run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        menu()

    pygame.quit()


if __name__ == "__main__":
    main()
