def get_spotify_credentials():
    return dict(
        cid='4992da23ca80481c8e94a93c62ddcda6',
        secret='e96b70f133504d30b0d6651fcd9bfe13',
    )


def get_mapbox_token():
    return open('auth/mapbox_token', 'r').read()
