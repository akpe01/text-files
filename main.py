# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename, "r")
    data= file.read()
    return data


def count_words():
    text = read_file_content("./story.txt")
    file_content =text.split()
    count_words={word:file_content.count(word) for word in file_content}
      
    return count_words
print(count_words())
    
    
    
    