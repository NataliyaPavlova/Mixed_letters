#!/usr/bin/python3

'''
The code reads text from a given file and write a file with the same text but with randomly mixed letters inside words
'''

import sys
import random
import re


def mix_letters(word):
    ''' Returns a word with mixed letters inside'''
    new_word=[]
    
    #feature: punctuation is in place - another split
    for wrd in re.split('([a-zA-Zа-яА-Я]+)', word):
        
        if not re.search('[a-zA-Zа-яА-Я]', wrd) or len(wrd)==1:
            new_word.append(wrd)
            continue
        
        #pool of available letters
        letters=[letter for letter in wrd[1:-1]]
    
        #pool of indicies of available letters
        indices=[i for i in range(len(letters))]
       
        #final word
        middle=wrd[0]
    
        #randomly choose a letter from pool, add it to the final word, remove letter's index from pool
        while indices:
            i = random.choice(indices)
            middle+=letters[i]
            indices.remove(i)     
        middle+=wrd[-1]
        new_word.append(middle)

    return ''.join(new_word)


def text(filename, result_filename):
    try:    
        with open(filename, newline=None) as f, open(result_filename,'w') as fw:
            for line in f:
                #read each line from file
                eol_flag=0
                if re.findall('\n',line): eol_flag=1
                
                list_of_words = line.split()
                
                #process it 
                new_list=[]
                for word in list_of_words:
                    new_list.append(mix_letters(word))
            
                #compile it back and write to another file
                new_line=' '.join(new_list) if eol_flag==0 else ' '.join(new_list)+'\n'
                fw.write(new_line)
    except IOError as e:
        print('Operation failed: {}'.format(e.strerror))


def main():
    if len(sys.argv)==1:
        filename='text.txt'
    else:
        filename = sys.argv[1]
    result_filename='mixed_'+filename
    text(filename, result_filename)
    print('You may find a result in {}'.format(result_filename))
    

if __name__=='__main__':
    main()


