from app import db

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    nick = db.Column(db.String(20))
    team = db.Column(db.String(20))
    role = db.Column(db.String(20))
    kills = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    matches = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    kda = db.Column(db.Float(asdecimal=True))
    winrate = db.Column(db.Float(asdecimal=True))

    def __init__(self, name, nick, team, role, kills, assists, deaths, matches, wins):
        self.name = name
        self.nick = nick
        self.team = team
        self.role = role
        self.kills = kills
        self.assists = assists
        self.deaths = deaths
        self.matches = matches
        self.wins = wins
        self.calc()

    def calc(self):
        if(self.deaths==0):
            self.kda = float(self.kills+self.assists)
        else:
            temp = float(self.kills+self.assists)
            self.kda = float(temp/self.deaths)
        self.winrate = (self.wins/self.matches)*100

    def __repr__(self):
        return "Info {0}".format(self.id)