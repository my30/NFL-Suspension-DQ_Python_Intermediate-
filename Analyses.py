# 2/6
import csv

file = open('nfl-suspensions-data.csv', 'r')
nfl_suspensions = list(csv.reader(file))
header = nfl_suspensions[0]
nfl_suspensions = nfl_suspensions[1:]
years = {}
for record in nfl_suspensions:
    if record[5] in years:
        years[record[5]] += 1
    else:
        years[record[5]] = 1
print(years, '\n')

# 3/6
# teams = []
teams = (record[1] for record in nfl_suspensions)
unique_teams = set(teams)
games = (record[2] for record in nfl_suspensions)
unique_games = set(games)
print(unique_teams, '\n', unique_games, '\n')


# 4
class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]


third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension, '\n')


# 5
class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]

    def get_year(self, row):
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
        return self.year


missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year(22)
print(twenty_third_year, '\n')
