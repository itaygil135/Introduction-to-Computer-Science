import hangman_helper


def new_short_list(listt):
    short_list = []
    n = len(listt)
    for i in range(hangman_helper.HINT_LENGTH):
        short_list.append(listt[(n*i)//hangman_helper.HINT_LENGTH])

    return short_list




def filter_words_list(words, pattern, wrong_guess_lst):
    update_list = []
    for word in words:
        flag = False
        if len(word) != len(pattern):
            continue
        for letter in wrong_guess_lst:
            if letter in word:
                flag = True
                break
        if flag == True:
            continue
        for i in range(len(word)):
            if pattern[i] != '-' and pattern[i] != word[i]:
                flag = True
                break
            if word[i] in pattern and word[i] != pattern[i]:
                flag = True
                break
        if flag == True:
            continue


        update_list.append(word)
    return update_list











def update_word_pattern(word, pattern, letter):
    update_pattern = ''
    for i in range(len(pattern)):
        if word[i] == letter:
            update_pattern = update_pattern + letter
        else:
            update_pattern = update_pattern + pattern[i]

    return update_pattern




def is_letter_valid_or_chosed(letter,wrong_guss,patternn):
    list_of_alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                    'o','p','q','r','s','t','u','v','w','x','y','z']
    if len(letter)>1:
        return "the letter you typed is not valid"
    elif not letter in list_of_alpa:
        return 'the letter you typed is not valid'
    elif letter in wrong_guss or  letter in patternn:
        return "the letter you choose already been chosen "
    else:
        return "let's play"


def function_for_letter(word,pattern,letter,wrong_guss_list):
    counter = 0
    if letter in word:
        pattern = update_word_pattern(word, pattern, letter)
        for i in word:
            if i == letter:
                counter = counter+1
    else:
        wrong_guss_list.append(letter)
    return pattern,wrong_guss_list,counter


def function_for_word(word,pattern,gussed_word):
    counter = 0
    if gussed_word == word:
        for i in range(len(word)):
            if word[i] != pattern[i]:
                counter =  counter +1
        pattern = word
    return (pattern,counter)









def run_single_game(word_lst,score):
    word = hangman_helper.get_random_word(word_lst)
    wrong_guss_lst = []
    pattern =  len(word) * "-"
    msg = "let's play"
    while score > 0 and pattern != word:
        hangman_helper.display_state(pattern,wrong_guss_lst,score,msg)
        tuple = hangman_helper.get_input()
        if tuple[0] == hangman_helper.LETTER:
            msg = is_letter_valid_or_chosed(tuple[1],wrong_guss_lst,pattern)
            if msg == "let's play":
                score = score -1
                pattern,wrong_guss_lst, n =\
                    function_for_letter(word,pattern,tuple[1],wrong_guss_lst)
                score = score + n*(n+1)//2
        if tuple[0] == hangman_helper.WORD:
            score = score -1
            pattern,n = function_for_word(word,pattern,tuple[1])
            if n == 0:
                msg = "wrong word"
            else:
                msg = "well done, you gussed the word"
                score = score + n*(n+1)//2
        if tuple[0] == hangman_helper.HINT:
            msg = "here is your hint"
            up_list = filter_words_list(word_lst,pattern, wrong_guss_lst)
            print(up_list)
            if len(up_list) > hangman_helper.HINT_LENGTH:
                hangman_helper.show_suggestions(new_short_list(up_list))
            score = score - 1

    if score > 0:
        msg = "you won and discoverd succecfully the word"
    else:
        msg = "you lost, the word is " + str(word)
    hangman_helper.display_state(pattern, wrong_guss_lst, score, msg)

    return score



































if __name__ == "__main__":
    word_list = hangman_helper.load_words()
    update_score = 10
    num_of_games = 0
    another_game = True
    while another_game == True:
        update_score = run_single_game(word_list,update_score)
        num_of_games = num_of_games+1
        if update_score > 0:
            msg = "you played and won "+str(num_of_games)+" games and gain a "\
                  +str(update_score)+" points. " \
                    "would you like to start a new game?"
            another_game = hangman_helper.play_again(msg)
            if another_game == True:
                continue
            else:
                break
        else:
            msg="you survived as " +str(num_of_games)+" games till you lost."\
                  " would you like to start a new seshones of games?"
            another_game = hangman_helper.play_again(msg)
            if another_game == True:
                num_of_games = 0
                update_score = 10
                continue
            else:
                break



































