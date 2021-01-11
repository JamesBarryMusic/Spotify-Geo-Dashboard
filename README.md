# Spotify Geo Dashboard

The aim of this project is to build a dashboard where the user can analyse geographically derieved 'audio profiles' based on audio features over time.

![image_header](https://raw.githubusercontent.com/JamesBarryMusic/Spotify-Geo-Dashboard/main/assets/SPOTIFY_GEO_DASHBOARD.png)


## How the webpage works?

**Spotify Charts**
The track constituents of the Spotify Top 200 charts are scraped for every week and every country. You can find the charts [here](spotifycharts.com).

**Spotify Web API and Track Audio Features**
The track audio features for all the tracks in the charts are retrieved via the Spotify Web API. You can find documentation describing the different [audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/).

**Data analysis**
Raw scores for each audio feature are calculated by the mean value of all the tracks in the chart of a country for each point in time. These scores are then also standardised for each country over time to allow for comparison between countries and points in time.

**Data Visualisation**
The data is visualised in 5 different ways:
* **Map** - A choropleth map visualises the z-scores for a singular audio feature at one point in time (default latest). The audio feature that is mapped can be selected from the dropdown and the week can be changed using the slider. Countries can be selected by clicking on them.
* **Country specific**
  * **Description** - A dynamic description of the current sentiment of the country relative to their history is displayed below the country name.
  * **Profile** - A polar histogram plots the mean raw score normalised against every other country for every audio feature. Therefore a 1 indicates it has the highest audio feature score and 0 the lowest.
  * **Distribution** - A chart plots the distributions of the audio feature raw scores for a country.
  * **Time series** - A time series chart plots the z-scores of the audio features over time for the selected country. The series that are plotted on the chart can be altered by clicking the legend labels (double clicking singles out a feature).



## Possible improvements

As all applications this one can also be improved. Possible improvements:

- Make it more dynamic; add update database functionality in the frontend.
- Better UI design.
- Add artist tracking.


## How to launch application

1. Check that you have flask installed.
2. install requirements: pip install -r requirements.txt
3. Sign up to developer.spotify.com and get cid + API secret.
4. Update cid + API secret in auth.py
3. Run : python update_databases.py
4. Run : python main.py to launch application.
5. Go to assigned link.
6. Enjoy browsing Spotify streaming data.
