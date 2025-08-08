from transformers import pipeline

text_generate = pipeline('text-generation',model='gpt2')
quest         = pipeline('question-answering')


def generate_text(prompt):
    res = text_generate(prompt,max_length=100,num_return_sequences=1)
    return res[0]['generated_text']

def ques_answer(ques):
    res = quest(ques)
    return res[0]['answer']