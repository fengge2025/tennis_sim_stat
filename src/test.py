from player import Player, Match

if __name__ == "__main__":
    player1 = Player(name="nimish", continue_chance=99)
    player2 = Player(name="freddy", continue_chance=99)
    match = Match(player1=player1, player2=player2)

    winner = match._simulate_match()

    num_loops = 100
    stat = [0, 0]

    for _ in range(num_loops):
        winner_idx = match._simulate_match()
        stat[winner_idx] += 1

    print(stat)
