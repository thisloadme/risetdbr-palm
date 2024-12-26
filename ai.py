import config
import google.generativeai as palm

palm.configure(api_key=config.API_KEY)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def generate_answer(prompt):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=300,
    )

    return completion.result

teks = input("input prompt:")
answer = generate_answer(teks)
print(answer)