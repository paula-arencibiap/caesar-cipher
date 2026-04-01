def pin_extractor(poems):
    '''Extracts a secret code from each poem in a list and returns all codes as a list.'''
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n') 
        
        for line_index,line in enumerate(lines):
            words = line.split() 
            if len(words) > line_index:
               secret_code += str(len(words[line_index])) 
            else:
                secret_code += '0'    
        secret_codes.append(secret_code) 
    return secret_codes

poem1 = 'Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night'

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem1,poem2,poem3]))
