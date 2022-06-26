import pygame, sys, time, random, math
from settings import *
from levels import Level


class Game:
	
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		pygame.display.set_caption("Kingdom Fall")
		self.state = 1
		self.level = Level()
	
	def run(self):
		self.welcome_screen()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					self.state += 1
			self.screen.fill(BLACK)
			self.draw_win()
			pygame.display.update()
			self.clock.tick(FPS)	

	def first_slide(self):
		story_text = STORY_FONT.render("Once upon a time, the world of Lamba was divine", 1, WHITE)
		story_text2 = STORY_FONT.render("and pure, but the people took it for granted.", 1, WHITE)
		story_text3 = STORY_FONT.render("They polluted the planet to utter shambles.", 1, WHITE)
		story_text4 = STORY_FONT.render("Click to Continue", 1, RED)
		self.screen.blit(story_text, (575, 100))
		self.screen.blit(story_text2, (575, 150))
		self.screen.blit(story_text3, (575, 200))
		self.screen.blit(story_text4, (800, 300))

	def second_slide(self):
		story_text = STORY_FONT.render("Upset, the dark wizard gave life to the trash.", 1, WHITE)
		story_text2 = STORY_FONT.render("Such, turning vengeful after being neglected by ", 1, WHITE)
		story_text3 = STORY_FONT.render("the people for so long, terrorized the kingdom.", 1, WHITE)
		story_text4 = STORY_FONT.render("Click to Continue", 1, RED)
		self.screen.blit(story_text, (575, 100))
		self.screen.blit(story_text2, (575, 150))
		self.screen.blit(story_text3, (575, 200))
		self.screen.blit(story_text4, (800, 300))

	def third_slide(self):
		story_text = STORY_FONT.render("One man has taken the responsibility of", 1, WHITE)
		story_text2 = STORY_FONT.render("restoring the city to its former glory.", 1, WHITE)
		story_text3 = STORY_FONT.render("Click to Play", 1, RED)
		self.screen.blit(story_text, (575, 100))
		self.screen.blit(story_text2, (575, 150))
		self.screen.blit(story_text3, (800, 300))

	
	def draw_win(self):
		if self.state == 1:
			self.first_slide()
		elif self.state == 2:
			self.second_slide()
		elif self.state == 3:
			self.third_slide()
		else:
			self.level.run()
			
			

	def welcome_screen(self):
		pass
		

	
	

if __name__ == "__main__":
	game = Game()
	game.run()



