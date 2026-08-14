import json

apartments = [
    {
        "id": 999,
        "title": "Byt vytvořený GitHub Action",
        "price": 12345678,
        "area_m2": 100,
        "layout": "3+kk",
        "construction": "cihla",
        "metro_distance_m": 100,
        "tram_distance_m": 50,
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
