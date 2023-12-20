# Практические задания по курсу "Программная инженерия"
1. Файл evaluation.py: Используемая модель https://huggingface.co/AlexWortega/instruct_rugptlarge, Модель отвечает на вопрос "Какой сегодня будет день?"
2. Файл answ.py : Используемая модель https://huggingface.co/timpal0l/mdeberta-v3-base-squad2 . Модель позволяет получать ответы на пользовательские вопросы на основе заданного текста
3. Добавлен интерфейс в стримлит с элементами: Заголовок, область ввода, поле ввода, кнопка, текст в модель answ.py
4. Добавлен файл answ_api.py и requirements.txt для домашнего задания по api
5. Добавлен файл evaStream.py, интерфейс в стримлит для модели evaluation.py
6. Добавлен файл Cloud.py, приложение в облаке, отвечающее на вопросы по тексту. Используемая модель https://huggingface.co/deepset/roberta-base-squad2.
7. Добавлен файл CloudApi.py, реализация Api приложения. Используемая модель https://huggingface.co/deepset/roberta-base-squad2.
8. Добавлен файл test_CloudApi.py, тесты для приложения CloudApi.py.

# Итоговое приложение

Приложение используется модель https://huggingface.co/deepset/roberta-base-squad2. Выполняет поиск ответа на вопрос по тексту.

Структура файлов
1. Cloud.py - файл приложения для публикации в облаке streamlit
2. CloudApi.py - файл приложения, реализующий интерфейс api
3. test_CloudApi.py - файл тестов

Приложение опубликовано в облаке streamlit https://mlproject14-kbzvc5fnzdrhalbamjnro7.streamlit.app/
Для запуска нужно:
1. Задать текст
2. Задать вопрос
3. Нажать выполнить. В результате будет выведен ответ.

![image](https://github.com/AlexMaltsev86/ml_project14/assets/149813897/026b9561-ffab-4828-9f4b-6bd6476968ce)
   



