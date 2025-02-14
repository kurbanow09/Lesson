def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        
    line_count = len(lines)  
    words = [word for line in lines for word in line.split()]
    word_count = len(words) 
    longest_word = max(words, key=len, default="") 
    longest_word_length = len(longest_word) 

    return line_count, word_count, longest_word, longest_word_length

file_path = "Book.txt"  

line_count, word_count, longest_word, longest_word_length = analyze_text(file_path)

print(f"Setir sany: {line_count}")
print(f"Soz sany: {word_count}")
print(f"In uzyn sozi: {longest_word}")
print(f"Harp sany: {longest_word_length}")