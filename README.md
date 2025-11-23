Footle: Football Stats Tracker
https://youtu.be/mWRBRNC1e9o

I have created a simple interface to see the upcoming football (soccer) matches for certain teams and leagues in Europe, which can be searched through and clicked on.

I took a lot of inspiration from another app called "FotMob", which essentially does what Footle does (but better), on a mobile application.

At first, I wasn't sure how I was going to import all the data into the wesbite and thought I might have to create one large database using SQL, however, this:
a) wouldn't be live and update with scores as time went on
b) would be very storage inefficient and potentially slow down the website

Therefore, I opted to using a free football API that allowed me to send requests to using the "requests" library in python.

In addition, I wanted to use SQL somewhere in my website, having enjoyed using it so much over the course of CS50, so on my website, the url's of the images for the competitions,
such as the Premier Leaguue's Logo, are stored in there. This was because I didn't want to have 7-8 image files stored in my static taking up memory so I thought of using this
creative and unique way to still show the images on my wesbite.


<h3>The Project itself...</h3>

The project uses football data.org's free API, which has access to many competitions with live score data. It uses the requests library to open a http client and send requests to the API using the API key and a "header" parameter. When prompted with the right league, it returns all the upcoming matches in one big dictionary, which you can sort through using key-value pairs, for example using dictionary comprehension you can see all the upcoming matches using list["matches"]. This large dictionary passed as an argument into the website when rendered which is then, using jinija, is iterated over and (using CSS and HTML) creates lots of div tags which include the logo, title and date of the match.

I then included a search bar - allowing the user to search through the upcoming matches. It uses JavaScript to take in the search and then if the home or away side of each div includes that search to show them and hide the rest as they are not necessary to be shown.

I then also included a "Check Stats" button, which allowed the user to look through a certain team's upcoming matches through all competitions, including Champions League and their own national league. This raised a big problem however - the request limit. Football Data's free API has a request limit of 10 times per minute, however the check stats button alone sent 6 requests each time pressed as it asked for info from all 6 competitions that I show, even pressed on the tabs more than 10 times in a minute crashes means that the API stops sending data back and nothing shows on the webiste.

This was a problem.

So I added a cache. When the requests are sent, they are stored locally in app.py and are updated every 10 minutes. Not only does this fix the issue of the website crashing, but it also increases the speed of the site loading as the website can just check the cache for the data rather than request and wait for the API to respond which can sometimes take a few seconds.

I also learned how to do CSS animation using keyframes and glow effects which I applied on my h1 tag, which is used for the "LIVE!" part of live matches.

In addition to these core features, I also spent time making the website easier to navigate and more intuitive for users. This included refining the layout of match cards, experimenting with different Bootstrap components, and ensuring the interface worked smoothly on both desktop and mobile devices. I wanted the experience to feel clean and responsive, especially because football fixtures are something people often check quickly and casually.

Another challenge I faced was error-handling, particularly when the API returned incomplete or unexpected data. To address this, I added conditional checks in my Flask routes and templates so the website would still load even if certain pieces of information were missing.

Overall, this project taught me a lot about full-stack development, debugging, and designing a practical application that solves a real problem.

<img width="1857" height="799" alt="image" src="https://github.com/user-attachments/assets/4a6896a9-f112-46dd-88fd-5e17fb33173f" />


This was Footle by Ali Sheikh.

And this was CS50.






