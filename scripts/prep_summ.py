import json, random
from datasets import load_dataset

ds = load_dataset("csebuetnlp/xlsum", revision="refs/convert/parquet",
                  data_dir="bengali", split="test")
print(ds)

# keep articles short enough for small models
rows = [r for r in ds if 500 < len(r["text"]) < 3000 and r["summary"]]
print("usable rows:", len(rows))

random.seed(42)
sample = random.sample(rows, 100)

with open("data/tasks/summarisation.jsonl", "w", encoding="utf-8") as f:
    for i, r in enumerate(sample):
        f.write(json.dumps({
            "id": f"sum-{i:03d}", "task": "summarisation",
            "input": r["text"], "context": "",
            "reference": r["summary"], "category": "news",
        }, ensure_ascii=False) + "\n")

print("wrote 100 examples to data/tasks/summarisation.jsonl")