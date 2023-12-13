import pygame
import sys


# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("There Is No Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define font
font = pygame.font.Font(None, 36)

def level_1():
    window.fill(BLACK)
    text = font.render("Welcome to Level 1!", True, WHITE)
    print("Level 1 Question: Press a button to proceed.")
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    text = font.render("Click the button to proceed.", True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def level_2():
    window.fill(BLACK)
    text = font.render("Welcome to Level 2!", True, WHITE)
    print("Level 2 Question: What is the password?")
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    text = font.render("Enter the password to proceed:", True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()

    password = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if password == "password123":
                        return
                    else:
                        password = ""
                elif event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (WIDTH/2 - 100, HEIGHT/2 - 20, 200, 40))
        text_surface = font.render(password, True, BLACK)
        window.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
        pygame.display.flip()

def level_3():
    window.fill(BLACK)
    text = font.render("Welcome to Level 3!", True, WHITE)
    print("Level 3 Question: What is 2 + 2?")
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    text = font.render("What is 2 + 2?", True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()

    answer = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if answer == "4":
                        return
                    else:
                        answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                else:
                    answer += event.unicode

        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (WIDTH/2 - 100, HEIGHT/2 - 20, 200, 40))
        text_surface = font.render(answer, True, BLACK)
        window.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
        pygame.display.flip()


def level_4():
    # Level 4 logic here
    window.fill(BLACK)
    text = font.render("Welcome to Level 4!", True, WHITE)
    print("Level 4 Question: What is the capital of France?")
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    text = font.render("What is the capital of France?", True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()

    answer = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if answer.lower() == "paris":
                        return
                    else:
                        answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                else:
                    answer += event.unicode

            window.fill(BLACK)
            pygame.draw.rect(window, WHITE, (WIDTH/2 - 100, HEIGHT/2 - 20, 200, 40))
            text_surface = font.render(answer, True, BLACK)
            window.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
            pygame.display.flip()
def level_5():
    # Level 5 logic here
    window.fill(BLACK)
    text = font.render("Welcome to Level 5!", True, WHITE)
    print("Level 5 Question: What is the capital of Germany?")
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    text = font.render("What is the capital of Germany?", True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.flip()

    answer = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if answer.lower() == "berlin":
                        return
                    else:
                        answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                else:
                    answer += event.unicode

            window.fill(BLACK)
            pygame.draw.rect(window, WHITE, (WIDTH/2 - 100, HEIGHT/2 - 20, 200, 40))
            text_surface = font.render(answer, True, BLACK)
            window.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
            pygame.display.flip()

# def level_5():
#     # Level 5 logic here
#     pass

def level_6():
    # Level 6 logic here
    pass

def level_7():
    # Level 7 logic here
    pass

def level_8():
    # Level 8 logic here
    pass

def level_9():
    # Level 9 logic here
    pass

def level_10():
    # Level 10 logic here
    pass

def level_11():
    # Level 11 logic here
    pass

def level_12():
    # Level 12 logic here
    pass

def level_13():
    # Level 13 logic here
    pass

def level_14():
    # Level 14 logic here
    pass

def level_15():
    # Level 15 logic here
    pass

def level_16():
    # Level 16 logic here
    pass

def level_17():
    # Level 17 logic here
    pass

def level_18():
    # Level 18 logic here
    pass

def level_19():
    # Level 19 logic here
    pass

def level_20():
    # Level 20 logic here
    pass

def level_21():
    # Level 21 logic here
    pass

def level_22():
    # Level 22 logic here
    pass

def level_23():
    # Level 23 logic here
    pass

def level_24():
    # Level 24 logic here
    pass

def level_25():
    # Level 25 logic here
    pass

def level_26():
    # Level 26 logic here
    pass

def level_27():
    # Level 27 logic here
    pass

def level_28():
    # Level 28 logic here
    pass

def level_29():
    # Level 29 logic here
    pass

def level_30():
    # Level 30 logic here
    pass

# Main game loop
def play_game():
    level_1()
    level_2()
    level_3()
    level_4()
    level_5()
    level_6()
    level_7()
    level_8()
    level_9()
    level_10()
    level_11()
    level_12()
    level_13()
    level_14()
    level_15()
    level_16()
    level_17()
    level_18()
    level_19()
    level_20()
    level_21()
    level_22()
    level_23()
    level_24()
    level_25()
    level_26()
    level_27()
    level_28()
    level_29()
    level_30()

# Run the game loop
play_game()



print("Congratulations! You have completed the game! Adding more soon!")
