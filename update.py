def update_vocabulary_words(new_words):
    with open("vocabulary/vocabulary_words.txt", 'a+') as vw:
        for i in range(len(new_words)):
            word = new_words[i]
            vw.write('\n' + word.to_string())


def update_familiar_words(old_words):
    with open("familiar/familiar_words.txt", 'a+') as fw:
        for i in range(len(old_words)):
            word = old_words[i]
            fw.write('\n' + word.to_string())
