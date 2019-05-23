from game import Game
from snake import Snake

game = Game(20)

snake = Snake(game)
game.set_snake(snake)

game.add_apple()

game.show_game()

while True:
	game.update_game()
	game.show_game()

