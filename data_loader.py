import json

def load_dataset(jsonl_path):
    data = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            facts = " ".join(item["facts"]).strip()
            labels = [v.strip() for v in item["violated_articles"]]
            data.append((facts, labels))
    return data
