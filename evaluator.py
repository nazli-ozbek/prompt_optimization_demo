from sklearn.metrics import f1_score
from typing import List

def evaluate(true_labels_list: List[List[str]], predicted_labels_list: List[List[str]]) -> float:
    all_labels = sorted(list(set(label for labels in true_labels_list for label in labels)))

    def to_binary_vector(label_list):
        return [1 if label in label_list else 0 for label in all_labels]

    y_true = [to_binary_vector(labels) for labels in true_labels_list]
    y_pred = [to_binary_vector(labels) for labels in predicted_labels_list]

    return f1_score(y_true, y_pred, average='micro')
