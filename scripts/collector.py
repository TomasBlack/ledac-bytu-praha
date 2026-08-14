import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

apartments = [
    {
        "id": 1,
        "title": "Špitálská, Praha 9",
        "price": 7790000,
        "area_m2": 57,
        "layout": "2+kk",
        "construction": "cihla",
        "metro_distance_m": 198,
        "tram_distance_m": 69,
        "balcony": False,
        "cellar": True,
        "elevator": False
    },
    {
        "id": 2,
        "title": "Sousedíkova, Praha 9",
        "price": 9360000,
        "area_m2": 59,
        "layout": "2+kk",
        "construction": "cihla",
        "metro_distance_m": 586,
        "tram_distance_m": 220,
        "balcony": True,
        "cellar": True,
        "elevator": True
    }
]

filtered = []

for apartment in apartments:

    if apartment["price"] > config["max_price"]:
        continue

    if apartment["area_m2"] < config["min_area"]:
        continue

    if apartment["layout"] not in config["allowed_layouts"]:
        continue

    if apartment["construction"] in config["exclude_construction"]:
        continue

    if apartment["layout"] in config["exclude_layouts"]:
        continue

    filtered.append(apartment)

with open(
    "apartments.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        filtered,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Uloženo {len(filtered)} bytů")
