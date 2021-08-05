{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import spotipy\n",
    "import spotipy.util as util\n",
    "from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the URL you were redirected to:  https://developer.spotify.com/dashboard/login?code=AQBf_Z6Flflwk-GUEAODee7WNCqqn6XthF2KUoRC6XBCISpnzt0WRfYcgj55SQjvK8M3q6b9fdFaPzE9g4ZRHpaP0sbiFP_6iQ91AUvl7fSTx3oHF7q7jFh6s4oqwN1EE_MnXFY03p3SZOfgPsBBq4tpIVTKcuTTNVIapVzSy_pevDowAlk3s3LfSePIYvwk_Jm8r4JyjNpHskX64oKOclgwKmBUKilp9pQj37zPjph69KwShdKCShSs_Q33B_INE91T4P-_rskop03owA51D9j9-adMSkWHIokdaeWJnrSm1PfnGfyOhJVNqT6UE-5eq6xV6FZPadfH17qBVcu4bkmdqegmRT36zIWodXbUjvtiV9J9nxDJlPa83qkOnA\n"
     ]
    }
   ],
   "source": [
    "'''Config'''\n",
    "\n",
    "# Once landed on the App Dashboard, select edit settings and set the dashboard URL that you have on your tab as the Redirect URI.\n",
    "client_id = \"e4fbca07a1234a0493f2303d2b65846a\"\n",
    "client_secret = \"f519c9cec75045d9b750b570003f12de\"\n",
    "user = \"WhistlingFawn\"\n",
    "\n",
    "# In order to avoid out of scope token, we take as much permissions as possible: https://developer.spotify.com/web-api/using-scopes/\n",
    "scope = \"playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative\"\n",
    "uri = \"https://developer.spotify.com/dashboard/applications/e4fbca07a1234a0493f2303d2b65846a\"\n",
    "\n",
    "client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) \n",
    "sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)\n",
    "token = util.prompt_for_user_token(user, scope, client_id, client_secret, uri)\n",
    "\n",
    "if token:\n",
    "    sp = spotipy.Spotify(auth=token)\n",
    "else:\n",
    "    print(\"Token not available for\", user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Fast Recall'''\n",
    "\n",
    "PlaylistID = '6v0CBKAwPP0OjF7n6QNSIW'\n",
    "playlist = sp.user_playlist(user, PlaylistID);\n",
    "tracks = playlist[\"tracks\"];\n",
    "songs = tracks[\"items\"];\n",
    "\n",
    "# Need to insert genres, artist name and BPM as well\n",
    "track_ids = []\n",
    "track_names = []\n",
    "\n",
    "for i in range(0, len(songs)):\n",
    "    if songs[i]['track']['id'] != None: \n",
    "        track_ids.append(songs[i]['track']['id'])\n",
    "        track_names.append(songs[i]['track']['name'])\n",
    "\n",
    "features = []\n",
    "for i in range(0,len(track_ids)):\n",
    "    audio_features = sp.audio_features(track_ids[i])\n",
    "    for track in audio_features:\n",
    "        features.append(track)\n",
    "        \n",
    "df = pd.DataFrame(features, index = track_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Playlist Specific Recall'''\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Audio Features'''\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
