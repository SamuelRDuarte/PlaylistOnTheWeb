from django.shortcuts import render
from BaseXClient import BaseXClient
import xmltodict
# Create your views here.

session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

def home(request):
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track return <elem> {$a/name} {$a/external_urls/spotify} </elem> } </root>"
    query = session.execute(input)
    print(query)
    info = dict()
    res = xmltodict.parse(query)
    print(res)
    for c in res["root"]["elem"]:
        info[c["name"]] = c["spotify"]
    tparams = {
        'tracks': info,
        'frase': "Músicas da Playlist Pokémon LoFi:",
    }
    return render(request, "tracks.html", tparams)