import editdistance
import re
text = ""
way_to_text_file = "C:/Users/matkl/OneDrive/Рабочий стол/python_projects/calculator/text_analysis/prince.txt"
with open(way_to_text_file, 'r', encoding="utf-8") as file:
    text = file.read()

list_of_words = [i for i in re.findall(r'\b\w+\b', text)]

query_words = ['text', 'rose', 'fox', 'pc']
query_pattern = r'\b(' + r')\b.*\b('.join(query_words) + r')\b'
print(query_pattern)