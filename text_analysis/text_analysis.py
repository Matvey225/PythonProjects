import editdistance
import re

query = input()

text = ""
way_to_text_file = "C:/Users/matkl/OneDrive/Рабочий стол/python_projects/calculator/text_analysis/prince.txt"

with open(way_to_text_file, 'r', encoding='utf-8') as file:
        text = file.read()


def find_similar_words(query, text):
    components = query.split()
    sim_word = []
    list_of_words = [i for i in re.findall(r'\b\w+\b', text)]
    for part in components:
        for word in list_of_words:
            if editdistance.eval(part, word) == 1 or editdistance.eval(part, word) == 2 or editdistance.eval(part, word) == 3:
                sim_word.append(word)
        if len(list_of_words) == 0:
            return query
        else:
            return sim_word[0]
    
def sentences_with_query(query, way_to_text_file):
    # разделение запроса на части
    components = query.split()
    

    query_pattern = r'\b(' + r')\b.*\b('.join(components) + r')\b'
    query_regex = re.compile(query_pattern, re.IGNORECASE)
    
    list_of_sentences = re.split(r'[.!?]+', text)
    the_found_sentences = []

    for i in list_of_sentences:
        if query_regex.search(i):
            the_found_sentences.append(i.strip())
    return the_found_sentences
    
query = find_similar_words(query, text)
answer = sentences_with_query(query, way_to_text_file)

print(*answer)