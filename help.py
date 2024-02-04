from winner import winner
from tabulate import tabulate


class Table:
    def __init__(self, moves):
        self.data = []
        self.data.append(["v PC\\User >"] + moves)

        for i in range(len(moves)):
            row = [moves[i]] + [winner(moves, i, j) for j in range(len(moves))]
            self.data.append(row)

    def print_ascii_table(self):
        table = tabulate(self.data, tablefmt='grid')
        print(table)
