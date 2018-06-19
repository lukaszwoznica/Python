import re

pattern = re.compile(r'''
            ^                                      
            ([2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})     
            .                                      
            ([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})     
            .                                      
            ([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})   
            .                                      
            ([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})    
            $                                       
            ''', re.VERBOSE)


with open("plik.txt", "r") as f:
    for line in f:
        for match in pattern.finditer(line):
            print("IPv4: {}".format(match.string))

