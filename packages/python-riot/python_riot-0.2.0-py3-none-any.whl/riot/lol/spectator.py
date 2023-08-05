from riot import APIRequest

__VERSION = "v4"

def active_game_by_summoner_id(summoner_id, region=None):
    url = '/lol/spectator/{version}/active-games/by-summoner/{encryptedSummonerId}'
    api = APIRequest(
        url.format(
            version=__VERSION,
            encryptedSummonerId=summoner_id
        )
    )
    return api.get(region), api.data
