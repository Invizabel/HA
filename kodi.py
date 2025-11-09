import json

url = "http://kodi.arpa:8080/jsonrpc?request="

rom_path = "/storage/ROMS/GB/demo.gb"

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "Addons.ExecuteAddon",
    "params": {
        "addonid": "game.libretro.mgba",
        "params": [rom_path],
        "wait": True
    }
}

print(json.dumps(payload))
