from transformers import pipeline
import streamlit as st

# Функция подгрузки данных модели
@st.cache_resource
def load_model():
   translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
   return translator

# Функция запуска модели
def execute(question):
   
    result = model(question)
    st.text('Перевод: ' + result[0]['translation_text'])

# Заголовок
st.title(body= 'Приложение выполняющее перевод с Английский на Русский')

# Текст
question = st.text_input(label='Введите текст',value=' ')
# Активность кнопки
if question == ' ':
   disabled = True
else:
   disabled = False
# Подгрузка модели
model = load_model()
# Кнопка для запуска модели
executed = st.button(label='Выполнить', disabled=disabled)
if executed:
   execute(question)
