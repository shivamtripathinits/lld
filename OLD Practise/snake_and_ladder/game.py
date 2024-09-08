from lld.snake_and_ladder.board import Board
from lld.snake_and_ladder.dice import Dice
from lld.snake_and_ladder.player import Player


class Game:
    def __init__(self, no_of_players=2,board_size=10, count_snake=5, count_ladder=3):
        self.count_snake = count_snake
        self.count_ladder = count_ladder
        self.board_size = board_size
        self.dice = None
        self.board = None
        self.winner = None
        self.no_of_players = no_of_players
        self.players = []
        self.initialise_game()
        self.snakes = []
        self.ladders = []

    def initialise_game(self):
        self.board = Board(size=self.board_size, count_snake=self.count_snake, count_ladder=self.count_ladder)
        self.dice = Dice(dice_count=1)
        for pc in range(self.no_of_players):
            input_statement = "enter player {} name ".format(pc+1)
            pname = input(input_statement)
            player = Player(input_id=pname, current_position=0)
            self.players.append(player)

    def print_all_constants(self):
        print("Total Players are : {}".format(len(self.players)))
        pcount = 1
        for player in self.players:
            print("Player {} is {}".format(pcount, player.id))
            pcount += 1
        print("Total Snakes are : {}".format(self.count_snake))
        print("Total Ladders are : {}".format(self.count_ladder))
        all_cells = self.board.cells
        curr_cell = 0
        print("Board size = {}".format(self.board_size))
        for i in range(self.board_size):
            for j in range(self.board_size):
                if all_cells[i][j] and all_cells[i][j].jump and all_cells[i][j].jump.start == curr_cell:
                    if all_cells[i][j].jump.type == "snake_bite":
                        self.snakes.append([all_cells[i][j].jump.start, all_cells[i][j].jump.end])
                        # print("snake at {} to {}".format(all_cells[i][j].jump.start,
                        #                                  all_cells[i][j].jump.end))
                    else:
                        self.ladders.append([all_cells[i][j].jump.start, all_cells[i][j].jump.end])
                        # print("ladder at {} to {}".format(all_cells[i][j].jump.start,
                        #                                   all_cells[i][j].jump.end))
                curr_cell += 1
        print ("Snakes are at {}".format(self.snakes))
        print("Ladders are at {}".format(self.ladders))
    def start_game(self):
        while self.winner is None:
            next_player = self.get_next_turn_player()
            input("{} press enter to roll ".format(next_player.id))
            dice_number = self.dice.roll_dice()
            if next_player.current_position == 0 and dice_number != 6:
                print("{} Unlucky Try again for 6 to open !".format(dice_number))
            else:
                print("Score {} {} Moving from {} to {}".format(dice_number, next_player.id,
                                                                next_player.current_position,
                                                                next_player.current_position + dice_number))
                next_player.current_position = next_player.current_position + dice_number
                if next_player.current_position >= 100:
                    # print("inside")
                    self.winner = next_player
                    break
                current_cell = self.board.get_cell(next_player.current_position)

                if current_cell.jump and current_cell.jump.start == next_player.current_position:
                    print("{} is at given position".format(current_cell.jump.type))
                    print("Score {} {} Moving from {} to {}".format(dice_number,next_player.id,
                                                                    next_player.current_position,
                                                           current_cell.jump.end))
                    next_player.current_position = current_cell.jump.end
                if next_player.current_position >= 100:
                    # print("inside")
                    self.winner = next_player
                    break
        print(self.winner.id, " is winner")

    def get_next_turn_player(self):
        next_player = self.players[0]
        del self.players[0]
        self.players.append(next_player)
        return next_player


