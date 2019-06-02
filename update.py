def update_vocabulary_words(new_words):
    with open("vocabulary/vocabulary_words.txt", 'a+') as vw:
        for word in new_words:
            vw.write("\n" + word.to_string())


def update_familiar_words(old_words):
    with open("familiar/familiar_words.txt", 'a+') as fw:
        for word in old_words:
            fw.write("\n" + word.get_name())
