# Kpop Song Analyses: 
A statistical analysis of Korean pop (K-pop) music from 2000-2019.

## Background: 
K-pop is a genre of popular music from South Korea. However, to confine K-pop to just music is too simplistic. It is a fusion of music, visual art and fashion. Though K-pop has origins in the early 90s, modern K-pop truly emerged in the 2000s. K-pop artists tend to perform in boy or girl groups produced by large companies. 

Despite songs being in korean, the impact of K-pop is has gone beyond it's native borders and gone worldwide.

<p align="center"><a href="http://www.youtube.com/watch?feature=player_embedded&v=U7mPqycQ0tQ
" target="_blank"><img src="http://img.youtube.com/vi/U7mPqycQ0tQ/0.jpg" 
alt="Kpop Example" width="240" height="180" border="10" /></a>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=hmE9f-TEutc
" target="_blank"><img src="http://img.youtube.com/vi/hmE9f-TEutc/0.jpg" 
alt="Another Kpop Example" width="240" height="180" border="10" /></a>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=LlQEKB2H7z4
" target="_blank"><img src="http://img.youtube.com/vi/LlQEKB2H7z4/0.jpg" 
alt="Also Another Kpop Example" width="240" height="180" border="10" /></a></p>


## Hypotheses:
I'm interested in the musical song features for K-pop artists and how they differ with Western pop idols. Hopefully, these analyses will provide insight on why K-pop has grown in popularity around the world. 

## Dataset:
Wikipedia was scraped to obtain a list of kpop artists that have debuted from 2000-2019 (cut off: Sept 7, 2019, n = 378), along with information concerning the gender, debut year, and record company. Pudding (https://pudding.cool/2018/11/boy-bands/) was scraped to obtain a list of western boybands (n = 103) who have charted on the Billboard Hot 100 since 1980. The Spotify API was used to download all the song features for the discography:

* Acousticness
* Danceability
* Energy
* Instrumentalness
* Valence
* Tempo
* Popularity

## Methodology and Tools:
* Spotify Api
* Spotipy Library
* Beautiful Soup
* Python
* Numpy
* scikitlearn
* pandas
* jupyter notebook
* matplotlib
* seaborn
* Hypotheses Testing

## Results and Insight:

### Song Popularity 
I wanted to first to compare the popularity of songs between western pop idols and kpop idols. Song popularity is a 0-100 (most popular) measure from spotify that is based on the total number of plays and how recent those plays were. 

Before comparing song popularity, I examined the distribution of the data, so I can decide what hypothesis test would be appropriate. Both distributions do not look normal, so a hypothesis test the doesn't make an assumption of a distribution would be best: the Mann Whitney U test.

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Popularity_Density.png "Logo Title Text 1")

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Popularity_Violin.png "Logo Title Text 1")

__Null Hypothesis:__ Kpop song popularity is less than Western idol song popularity. 
__Alternate Hypothesis:__ Kpop song popularity is greater than Western idol song popularity. 

__Mann Whitney U test P-val for Kpop Popularity < Western Popularity: 0.0000000000__

Given an alpha value of 0.05, I can reject the null hypothesis. Therefore, there is statistical evidence suggesting that Kpop songs are more popular than western idol pop songs. 

### Song Features 

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Features_Density.png "Logo Title Text 1")


## Conclusions:

Kpop songs are more popular on Spotify compared to Western pop idols. When comparing the song features between Kpop Idols and Western Idols, Kpop Idols have songs that are more loud and energetic. 

## Future Work:

## References: 
