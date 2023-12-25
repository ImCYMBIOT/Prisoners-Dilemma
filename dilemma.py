import random

def play_round(p1_choice, p2_choice):
    payoff_matrix = {
        ('C', 'C'): (3, 3),
        ('C', 'D'): (0, 5),
        ('D', 'C'): (5, 0),
        ('D', 'D'): (1, 1),
    }
    return payoff_matrix[(p1_choice, p2_choice)]

class Player:
    def __init__(self, name, strategy_function):
        self.name = name
        self.strategy_function = strategy_function
        self.history = []

    def play(self, opponent_last_move):
        move = self.strategy_function(self.history, opponent_last_move)
        self.history.append(move)
        return move

def random_strategy(player_history, opponent_last_move):
    return random.choice(['C', 'D'])

#  strategies
def tit_for_tat(player_history, opponent_last_move):
    if not player_history:
        return 'C'
    else:
        return opponent_last_move

def always_defect(player_history, opponent_last_move):
    return 'D'

def main():
    rounds = 50

    # Instantiate players with their strategies
    player1 = Player("Player 1", tit_for_tat)
    player2 = Player("Player 2", always_defect)

    for round_num in range(1, rounds + 1):
        # Players make their moves
        p1_move = player1.play(player2.history[-1] if player2.history else None)
        p2_move = player2.play(player1.history[-1] if player1.history else None)

        # Display the choices made in the last round
        if round_num > 1:
            print("Last round choices: Player 1 - {}, Player 2 - {}".format(player1.history[-1], player2.history[-1]))

        # Play the round
        round_payoffs = play_round(p1_move, p2_move)
        player1.history.append(p1_move)
        player2.history.append(p2_move)

        # Display round results
        print("Round {}: Player 1 - {}, Player 2 - {}".format(round_num, p1_move, p2_move))
        print("Scores - Player 1: {}, Player 2: {}\n".format(player1.history.count('C'), player2.history.count('C')))

    # Display final scores
    print("Game Over! Final Scores - Player 1: {}, Player 2: {}".format(player1.history.count('C'), player2.history.count('C')))

if __name__ == "__main__":
    main()

