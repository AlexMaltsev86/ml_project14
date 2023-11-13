from transformers import pipeline

question = 'Где вечеринка?'
context = ('Вечеринка у Децла дома -Гуляют весь район, гуляет вся школа Вечеринка у Децла дома Все двигают попами под музыку хип-хопа.')

model_pipeline = pipeline(
   task='question-answering',
   model='timpal0l/mdeberta-v3-base-squad2'
)

print(model_pipeline(question=question, context=context))