import json, random
from datasets import load_dataset

ds = load_dataset("csebuetnlp/xnli_bn", revision="refs/convert/parquet", split="test")
print(ds)

names = getattr(ds.features["label"], "names", None) or ["contradiction", "entailment", "neutral"]
print("label names:", names)

random.seed(42)
sample = []
for label_id, name in enumerate(names):
    rows = [r for r in ds if r["label"] == label_id]
    print(name, "->", len(rows), "rows")
    sample += random.sample(rows, 35)
random.shuffle(sample)

with open("data/tasks/reasoning_nli.jsonl", "w", encoding="utf-8") as f:
    for i, r in enumerate(sample):
        f.write(json.dumps({
            "id": f"nli-{i:03d}", "task": "reasoning",
            "input": r["sentence2"], "context": r["sentence1"],
            "reference": names[r["label"]], "category": "nli",
        }, ensure_ascii=False) + "\n")

print("wrote", len(sample), "examples to data/tasks/reasoning_nli.jsonl")