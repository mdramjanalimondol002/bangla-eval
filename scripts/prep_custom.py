import json

CATEGORIES = {"arithmetic", "ordering", "calendar", "logic", "trick"}
rows = []

with open("data/custom_questions.txt", encoding="utf-8-sig") as f:
    for n, line in enumerate(f, start=1):
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3 or parts[0] not in CATEGORIES or not parts[1] or not parts[2]:
            print(f"PROBLEM on line {n}: {line.strip()}")
            continue
        rows.append(parts)

with open("data/tasks/reasoning_custom.jsonl", "w", encoding="utf-8") as f:
    for i, (cat, question, answer) in enumerate(rows):
        f.write(json.dumps({
            "id": f"cus-{i:03d}", "task": "reasoning",
            "input": question, "context": "",
            "reference": answer, "category": cat,
        }, ensure_ascii=False) + "\n")

print("wrote", len(rows), "questions to data/tasks/reasoning_custom.jsonl")