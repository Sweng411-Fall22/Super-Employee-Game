import sys
import self as self

import button as button
import pygame

pygame.init()


def main_menu(button: object = None) -> object:  # main menu screen
    pygame.display.set_caption("MENU")

    def get_font(param):
        pass

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        START_BUTTON = button.Button(self.SCREEN_WIDTH // 2 - 130, self.SCREEN_HEIGHT // 2 - 150, self.start_img, 1),


        SETTINGS_BUTTON = button.Button(self.SCREEN_WIDTH // 2 - 170, self.SCREEN_HEIGHT // 2 - 50, self.settings_img,
                                        1),

        EXIT_BUTTON = button.Button(self.SCREEN_WIDTH // 2 - 110, self.SCREEN_HEIGHT // 2 + 50, self.exit_img, 1),

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, SETTINGS_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SCREEN.checkForInput(MENU_MOUSE_POS):
                        start()
                        if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            settings()
                            if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                                pygame.quit()
                                sys.exit()

            pygame.display.update()

            main_menu()
