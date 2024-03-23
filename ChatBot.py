import openai

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = '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'


def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Kullanılacak modeli belirtin
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Hoş geldiniz! ChatGPT-3 ile konuşmaya başlayın. Çıkış yapmak için 'quit' yazın.")
    
    while True:
        user_input = input("Sorunuz: ")
        
        if user_input.lower() == 'quit':
            print("Çıkış yapılıyor...")
            break
        
        response = chat_with_gpt3(user_input)
        print("ChatGPT-3 Cevabı:", response)

if __name__ == "__main__":
    main()
