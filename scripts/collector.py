import json

print("Načítám konfiguraci...")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

with open("sources.json", "r", encoding="utf-8") as f:
    sources = json.load(f)

print("URL Sreality:")
print(sources["sreality_search_url"])

print("Konfigurace:")
print(config)

apartments = [
    {
        "id": 1,
        "title": "Test ze sources.json",
        "price": 8000000,
        "area_m2": 55,
        "layout": "2+kk",
        "construction": "cihla",
        "metro_distance_m": 200,
        "tram_distance_m": 100,
        "balcony": True,
        "cellar": True,
        "elevator": True
    }
]

with open(
    "apartments.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        apartments,
        f,
        ensure_ascii=False,
        indent=2
    )

print("apartments.json vytvořen")
