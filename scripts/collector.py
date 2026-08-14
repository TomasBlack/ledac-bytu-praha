import json

apartments = [
    {
        "id": 999,
        "title": "Byt vytvořený GitHub Action",
        "price": 12345678
    }
]

with open(
    "apartments-generated.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        apartments,
        f,
        ensure_ascii=False,
        indent=2
    )

print("apartments-generated.json vytvořen")
