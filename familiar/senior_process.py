import re

with open('gaozhong.txt') as gz:
    gk = open('gaokao.txt', 'w+')
    for line in gz.readlines():
        if not re.match('[a-zA-Z]', line[0]):
            continue
        word = re.split('[)( 0-9]+', line.strip())
        # new_word = Word(word, en_mean(word), ch_mean(word))
        gk.write(word[0]+'\n')
    gk.close()
