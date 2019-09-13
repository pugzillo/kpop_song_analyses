# Kpop Song Analyses 
A statistical analysis of Korean pop (K-pop) music from 2000-2019.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Kpop Song Analyses:](#kpop-song-analyses)
  - [Background:](#background)
  - [Hypotheses:](#hypotheses)
  - [Dataset:](#dataset)
  - [Methodology and Tools:](#methodology-and-tools)
  - [Results and Insight:](#results-and-insight)
    - [Song Popularity](#song-popularity)
  - [Conclusions:](#conclusions)
  - [Future Work:](#future-work)
  - [References:](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Background 
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


## Hypotheses
I'm interested in the musical song features for K-pop artists and how they differ with Western pop idols. Hopefully, these analyses will provide insight on why K-pop has grown in popularity around the world. 

## Dataset
Wikipedia was scraped to obtain a list of kpop artists that have debuted from 2000-2019 (cut off: Sept 7, 2019, n = 378), along with information concerning the gender, debut year, and record company. Pudding (https://pudding.cool/2018/11/boy-bands/) was scraped to obtain a list of western boybands (n = 103; 51 who first hit the Billboard Hot 100 in 2000-2018) who have charted on the Billboard Hot 100 since 1980. The Spotify API was used to download all the song features for the discography:

* Acousticness
* Danceability
* Energy
* Instrumentalness
* Liveness
* Speechiness
* Loudness
* Valence
* Tempo
* Popularity

For comparisons between kpop idols and western idols, I only used boybands and those the debuted between 2000-2019 (kpop) and those that first reached the billboard hot 100 in the 2000s. 

## Methodology and Tools
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

## Results and Insight

### Song Popularity Comparison between Western Idols and Kpop Idols
I wanted to first to compare the popularity of songs between western pop idols and kpop idols. Song popularity is a 0-100 (most popular) measure from spotify that is based on the total number of plays and how recent those plays were. 

Before comparing song popularity, I examined the distribution of the data, so I can decide what hypothesis test would be appropriate. Both distributions do not look normal, so a hypothesis test the doesn't make an assumption of a distribution would be best: the Mann Whitney U test.

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Popularity_Density.png "Logo Title Text 1")

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Popularity_Violin.png "Logo Title Text 1")

__Null Hypothesis:__ Kpop song popularity is less than Western idol song popularity. 

__Alternate Hypothesis:__ Kpop song popularity is greater than Western idol song popularity. 

__Mann Whitney U test P-val for Kpop Popularity < Western Popularity: 0.0000000000__

Given an alpha value of 0.05, I can reject the null hypothesis. Therefore, there is statistical evidence suggesting that Kpop songs are more popular than western idol pop songs. As of September 7, 2019, the most popular K-pop song is Boy with Luv by BTS and Halsey. 

### Song Feature Comparison between Western Idols and Kpop Idols

To understand the distributions of the different song features, I created histograms for each song feature for both Western and K-pop male idols from 2000 to 2019.

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_Features_Density.png "Logo Title Text 1")

For certain measures, there seems to be differences in the distributions: Dancebility, Energy, Instrumentalness, and loudness. Instrumentalness may be due to the inclusion of instrumental versions of songs, which is common (must check this later!).

Let's check the difference in Energy, Loudness, and Danceability in the meanwhile. Given that we're doing multiple test, let's use a bonferroni corrected alpha ( alpha = 0.05/9 song features: 0.005 ).

![alt text](https://github.com/pugzillo/kpop_song_analyses/blob/master/images/Song_LoudEnergyDance_Violin.png "Logo Title Text 1")

#### Energy
__Null Hypothesis:__ Kpop song energy is less than Western idol song energy. 

__Alternate Hypothesis:__ Kpop song energy is greater than Western idol song energy. 

__Mann Whitney U test P-val for Kpop Energy < Western Energy: 0.0000000000__


#### Dancability
__Null Hypothesis:__ Kpop song danceability is less than Western idol song danceability. 

__Alternate Hypothesis:__ Kpop song danceability is greater than Western idol song danceability. 

__Mann Whitney U test P-val for Kpop danceability < Western danceability: 0.0000000000__


#### Loudness
__Null Hypothesis:__ Kpop song loudness is less than Western idol song loudness. 

__Alternate Hypothesis:__ Kpop song loudness is greater than Western idol song loudness. 

__Mann Whitney U test P-val for Kpop loudness < Western loudness: 0.0000000000__


## Conclusions

Kpop songs are more popular on Spotify compared to Western pop idols. When comparing the song features between Kpop Idols and Western Idols, Kpop Idols have songs that are more loud, energetic, and danceable. 

## Future Work

Given the multidimensional aspects of Kpop, (For example, the importance of music videos), it would be interesting to examine the differences between Western Pop Idols and Kpop Idols Youtube views and how it relates to audio streams. Also, given the increasing number of Kpop idol debuts, it would also interesting to predict long term popularity of Kpop Idols based off of their early youtube views of their debut music videos.  

## References 
Internet Boyband Database: https://pudding.cool/2018/11/boy-bands/

Billboard: https://www.billboard.com/articles/columns/k-town/8500363/k-pop-closer-than-ever-american-pop-mainstream
