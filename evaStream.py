from transformers import pipeline
import streamlit as st


# Функция подгрузки данных модели
@st.cache_resource
def load_model():
    model_pipeline = pipeline(model="AlexWortega/instruct_rugptlarge")
    return model_pipeline


# Функция запуска модели
def execute(question):   

   gen_kwargs = {
        "min_length": 20,
        "max_new_tokens": 100,
        "top_k": 50,
        "top_p": 0.9,
        "do_sample": True,
        "early_stopping": True,
        "no_repeat_ngram_size": 2,
        # "use_cache": True,
        "repetition_penalty": 1.5,
    }
    result = model(question, **gen_kwargs)
    st.text("Ответ на вопрос: " + result[0]["generated_text"])


# Заголовок
st.title(body='Приложение отвечающее на пользовательские вопросы')

# Вопрос
question = st.text_input(label="Введите вопрос", value=" ")
# Активность кнопки
if question == " ":
    disabled = True
else:
    disabled = False
# Подгрузка модели
model = load_model()
# Кнопка для запуска модели
executed = st.button(label="Выполнить", disabled=disabled)
if executed:
    execute(question)
