from lld.snake_and_ladder.game import Game


class Main:
    no_of_players = int(input("Enter No of Players "))
    board_size = int(input("Enter Board size n in format (n*n) "))
    snakes_count = int(input("Enter No of Snakes "))
    ladders_count = int(input("Enter No of Ladders "))
    game = Game(no_of_players=no_of_players, board_size=board_size,
                count_snake=snakes_count, count_ladder=ladders_count)
    game.print_all_constants()
    game.start_game()
