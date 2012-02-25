'''
Created on 2011-11-20

@author: Gooble
'''
import main.game.gameplay as gameplay
import main.view.slotting
import main.view.menufactory as menufactory
import main.view.boardcanvasfactory as boardcanvasfactory
from main.ai import minimaxai
import pygame
import threading

class AIThread(threading.Thread):
    def __init__(self, ai, game):
        threading.Thread.__init__(self)
        self.ai=ai
        self.game=game
        self.finished=False
    
    def run(self):
        self.ai.make_move(self.game)
        self.finished=True

class GamePanel(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self, canvas_factory=boardcanvasfactory.BoardCanvasFactory(), menu_factory=menufactory.MenuFactory(), ai=None):
        self.game = gameplay.GamePlay()
        
        self.screen = pygame.display.set_mode([self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT])
        pygame.display.set_caption("Gooble Checkers")
        #menu_factory.make_menu(self)
        
        self.slotting = main.view.slotting.Slotting(self.game)
        self.canvas = canvas_factory.make_canvas(self.screen, self.game.board, self.slotting)
        self.ai = ai
        self.aithread = None
        
    def handle_events(self, game):
        self.canvas.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.draw_slotting(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                self.draw_release(event.pos)
            if event.type == pygame.MOUSEMOTION:
                self.canvas.draw(event.pos)
                
        return False
        
    def draw_slotting(self, event):
        if not self.game.current_turn.is_computers_turn(self.ai):
            self.slotting.select_piece(event)
            self.canvas.draw(event)
        
    def draw_release(self, event):
        if not self.game.current_turn.is_computers_turn(self.ai):
            self.slotting.release_piece(event)
            self.canvas.draw(event)
            self.check_and_use_ai()
            if (self.game.is_game_over()):
                self.new_game()
            
    def check_and_use_ai(self):
        if self.ai is not None and self.game.current_turn.is_computers_turn(self.ai) and (self.aithread is None or self.aithread.finished):
            self.canvas.draw()
            if self.aithread is not None:
                self.aithread.join(10)
            self.aithread = AIThread(self.ai, self.game)
            self.aithread.start()
            self.canvas.draw()
        
    def start(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)
        done = False
        while not done:
            self.clock.tick(30)
            self.screen.fill([0,0,0])
            done = self.handle_events(self.game)
            self.check_and_use_ai()
            
            if self.game.current_turn.is_computers_turn(self.ai):
                text = font.render("The computer is thinking...", False, [150,150,150], [255,255,255])
                self.screen.blit(text, [self.DEFAULT_WIDTH/4, self.DEFAULT_HEIGHT/2 - 25])
            pygame.display.flip()

        
    def new_game(self):
        self.game = gameplay.GamePlay()
        self.slotting = main.view.slotting.Slotting(self.game)
        self.canvas.board = self.game.board
        self.canvas.slotting = self.slotting
        self.canvas.draw()
        
if __name__ == '__main__':
    GamePanel(ai=minimaxai.MinimaxAI(3)).start()