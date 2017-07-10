# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:55:20 2017

@author: Vandana Bagla
"""

#morse code translator

morse_code_dict={
'A':'.-',
'B':'-...',
'C':'-.-.', 
'D':'-..',
'E':'.',
'F':'..-.', 
'G':'--.', 
'H':'....',
'I':'..', 
'J':'.---',
'K':'-.-',
'L':'.-..', 
'M':'--', 
'N':'-.',
'O':'---', 
'P':'.--.', 
'Q':'--.-',
'R':'.-.', 
'S':'...', 
'T':'-',
'U':'..-', 
'V':'...-', 
'W':'.--',
'X':'-..-', 
'Y':'-.--', 
'Z':'--..',
'1':'.----', 
'2':'..---', 
'3':'...--',
'4':'....-', 
'5':'.....', 
'6':'-....',
'7':'--...', 
'8':'---..', 
'9':'----.',
'0':'-----', 
', ':'--..--', 
'.':'.-.-.-',
'?':'..--..', 
'/':'-..-.', 
'-':'-....-',
'(':'-.--.', 
')':'-.--.-'
}

#encryption for single word
message="GEEKS-FOR-GEEKS GEEKS-FOR-GEEKS" 
result=''
for letter in message:
    print(letter)
    if letter!=' ':
        result=result+morse_code_dict[letter]+' '
    else:
         result=result+'  '
print(result)

message="--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ...   --. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
result=''
c=''
for i in range(len(message)):
   
    if(message[i]==' '):
        if((i+1)!=len(message) and message[i+1]==' '):
            if(c!=''):
               for k,v in morse_code_dict.iteritems():
                   if(v==c):
                       result=result+k; 
               result=result+' '
            i=i+1
            c=''                    
        else:
            for k,v in morse_code_dict.iteritems():
                if(v==c):
                    result=result+k;
    
            c=''
    else:
        c=c+message[i]
print(result)


