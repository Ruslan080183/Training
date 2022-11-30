class FootballClub:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def __str__(self):
        return F"The Football Club {self.name} is located in {self.country}"
    def __repr__(self):
        return repr(self.name)
class FootballClubBudget(FootballClub):
    def __init__(self, name, country, budget):
        FootballClub.__init__(self, name, country)
        self.budget = budget
    def size_budget(self):
        if self.budget >= 100000000:
         return print(F"The Football Club {self.name} has a high budget")
    def __add__(self, other):
        return self.budget + other.budget
    def __str__(self):
        return F"The budget of the Football Club  {self.name} from {self.country} is {self.budget}$"
class NationalChampionship(FootballClub):
    def __init__(self, name, country, season, place_championship):
        FootballClub.__init__(self, name, country)
        self.season = season
        self.place_championship = place_championship
    def __ge__(self, other):
        return self.place_championship >= other.place_championship
    def __str__(self):
        return F"The Football Club  {self.name} in the national championship of {self.country} in the {self.season} season takes {self.place_championship} place"
class SeasonResults:
    def __init__(self, games, victories, defeats, draws):
        self.games = games
        self.victories = victories
        self.defeats = defeats
        self.draws = draws
    def __ge__(self, other):
        return self.victories >= other.victories
    def __str__(self):
        return F"Number games - {self.games:victories} - {self.victories}, defeats - {self.defeats} , draws = {self.draws} "
class RatingClubEurope(NationalChampionship,SeasonResults):
    def __init__(self, name, country, season, place_championship, games, victories, defeats, draws, rating_place):
        NationalChampionship.__init__(self, name, country, season, place_championship)
        SeasonResults.__init__(self, games, victories, defeats, draws)
        self.rating_place = rating_place
    def __ge__(self, other):
        return self.rating_place >= other.rating_place
    def __str__(self):
        return F"In the UEFA ranking the Football Club  {self.name} from {self.country} is in {self.rating_place} place"
class Transfers:
        def __init__(self, buying_football_players, sale_football_players, transaction_amount):
            self.buying_football_players = buying_football_players
            self.sale_football_players = sale_football_players
            self.transaction_amount = transaction_amount
        def __add__(self, other):
            return self.transaction_amount + other.transaction_amount
        def __str__(self):
            return F"The transfer{self.buying_football_players or self.sale_football_players} was {self.transaction_amount}$"
class PlayerTransitions(FootballClubBudget, Transfers):
    def __init__(self, name, country, budget, buying_football_players, sale_football_players, transaction_amount, footballer):
        FootballClubBudget.__init__(self, name, country, budget)
        Transfers.__init__(self, buying_football_players, sale_football_players, transaction_amount)
        self.footballer = footballer
    def __repr__(self):
        return repr(self.footballer)
    def __str__(self):
        return F"The transfer of {self.footballer} to the football club {self.name} was paid for {self.transaction_amount}$"