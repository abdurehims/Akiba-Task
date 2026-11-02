class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        losses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)

            losses[loser] = losses.get(loser, 0) + 1

        no_losses = []
        one_loss = []

        for player in players:
            if losses.get(player, 0) == 0:
                no_losses.append(player)

            elif losses[player] == 1:
                one_loss.append(player)

        return [sorted(no_losses), sorted(one_loss)]
        
        