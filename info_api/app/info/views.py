import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from app.info.models import Info
from app import api, db

info = Blueprint("info", __name__)

parser = reqparse.RequestParser()

parser.add_argument("name", type=str)
parser.add_argument("nick", type=str)
parser.add_argument("team", type=str)
parser.add_argument("role", type=str)
parser.add_argument("kills", type=int)
parser.add_argument("assists", type=int)
parser.add_argument("deaths", type=int)
parser.add_argument("matches", type=int)
parser.add_argument("wins", type=int)
parser.add_argument("kda", type=float)
parser.add_argument("winrate", type=float)

@info.route("/")
@info.route("/home")
def home():
    return "lista de Jogadores"

class InfoAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            infos = Info.query.paginate(page, 10).items
        else:
            infos = [Info.query.get(id)]
        if not infos:
            abort(404)
        res = {}
        for inf in infos:
            res[inf.id] = {
                "name": inf.name, 
                "nick": inf.nick,
                "team": inf.team,
                "role": inf.role,
                "kills": inf.kills,
                "assists": inf.assists,
                "deaths": inf.deaths,
                "matches": inf.matches,
                "wins": inf.wins,
                "kda": str(inf.kda),
                "winrate": str(inf.winrate)
                }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args["name"]
        nick = args["nick"]
        team = args["team"]
        role = args["role"]
        kills = args["kills"]
        assists = args["assists"]
        deaths = args["deaths"]
        matches = args["matches"]
        wins = args["wins"]

        inf = Info(name, nick, team, role, kills, assists, deaths, matches, wins)
        db.session.add(inf)
        db.session.commit()
        res = {}
        res[inf.id] = {
                "name": inf.name, 
                "nick": inf.nick,
                "team": inf.team,
                "role": inf.role,
                "kills": inf.kills,
                "assists": inf.assists,
                "deaths": inf.deaths,
                "matches": inf.matches,
                "wins": inf.wins,
                "kda": str(inf.kda),
                "winrate": str(inf.winrate)
                }
        return json.dumps(res)

    def delete (self, id):
        inf = Info.query.get(id)
        db.session.delete(inf)
        db.session.commit()
        res = {'id':id}
        return json.dumps(res)

    def put(self, id):
        inf = Info.query.get(id)
        args = parser.parse_args()
        name = args["name"]
        nick = args["nick"]
        team = args["team"]
        role = args["role"]
        kills = args["kills"]
        assists = args["assists"]
        deaths = args["deaths"]
        matches = args["matches"]
        wins = args["wins"]
        
        inf.name=name
        inf.nick=nick
        inf.team = team
        inf.role = role
        inf.kills = kills
        inf.assists = assists
        inf.deaths = deaths
        inf.matches = matches
        inf.wins = wins
        inf.calc()

        db.session.commit()
        res = {}
        res[inf.id] = {
                "name": inf.name, 
                "nick": inf.nick,
                "team": inf.team,
                "role": inf.role,
                "kills": inf.kills,
                "assists": inf.assists,
                "deaths": inf.deaths,
                "matches": inf.matches,
                "wins": inf.wins,
                "kda": str(inf.kda),
                "winrate": str(inf.winrate)
                }
        return json.dumps(res)


api.add_resource(
    InfoAPI,
    '/api/info',
    '/api/info/<int:id>',
    '/api/info/<int:id>/<int:page>'
)