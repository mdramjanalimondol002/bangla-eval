import json, random
from datasets import load_dataset

ds = load_dataset("csebuetnlp/squad_bn", revision="refs/convert/parquet", split="test")

# keep questions that have an answer and a reasonably short passage
rows = [r for r in ds if r["answers"]["text"] and len(r["context"]) < 1500]
print("usable rows:", len(rows))

random.seed(42)
sample = random.sample(rows, 150)

with open("data/tasks/qa.jsonl", "w", encoding="utf-8") as f:
    for i, r in enumerate(sample):
        f.write(json.dumps({
            "id": f"qa-{i:03d}", "task": "qa",
            "input": r["question"], "context": r["context"],
            "reference": r["answers"]["text"][0], "category": "extractive",
        }, ensure_ascii=False) + "\n")

print("wrote 150 examples to data/tasks/qa.jsonl")