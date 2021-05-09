black_list = ["chapter", "mr", "mrs", "ourselves", "hers", "between", "yourself", "but", "again", "there", "about",
              "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its",
              "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as",
              "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his",
              "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their",
              "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before",
              "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that",
              "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself",
              "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t",
              "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here",
              "than", "https://wwwgutenbergorg/////"]
black_list2 = ['œ', 'â', '€', ',', '.', '”', '?', '„', '¢']

file1 = open("Beyond the Wall of Sleep.txt", "r", errors='ignore')
file2 = open('Pride and Prejudice.txt', 'r', errors='ignore')

book1: str = file1.read().lower()
book2: str = file2.read().lower()

file1.close()
file2.close()

# remove empty lines
book1 = (' '.join([i for i in book1.split('\n') if len(i) > 0]))
book2 = (' '.join([i for i in book2.split('\n') if len(i) > 0]))

# remove numbers
book1 = (''.join([i for i in book1 if not i.isdigit()]))
book2 = (''.join([i for i in book2 if not i.isdigit()]))

# for punctuation
for word in black_list2:
    book1 = book1.replace(word, '')
    book2 = book2.replace(word, '')

# for commonly used words since replace cannot be used here
# (replacing 'he' would also mean replacing help (lp)))
book1 = ' '.join(filter(lambda x: x.lower() not in black_list, book1.split()))
book2 = ' '.join(filter(lambda x: x.lower() not in black_list, book2.split()))

list_book1 = set(book1.split(' '))
list_book2 = set(book2.split(' '))

intersection = list_book2.intersection(list_book1)
print(intersection)
print(len(intersection))
