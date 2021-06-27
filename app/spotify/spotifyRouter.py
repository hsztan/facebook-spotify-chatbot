from app import app
from flask import render_template, request
from app.helpers.spotify import search_artist_name, get_artist, get_artist_tracks, get_artist_relateds


@app.route('/')
def index():
    return render_template('views/index.html')

@app.route('/search', methods=['POST'])
def search():
    artista = request.values.get('artista')
    data = search_artist_name(artista)
    api_url = data['artists']['href']
    items = data['artists']['items']
    return render_template('views/search.html', artist_name=artista, results=items, api_url=api_url)

@app.route('/artist/<id>')
def artist(id):
    artist_data = get_artist(id)

    tracks_data = get_artist_tracks(id)
    tracks = tracks_data['tracks']

    relateds_data = get_artist_relateds(id)
    relateds = relateds_data['artists']

    return render_template('views/artist.html', artist=artist_data, relateds=relateds, tracks=tracks)
