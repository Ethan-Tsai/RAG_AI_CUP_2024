import json

# 讀取 ground truth 和 prediction 資料
with open("data/dataset/preliminary/ground_truths_example.json", "r") as f:
    ground_truths = json.load(f)["ground_truths"]

with open("data/dataset/preliminary/pred_retrieve.json", "r") as f:
    predictions = json.load(f)["answers"]

# 將資料轉換為字典，方便查詢
ground_truth_dict = {item["qid"]: item["retrieve"] for item in ground_truths}
prediction_dict = {item["qid"]: item["retrieve"] for item in predictions}

# 計算正確率
correct_count = 0
total_count = len(ground_truth_dict)

for qid, true_retrieve in ground_truth_dict.items():
    pred_retrieve = prediction_dict.get(qid)
    if pred_retrieve == true_retrieve:
        correct_count += 1

accuracy = correct_count / total_count if total_count > 0 else 0
print(f"正確率：{accuracy:.2%}")
