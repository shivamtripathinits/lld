from lld.snake_and_ladder.board import Board
from lld.snake_and_ladder.dice import Dice
from lld.snake_and_ladder.player import Player


class Game:
    def __init__(self, no_of_players=2):
        self.dice = None
        self.board = None
        self.winner = None
        self.no_of_players = no_of_players
        self.players = []
        self.initialise_game()

    def initialise_game(self):
        self.board = Board(size=10, count_snake=5, count_ladder=3)
        self.dice = Dice(dice_count=1)
        for pc in range(self.no_of_players):
            input_statement = "enter player {} name ".format(pc+1)
            pname = input(input_statement)
            player = Player(input_id=pname, current_position=0)
            self.players.append(player)

    def print_all_players(self):
        for player in self.players:
            print(player.id)

    def start_game(self):
        while self.winner is None:
            next_player = self.get_next_turn_player()
            dice_number = self.dice.roll_dice()
            if next_player.current_position == 0 and dice_number != 6:
                print("{} Unlucky Try again for 6 to open !".format(dice_number))
            else:
                print("{} Moving from {} to {}".format(dice_number, next_player.current_position,
                                                       next_player.current_position + dice_number))
                next_player.current_position = next_player.current_position + dice_number
                current_cell = self.board.get_cell(next_player.current_position)



    def get_next_turn_player(self):
        next_player = self.players[0]
        self.players.remove(0)
        self.players.append(next_player)


g = Game(no_of_players=2)
g.print_all_players()
