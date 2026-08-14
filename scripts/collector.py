import json

print("Načítám konfiguraci...")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print()

for source in config["sources"]:
    print(f"Zdroj: {source['name']}")
    print(f"URL: {source['url']}")
    print()

output = {
    "generated": True,
    "sources": config["sources"]
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

print("apartments-generated.json vytvořen")
