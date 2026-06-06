# Footle: Live Football Scores & Fixtures

A full-stack web app for checking live football scores and upcoming fixtures across Europe's top competitions — built with Python Flask, JavaScript, SQL, and Bootstrap.

**[Watch the demo](https://youtu.be/mWRBRNC1e9o)**

<img width="1857" height="799" alt="image" src="https://github.com/user-attachments/assets/4a6896a9-f112-46dd-88fd-5e17fb33173f" />

---

## What it does

- View live scores and upcoming fixtures across 6 European competitions (including the Premier League and Champions League)
- Search through matches in real time using a JavaScript-powered search bar
- Check all upcoming fixtures for a specific team across every competition via a "Check Stats" button
- Animated **LIVE!** indicator using CSS keyframes and glow effects for ongoing matches

---

## Technical challenges solved

### API rate limiting
The "Check Stats" feature sends 6 simultaneous requests to Football Data's free API (one per competition). The free tier caps requests at 10 per minute, meaning the button alone could crash the feed if clicked more than once.

To fix this, I implemented a server-side cache in `app.py`. Responses are stored locally and refreshed every 10 minutes. This eliminated the crash risk and cut load times significantly — the site can serve cached data instantly rather than waiting on the API each time.

### Incomplete API responses
Football Data's API occasionally returns incomplete or malformed data. I added conditional checks throughout the Flask routes and Jinja templates so the site loads cleanly even when certain fields are missing.

### Image storage
Rather than storing 7–8 competition badge images as static files, the URLs are stored in a SQL database and fetched at render time. This keeps the static folder lean and gave me a practical use case for SQL beyond CS50's problem sets.

---

## How it works

The app sends requests to [Football Data's API](https://www.football-data.org/) using Python's `requests` library. Each API call returns a dictionary of match data, which Flask passes to the front-end via Jinja templating. JavaScript handles the search bar filtering — showing and hiding match cards dynamically without a page reload. Bootstrap and custom CSS handle layout and responsiveness across desktop and mobile.

---

## Stack

| Layer | Technology |
|---|---|
| Back-end | Python, Flask |
| Front-end | JavaScript, HTML, CSS, Bootstrap |
| Templating | Jinja2 |
| Database | SQL |
| Data source | Football Data API |

---

This was Footle by Ali Sheikh.

And this was CS50.
