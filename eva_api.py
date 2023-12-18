from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

# Функция подгрузки данных модели
def load_model():
   model_pipeline = pipeline(model="AlexWortega/instruct_rugptlarge")
   return model_pipeline

# Класс для получения значения запрашиваемых параметров через API
class ApiParams(BaseModel):
   question: str
   
# Подгрузка модели
model = load_model()

# Объект для работы с api
app = FastAPI()

# Отправка результата запроса
@app.post("/answer/")
def answer(params: ApiParams):
   
    gen_kwargs = {
        "min_length": 20,
        "max_new_tokens": 100,
        "top_k": 50,
        "top_p": 0.9,
        "do_sample": True,
        "early_stopping": True,
        "no_repeat_ngram_size": 2,
        #"use_cache": True,
        "repetition_penalty": 1.5
        }
    result = model(params.question, **gen_kwargs)

    return result[0]['generated_text']
