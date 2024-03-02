from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia


# Функция подгрузки данных модели
def load_model():
    model_pipeline = pipeline(
        task="question-answering", model="timpal0l/mdeberta-v3-base-squad2"
    )
    return model_pipeline


# Класс для получения значения запрашиваемых параметров через API
class ApiParams(BaseModel):
    search_topic: str
    question: str


# Подгрузка модели
model = load_model()

# Объект для работы с api
app = FastAPI()


# Отправка результата запроса
@app.post("/answer/")
def answer(params: ApiParams):
    # Поиск статьи в википедии
    wiki_sum = wikipedia.summary(params.search_topic, sentences=10)
    # Ответ на вопрос
    result = model(params.question, params.search_topic)
    # Язык статьи
    wikipedia.set_lang("ru")
    # Страница википедии по запросу
    wiki_text = wikipedia.page(params.search_topic).content
    # Поиск ответа на вопрос по заданной странице википедии
    result = model(params.question, wiki_text)
    return result["answer"]
