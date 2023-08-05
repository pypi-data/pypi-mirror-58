from riot import APIRequest

__VERSION = "v1"


def entries_by_summoner_id(summoner_id, region=None):
    url = '/tft/league/{version}/entries/by-summoner/{encryptedSummonerId}'
    api = APIRequest(
        url.format(
            version=__VERSION,
            encryptedSummonerId=summoner_id
    ))
    return api.get(region), api.data