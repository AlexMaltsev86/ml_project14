from transformers import pipeline

generator = pipeline(model="AlexWortega/instruct_rugptlarge")
EvaluationDay = generator("Какой будет сегодня день?", return_full_text=True)
print(EvaluationDay)
