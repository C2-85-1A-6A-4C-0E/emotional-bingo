import emotional_loader
import pygame, pygame.locals
pygame.init()
pygame.font.init()
black, white = (0,0,0), (255,255,255)
FRAMERATE = 20

def print_card(card, shape=(5,5)):
	length = max([len(i) for i in card]) + 2
	assert len(card) == shape[0] * shape[1]
	for row in range(shape[0]):
		for col in range(shape[1]):
			pos = col + (row*shape[1])
			word = card[pos]
			while len(word) < length:
				word += ' '
			print(word, end='\t')
		print()

def draw_card(card, savename="bingo.png", id=None, freespace=False):
	SIZE = WIDTH, HEIGHT = 550, 650
	picture = pygame.display.set_mode(SIZE)
	font = pygame.font.SysFont('Times New Roman', 16)
	small_font = pygame.font.SysFont('Times New Roman', 12)
	title = pygame.font.SysFont('Ariel', 100)
	picture.fill(white)
	text = title.render("BINGO", True, black)
	text_rect = text.get_rect(center=(WIDTH//2, 75))
	picture.blit(text, text_rect)

	if freespace:
		middle = len(card) // 2
		card[middle] = "FREE SPACE"

	lines = [ (25,25), (WIDTH-25, 25), (WIDTH-25, 125), (25, 125), (25,25), (25, HEIGHT-25), (125, HEIGHT-25), (125,125), (225, 125), (225, HEIGHT-25), (325, HEIGHT-25), (325, 125),
			  (425, 125), (425, HEIGHT-25), (525, HEIGHT-25), (525, 125), (525, 225), (25, 225), (25, 325), (525, 325), (525, 425), (25, 425), (25, 525), (525, 525), (525, 625), (25, 625)]
	pygame.draw.lines(picture, black, False, lines)

	centers = [(75, 175), (175, 175), (275, 175), (375, 175), (475, 175),
			   (75, 275), (175, 275), (275, 275), (375, 275), (475, 275),
			   (75, 375), (175, 375), (275, 375), (375, 375), (475, 375),
			   (75, 475), (175, 475), (275, 475), (375, 475), (475, 475),
			   (75, 575), (175, 575), (275, 575), (375, 575), (475, 575), ]

	for label, point in zip(card, centers):
		text = font.render(label, True, black)
		if text.get_rect().width > 100:
			text = small_font.render(label, True, black)
		text_rect = text.get_rect(center=point)
		picture.blit(text, text_rect)

	if id is not None:
		text = small_font.render(f"Card {id}", True, black)
		text_rect = text.get_rect()
		text_rect.x = 30
		text_rect.y = 630
		picture.blit(text, text_rect)

	pygame.display.flip()
	pygame.image.save(picture, savename)

if __name__ == "__main__":
	card = emotional_loader.make_card(25)
	print_card(card)
	from time import sleep
	draw_card(card)
	sleep(2)
	for i, card in enumerate(emotional_loader.make_cards(50)):
		draw_card(card, f"Cards\\bingo_{i+1}.png", i+1, freespace=True)
		sleep(1/FRAMERATE)

	for card in emotional_loader.continous_cards():
		draw_card(card, freespace=True)
		sleep(1/FRAMERATE)

		for event in pygame.event.get():
			if event.type is pygame.locals.QUIT:
				pygame.quit()
				exit()
			if event.type is pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					FRAMERATE *= 1.25
				if event.button == 5:
					FRAMERATE *= 0.8
