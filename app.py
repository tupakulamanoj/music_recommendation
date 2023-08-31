from flask import Flask,render_template,request
from src.components.data_ingestion import data_ingest
from src.components.data_transformation import transform
from src.components.model_process import model_process
import re
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="your client_id",
                                                           client_secret="your client_secret_key"))

app=Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def hello():
    if request.method == 'POST':
        song_name=request.form['song']      
        def recommended_songs(song_name):
            obj=data_ingest()
            data_path,track_path=obj.data_dividing()
            obj1=transform()
            track,data,vector=obj1.transformation(data_path,track_path)
            obj2=model_process()
            p=obj2.recommend_process1(song_name,track,vector)
            if len(p)== 0:
                song=['Justified & Ancient - Stand by the Jams','I Know You Want Me (Calle Ocho)',"From the Bottom of My Broken Heart","Apeman - 2014 Remastered Version","You Can't Always Get What You Want"]
                artist_name=["The KLF","Pitbull","The Rolling Stones","Britney Spears","The Kinks"]
                q=["selected song is like not so popular!some of popular songs recommendations"]
                    
            else:
                artist_name=[]
                song=[]
                for i in range(len(p)):
                    song.append(p.iloc[i][0])
                    artist_name.append(p.iloc[i][1])
                data.drop_duplicates(subset=['Track Name'],keep='first',inplace=True)
                q=['some of popular songs recommendations']
            track_lis=[]
            artist_id=[]
            for i in range(len(song)):
                track_lis.append(data[data['Track Name']== song[i]]['Track URI'])
                artist_id.append(data[data['Track Name']== song[i]]['Artist URI(s)'])
            artist_names=[]
            image_links=[]
            track_name=[]
            spotify_link=[]
                
            for i in range(len(track_lis)):
                link=re.findall("spotify.*",str(track_lis[i]))[0]
                res=sp.track(link)
                artist_link=re.findall("spotify.*",str(artist_id[i]))[0]
                image=sp.artist(artist_link)
                image_link=dict(image['images'][0])['url']
                artist_names.append(artist_name[i])
                image_links.append(image_link)
                track_name.append(res['name'])
                spotify_link.append(res['external_urls']['spotify'])
            return (
                artist_names,image_links,track_name,spotify_link,q
            )
        artist_names,image_links,track_name,spotify_link,q=recommended_songs(song_name=song_name)
        return render_template("index2.html",artist_names=artist_names,image_links=image_links,track_name=track_name,spotify_link=spotify_link,q=q)
        

    return render_template('index.html')

if __name__=='__main__':
    
    app.run(debug=True)
