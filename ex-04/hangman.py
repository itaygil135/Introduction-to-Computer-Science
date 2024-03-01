import hangman_helper
import copy


def is_wrong_guess_in_word(wrong_guess_lst, word):
    """
    This function verify the word suggested to be included in the hint list
    does not contains any known wrong guess
    :param wrong_guess_lst: list of wrong guesses done by the user
    :param word:  word to be considered as word in hint list
    :return:
    True  - in case the word FAILED to meet the requirement of not including
            a known wrong guess.
    False - in case the word did not failed to meet the requirement of not
            including a known wrong guess.
    """
    for letter in wrong_guess_lst:
        if letter in word:
            return True
    return False


def is_mismatch_index(word, pattern):
    """
    This function scan all indexes at the word and  in case index i at the
    pattern was exposed, verify the word has the same letter at the same index
    :param word: word to be considered as word in hint list
    :param pattern: pattern includes the correct guessed letters till know
    :return:
    True: in case the word FAILED to meet the requirement of same index
    False: in case the word did not failed to meet the requirement of same
           index
    """
    for i in range(len(word)):
        if pattern[i] != '_' and pattern[i] != word[i]:
            return True
    return False


def is_mismatch_letter_appearance(word, pattern):
    """
    This function scan all indexes at the word and in case the letter at word,
    at index i, was exposed at the pattern, verify all appearance of the
    letter were exposed correctly.
    :param word: word to be considered as word in hint list
    :param pattern: pattern includes the correct guessed letters till know
    :return:
    True  - in case the word FAILED to meet the 'same appearance' requirement
    False - in case the word did not failed to meet the 'same appearance'
            requirement
    """
    for i in range(len(word)):
        if word[i] in pattern and word[i] != pattern[i]:
            return True
    return False


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This function scan all words used at the game and create as sub-list of
    words that can be used as a hint list of words for the user, based on
    the letters the user already exposed.
    :param words: List of all words used at the game
    :param pattern: pattern includes the correct guessed letters till know
    :param wrong_guess_lst: list of wrong guesses done by the user
    :return:
    List of words that can be used as hint list. The returned list
    is a sub-list of all words used at the game.
    """
    full_hint_list = []
    for word in words:
        if len(word) != len(pattern):
            continue
        if is_wrong_guess_in_word(copy.copy(wrong_guess_lst), word):
            continue
        if is_mismatch_index(copy.copy(word), copy.copy(pattern)):
            continue
        if is_mismatch_letter_appearance(copy.copy(word), copy.copy(pattern)):
            continue
        full_hint_list.append(word)
    return full_hint_list


def get_short_hint_list(hint_list):
    """
    This function select n (n = HINT_LENGTH) words from the hint list of words
    and create a shorter hint list
    :param hint_list: List of all words that can be used as hint list for the
                    user
    :return:
    A short sub-list of the hint list
    """
    short_hint_list = []
    n = len(hint_list)
    for i in range(hangman_helper.HINT_LENGTH):
        short_hint_list.append(hint_list[(n*i)//hangman_helper.HINT_LENGTH])
    return short_hint_list


def update_word_pattern(word, pattern, letter):
    """
    This function create an updated pattern based on a given pattern and a
    given word. the updated pattern will expose the new letter on top of all
    other letters exposed at the given pattern
    :param word:     the hidden word that the user should guess
    :param pattern:  pattern includes the correct guessed letters till know
    :param letter:   correct letter that was just guessed
    :return:
    updated_pattern - update pattern that include the previous pattern,
                      updated with the new letter that was just guessed.
    """
    updated_pattern = ''
    for i in range(len(pattern)):
        if word[i] == letter:
            updated_pattern = updated_pattern + letter
        else:
            updated_pattern = updated_pattern + pattern[i]

    return updated_pattern


def is_valid_letter(letter, wrong_guess, pattern):
    """
    This function validate that a letter meets the following requirements:
    1) it is a lower case letter
    2) it was not selected before (i.e. it does not appear at the pattern nor
       at the list of wrong guess)
    3) it is a single character
    :param letter: a character typed by the user
    :param wrong_guess: list of wrong guesses done by the user
    :param pattern: pattern includes the correct guessed letters till know
    :return:
    True  - in case the letter is valid and new
    False - in case the letter is invalid or was typed before
    """
    list_of_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']
    if len(letter) > 1:
        return False, "you typed more than one character"
    elif letter not in list_of_alpha:
        return False, 'the character you typed is not a lower case letter'
    elif letter in wrong_guess or letter in pattern:
        return False, "the letter you choose already had been chosen."
    else:
        return True, "let's play"


def handle_valid_letter_guess(word, pattern, letter, wrong_guess_list):
    """
    This function handle the case the user typed a new valid letter.
    The function:
    1) in case the letter appears at the hidden word, update the patter by
       calling update_word_pattern
    2) in case the letter does not appear at the hidden word, update the list
       of wrong guesses.
    3) count the number of the letter appearance in the hidden word.
    :param word: the hidden word that the user should guess
    :param pattern: pattern includes the correct guessed letters till know
    :param letter: the letter typed by the user
    :param wrong_guess_list: list of wrong guesses done by the user
    :return:
    1) the updated pattern
    2) the updated list of wrong guesses
    3) the number of the letter appearance in the hidden word
    """
    counter = 0      # assuming the letter does not appear in the hidden word.
    if letter in word:
        pattern = update_word_pattern(word, pattern, letter)
        # count the number the letter appears in the word
        for i in word:
            if i == letter:
                counter = counter + 1
    else:
        wrong_guess_list.append(letter)
    return pattern, wrong_guess_list, counter


def handle_letter_selection(word, pattern, letter, wrong_guess_list, score):
    """
    This function handle the case the user select to typed a letter.
    The function:
    1) check if the letter is valid or not
    2) check if the letter appears at the selected word, and based on that:
        2.1) update the user score
        2.2) update the pattern, if required,
        2.3) update the list of wrong guesses, if required.
    :param word: the hidden word that the user should guess
    :param pattern: pattern includes the correct guessed letters till know
    :param letter: the character typed by the user
    :param wrong_guess_list: list of wrong guesses done by the user
    :param score: current user's score
    :return:
    score   - the updated user's score
    msg     - the message to be displayed on the screed
    """
    valid_letter, msg = is_valid_letter(letter,
                                        copy.copy(wrong_guess_list),
                                        copy.copy(pattern))
    if valid_letter:
        score = score - 1
        pattern, wrong_guess_list, n = \
            handle_valid_letter_guess(word,
                                      pattern,
                                      letter,
                                      wrong_guess_list)
        score = score + n * (n + 1) // 2
    return score, msg , pattern


def is_valid_word(guessed_word):
    list_of_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']

    for letter in guessed_word:
        if letter not in list_of_alpha:
            return False
    return True

def handle_word_selection(word, pattern, guessed_word, score):
    """
    This function handle the case the user guessed a word. The function
    calculate the update user's score, update the patter in case the hidden
    hidden word was guessed, and set a proper message to be displayed
    :param word: the hidden word that the user should guess
    :param pattern: pattern includes the correct guessed letters till know
    :param guessed_word: word guessed by the user
    :param score: current user's score
    :return:
    score   - the updated user's score
    msg     - the message to be displayed
    """
    if not is_valid_word(guessed_word):
        msg = 'the word you typed includes invalid charecter'
    elif guessed_word == word:
        score = score - 1
        counter = 0
        for i in range(len(word)):
            if word[i] != pattern[i]:
                counter = counter + 1
        score = score + counter * (counter + 1) // 2
        pattern = word
        msg = "well done, you guessed the word"
    else:
        score = score - 1
        msg = "wrong word"
    return score, msg , pattern


def handle_hint_selection(word_lst, pattern , wrong_guess_list, score):
    """
    This function create a list of words that can be used as hint list.
    The size of the list is limited to HINT_LENGTH
    :param word_lst: list of all words used at the game
    :param pattern: pattern includes the correct guessed letters till know
    :param wrong_guess_list: list of wrong guesses done by the user
    :param score: current user's score
    :return:
    msg: message to be displayed to the user
    score: user's updated score
    """
    msg = "here is your hint"
    score = score - 1
    hint_list = filter_words_list(copy.copy(word_lst),
                                  copy.copy(pattern),
                                  copy.copy(wrong_guess_list))
    if len(hint_list) > hangman_helper.HINT_LENGTH:
        hangman_helper.show_suggestions(get_short_hint_list(hint_list))
    else:
        hangman_helper.show_suggestions(hint_list)
    return score, msg


def run_single_game(word_lst, score):
    """
    This function run a single game of "hangman" and update the user's score
    based on this specific game results
    :param word_lst: List of all words used at this game
    :param score: current user's score
    :return:
    score: update user's score
    """
    word = hangman_helper.get_random_word(word_lst)
    wrong_guess_list = []
    pattern = len(word) * "_"
    msg = "let's play"
    while score > 0 and pattern != word:
        hangman_helper.display_state(pattern,
                                     wrong_guess_list,
                                     score, msg)
        user_choice = hangman_helper.get_input()
        if user_choice[0] == hangman_helper.LETTER:
            score, msg, pattern \
                = handle_letter_selection(word,
                                         pattern,
                                         user_choice[1],
                                         wrong_guess_list,
                                         score)
        if user_choice[0] == hangman_helper.WORD:
            score, msg , pattern = handle_word_selection (word,
                                                          pattern,
                                                          user_choice[1],
                                                          score)
        if user_choice[0] == hangman_helper.HINT:
            score, msg = handle_hint_selection(copy.copy(word_lst),
                                               copy.copy(pattern),
                                               copy.copy(wrong_guess_list),
                                               score)
    if score > 0:
        msg = "you won and discovered successfully the word"
    else:
        msg = "you lost, the word is " + str(word)
    hangman_helper.display_state(pattern, wrong_guess_list, score, msg)

    return score


def main():
    """
    This function run sessions of "hangman" games
cf    :return: None
    """
    word_list = hangman_helper.load_words()
    score = hangman_helper.POINTS_INITIAL
    num_of_games = 0
    another_game = True
    while another_game:
        score = run_single_game(word_list, score)
        num_of_games = num_of_games + 1
        if score > 0:
            msg = "you played and won " + str(num_of_games) +               \
                  " games and gain a " + str(score) +                       \
                  " points. would you like to start a new game?"
            another_game = hangman_helper.play_again(msg)
            if another_game:
                continue
            else:
                break
        else:
            msg = "you survived as " + str(num_of_games) +                  \
                  " games till you lost."                                   \
                  " would you like to start a new session of games?"
            another_game = hangman_helper.play_again(msg)
            if another_game:
                num_of_games = 0
                score = hangman_helper.POINTS_INITIAL
                continue
            else:
                break

if __name__ == "__main__":
    main()