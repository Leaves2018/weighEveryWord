def update_vocabulary_words(new_words):
    with open("vocabulary_words.txt", 'a+') as vw:
        for i in range(len(new_words)):
            vw.write('\n' + new_words[i].to_string())


def update_familiar_words(old_words):
    with open("familiar_words.txt", 'a+') as fw:
        for i in range(len(old_words)):
            fw.write('\n' + old_words[i].to_string())
