import sys
import os.path


DELIMETER = ','

def get_list_from_file(list_name,file_name):
    #TODO hundle the case the input fileis not exice
    #TODO if os.path.exists(filename)
    with open(file_name, 'r') as f:
        for line in f:
            list_name.append(line[0:len(line) - 1])
        f.close()

def str_to_list(string):
    lst_string = []
    for char in string:
        if char != DELIMETER:
            lst_string.append(char)
    return lst_string


def read_matrix(mat_filename):
    mat = []
    row_list = []
    get_list_from_file(row_list,mat_filename)
    for row in row_list:
        mat.append(str_to_list(row))
    return mat

def find_words(word_list,matrix,directions):
    output_list = [("dog",1),("cat",2)]
    return output_list

def write_output(results,filename):
   #TODO make sure the order of the words in  file is the same with fun order
    with open(filename, 'w') as f:
        for item in results:
            f.write(item[0] + DELIMETER + str(item[1]))
            f.write("\n")
        f.close()  # TODO cheking if works withot close

def read_wordlist(word_lst_filename):
    words = []
    get_list_from_file(words, word_lst_filename)
    return words



def main():
    #TODO verify there are four args in the input
    word_lst_filename = sys.argv[1]
    mat_filename = sys.argv[2]
    output_filename = sys.argv[3]
    directions_str = sys.argv[4]

    #TODO all argumenus has value, the direction_str contains only valid char
    #TODO idnore a valid letter which appear more than one in directions_str

    look_for_word_lst = read_wordlist(word_lst_filename)
    #TODO hundle the case the input fileis not exice
    mat = read_matrix(mat_filename)
    #TODO hundle the case the input fileis not exice


    output_list = find_words(look_for_word_lst,mat,directions_str)

    write_output(output_list,output_filename)





if __name__=="__main__":
    main()

