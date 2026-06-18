#intro to matplotlib
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

sy = pd.read_csv('hw11_Spotify_Youtube_v4.csv', sep=',')
print(sy.head(5))

sy_sorted = sy.sort_values("Views") #sort data by views 
fig, ax1 = plt.subplots(figsize=(10, 6)) #10 inches wide 6 inches high 

ax1.plot(sy_sorted['Views'], sy_sorted['Likes'], color = 'blue', label='likes') #views by likes 
ax1.set_xlabel('Views')
ax1.set_ylabel('Likes', color='blue')
ax1.tick_params(axis='y', colors='blue')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(loc='upper left')

ax2 = ax1.twinx() #second y axis for columns 
ax2.plot(sy_sorted['Views'], sy_sorted['Comments'], color='red', label='Comments')
ax2.set_ylabel('Comments', color = 'red')
ax2.tick_params(axis = 'y', colors = 'red')
ax2.set_yscale('log')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()

#problem 2 

sy_artist = sy.groupby("Artist")[["Likes", "Views", "Stream", "Comments"]].sum()
sy_artist = sy_artist.sort_values("Likes", ascending=False).head(4) #take the top 4 
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx() #secondary y axis 

width = 0.25 
xticks = np.arange(len(sy_artist)) #gets xticks for top 4 artists
artists = sy_artist.index

posviews = xticks + (0 - 1) * width
posstreams = xticks + (1 - 1) * width
poscomments = xticks + (2 - 1) * width 

bar1 = ax1.bar(posviews, sy_artist["Views"], color='blue', label = 'Views')
bar2 = ax1.bar(posstreams, sy_artist['Stream'], color = 'green', label='Stream')
ax1.legend(loc='upper right')
bar3 = ax2.bar(poscomments, sy_artist['Comments'], color = 'red', label='Comments')
ax2.legend(loc='upper left')

ax1.set_ylabel('Views / Stream')
ax2.set_ylabel('Comments')
ax1.set_xticks(xticks)
ax1.set_xticklabels(artists, rotation =45, ha='right')

def addlabels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            f'{height:.1e}',
            ha='center', va='bottom', fontsize=8
        )

addlabels(ax1, bar1)
addlabels(ax1, bar2)
addlabels(ax2, bar3)

plt.tight_layout()
plt.show()











