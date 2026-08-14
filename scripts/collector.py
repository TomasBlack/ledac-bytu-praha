import json
from datetime import datetime

apartments = [
    {
        "id": 999,
        "title": "Byt vytvořený GitHub Action",
        "price": 12345678,
        "area_m2": 65,
        "layout": "2+kk",
        "construction": "cihla",
        "metro_distance_m": 300,
        "tram_distance_m": 100,
        "balcony": True,
        "cellar": True,
        "elevator": True,
        "source": "collector-test"
    }
]

output = {
    "generated_at": datetime.now().isoformat(),
    "count": len(apartments),
    "apartments": apartments
}

with open(
    "apartments-generated.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        output,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Vygenerováno {len(apartments)} bytů"
)
