import json

print("Načítám konfiguraci...")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

with open("sources.json", "r", encoding="utf-8") as f:
    sources = json.load(f)

print("URL Sreality:")
print(sources["sreality_search_url"])

apartments = []

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
