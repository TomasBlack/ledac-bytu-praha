import json

apartments = [
    {
        "id": 1,
        "title": "Testovací byt",
        "price": 8000000
    }
]

with open("apartments-generated.json", "w", encoding="utf-8") as f:
    json.dump(
        apartments,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Soubor apartments-generated.json vytvořen")
