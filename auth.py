def get_spotify_credentials():
    return dict(
        cid='',
        secret='',
    )


def get_mapbox_token():
    return open('auth/mapbox_token', 'r').read()
