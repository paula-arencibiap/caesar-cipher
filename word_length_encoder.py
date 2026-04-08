def word_lenght_encoder(sentences, position):
    if not isinstance(sentences, list):
        return 'Argument must be a list.'
    if not isinstance(position, int):
        return 'Position must be an integer.'
    if position < 0:
        return 'Position must be 0 or greater.'
    code = ''
    for index,sentence in enumerate(sentences):
        words = sentence.split(' ')
        if len(words) > position:
            code += str(len(words[position]))
        else: 
            code += '0'
    return code 

sentence1 = 'The cat sat on the mat'
sentence2 = 'I love learning Python every day'
sentence3 = 'Hello world'
sentence4 = 'Go'

sentences = [sentence1, sentence2, sentence3, sentence4]

if __name__ == "__main__":
print(word_lenght_encoder(sentences,0))
