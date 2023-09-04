import random
import time
from googletrans import Translator
import os

translator = Translator()

with open('Vocabulary.txt', 'r', encoding='utf-8') as file:
    file_lines = file.readlines()

single_word_lines = [line.strip() for line in file_lines if len(line.split()) == 1]

random.shuffle(single_word_lines)

batch_size = 10
batches = [single_word_lines[i:i+batch_size] for i in range(0, len(single_word_lines), batch_size)]

output_directory = 'FlashCardsResalt'
os.makedirs(output_directory, exist_ok=True)

timestamp = int(time.time())  # Текущее время в секундах

for batch_number, batch in enumerate(batches, start=1):
    session_batch_filename = f'fc_{timestamp}_{batch_number:02d}.txt'
    full_filename = os.path.join(output_directory, session_batch_filename)
    
    print(f"Batch {batch_number}:\n")
    
    with open(full_filename, 'w', encoding='utf-8') as output_file:
        for word in batch:
            translation = translator.translate(word, src='en', dest='ru')
            print(f"{word}={translation.text}")
            output_file.write(f"{word}={translation.text}\n")
    
    print()  # Пустая строка между пакетами
