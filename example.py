from SteamID import SteamID

steam_id = SteamID("76561198041007223")
steam_ids = [
    steam_id.get_steam_id(),
    steam_id.get_steam_id3(),
    steam_id.get_steam32_id(),
    steam_id.get_steam64_id(),
]

# Returns:
# STEAM_0:1:40370747
# U:1:80741495
# 80741495
# 76561198041007223
for id in steam_ids:
    print(id)