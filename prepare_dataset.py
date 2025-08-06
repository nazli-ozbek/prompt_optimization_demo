import json

INPUT_FILE = "data/cases.jsonl"
OUTPUT_FILE = "data/new_cases.jsonl"
MAX_ROWS = 20

count = 0
with open(INPUT_FILE, "r", encoding="utf-8") as infile, open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for line in infile:
        if count >= MAX_ROWS:
            break

        obj = json.loads(line)
        if "facts" in obj and "violated_articles" in obj:
            if obj["facts"] and obj["violated_articles"]:
                filtered = {
                    "facts": obj["facts"],
                    "violated_articles": obj["violated_articles"]
                }
                outfile.write(json.dumps(filtered, ensure_ascii=False) + "\n")
                count += 1

print(f"Done! {count} rows written to {OUTPUT_FILE}")
