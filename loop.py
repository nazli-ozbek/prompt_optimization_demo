# loop.py
from data_loader import load_dataset
from generator import generate_prompt
from classifier import classify_event
from evaluator import evaluate

dataset = load_dataset("data/new_cases.jsonl")

results = []

for i in range(3):
    prompt = generate_prompt()
    print(f"\n Prompt #{i+1}:\n{prompt}")

    all_true = []
    all_pred = []

    for facts, true_labels in dataset:
        prediction = classify_event(prompt, facts)
        predicted_labels = [p.strip() for p in prediction.split(",") if p.strip().isdigit()]
        all_true.append(true_labels)
        all_pred.append(predicted_labels)

    f1 = evaluate(all_true, all_pred)
    results.append((prompt, f1))
    print(f"F1 Score: {f1:.3f}")

best_prompt, best_score = max(results, key=lambda x: x[1])
print("\nBest Prompt:")
print(best_prompt)
print(f"Final F1: {best_score:.3f}")
