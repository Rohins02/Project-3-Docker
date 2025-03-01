import os
import re
import collections
import socket
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

file1_path = "/home/data/IF-1.txt"
file2_path = "/home/data/AlwaysRememberUsThisWay-1.txt"
output_path = "/home/data/output/result.txt"

os.makedirs("/home/data/output", exist_ok=True)

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def process_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s']", " ", text)  
    words = word_tokenize(text)
    return words

def handle_contractions(words):
    expanded_words = []
    contractions_map = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "it's": "it is",
        "you're": "you are", "won't": "will not", "didn't": "did not", "that's": "that is"
    }
    for word in words:
        expanded_words.extend(contractions_map.get(word, word).split())
    return expanded_words

text1 = process_text(read_file(file1_path))
text2 = handle_contractions(process_text(read_file(file2_path)))

count1 = len(text1)
count2 = len(text2)
total_count = count1 + count2

top_words_1 = collections.Counter(text1).most_common(3)
top_words_2 = collections.Counter(text2).most_common(3)

ip_address = socket.gethostbyname(socket.gethostname())

with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(f"Total words in IF-1.txt: {count1}\n")
    output_file.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {count2}\n")
    output_file.write(f"Grand total of words: {total_count}\n")
    output_file.write(f"Top 3 words in IF-1.txt: {top_words_1}\n")
    output_file.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_words_2}\n")
    output_file.write(f"Container IP Address: {ip_address}\n")

with open(output_path, "r", encoding="utf-8") as result_file:
    print(result_file.read())
