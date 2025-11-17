from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
from cs50 import SQL
import time




app = Flask(__name__)

db = SQL("sqlite:///images.db")

API_KEY = "9142f7cc03e5414f9c2ec9df7fee5aa8"
headers = {
    "X-Auth-Token": API_KEY
}
base_url = "https://api.football-data.org/v4/competitions/"

today = datetime.today().date()
next_month = today + timedelta(days=30)

CACHE = {}
CACHE_TIME = {}
CACHE_TTL = 600   # seconds (1 minute)

def show_upcoming_matches(prefix, time_limit):
    now = time.time()

    # 1. If cached AND not expired → return cached version
    if prefix in CACHE and (now - CACHE_TIME[prefix]) < CACHE_TTL:
        # print("CACHE HIT for:", prefix)
        data = CACHE[prefix]
    else:
        # print("CACHE MISS for:", prefix)
        urlmatches = base_url + prefix + "/matches"
        response = requests.get(urlmatches, headers=headers)
        data = response.json()

        # Save to cache
        CACHE[prefix] = data
        CACHE_TIME[prefix] = now

    # 2. Process matches (from cache or fresh)
    upcoming_matches = []
    try:
        for match in data.get("matches", []):
            match_date = datetime.fromisoformat(
                match["utcDate"].replace("Z", "+00:00")
            ).date()

            if today < match_date < time_limit:
                upcoming_matches.append(match)
    except Exception as e:
        print("ERROR WITH MATCH", prefix, e)

    return upcoming_matches




def titlefinder(prefix):
    titles = {
        "PL": "Premier League",
        "PD": "La Liga",
        "WC": "World Cup",
        "FL1": "Ligue 1",
        "BL1": "Bundesliga",
        "SA": "Serie A",
        "CL": "Champions League"
    }
    return titles.get(prefix.upper(), "")

@app.route("/")
def index():
    prefix = "PL"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

@app.route("/laliga")
def laliga():
    prefix="PD"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    print("cock")
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))


@app.route("/bundasliga")
def bundasliga():
    prefix="BL1"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

@app.route("/ligue1")
def ligue1():
    prefix="FL1"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

@app.route("/worldcup")
def worldcup():
    prefix="WC"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

@app.route("/championsleague")
def championsleague():
    prefix="CL"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

@app.route("/seriea")
def seriea():
    prefix="SA"
    upcoming_matches = show_upcoming_matches(prefix, next_month)
    logo = db.execute("SELECT url from images WHERE competition = ?", prefix)
    return render_template("index.html", upcoming_matches=upcoming_matches, logo=logo[0]["url"], title=titlefinder(prefix))

def extract_team_crest(match, team_name):
    if match["homeTeam"]["name"] == team_name:
        return match["homeTeam"]["crest"]
    if match["awayTeam"]["name"] == team_name:
        return match["awayTeam"]["crest"]

@app.route("/teamstats", methods=["GET"])
def teamstats():
    team_name = request.args.get("team")
    print("TEAM SELECTED:", team_name)

    ALL_PREFIXES = ["PL", "PD", "SA", "BL1", "FL1", "CL"]

    # collect matches across all leagues
    combined_upcoming_matches = []

    for prefix in ALL_PREFIXES:
        try:
            matches = show_upcoming_matches(prefix, next_month)
            combined_upcoming_matches.extend(matches)
        except Exception as e:
            print("ERROR WITH PREFIX", prefix, e)

    # FILTER FOR THIS TEAM
    team_matches = [
    match for match in combined_upcoming_matches
    if team_name.lower() in match["homeTeam"]["name"].lower()
    or team_name.lower() in match["awayTeam"]["name"].lower()
]


    crest=""
    try:
        crest = extract_team_crest(team_matches[0], team_name)
    except Exception as e:
        crest="https://cdn-icons-png.flaticon.com/512/77/77305.png"
        print("ERROR WITH LOGO", e)

    return render_template(
        "teamstats.html",
        upcoming_matches=team_matches,
        logo=crest,
        title=f"{team_name} - Upcoming Fixtures",
        teamname=team_name
    )
