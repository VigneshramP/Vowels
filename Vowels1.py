import argparse
def ArgParser(): 
    # Argument Passing Process 
    parser = argparse.ArgumentParser(description = 'Vowels Operation')
    parser.add_argument('path', help = 'Name or Path of file')
    args = parser.parse_args()
    return args
def Check_Vowels(string, vowels):
    #Check Voowls in this Function
    LowerString=string.lower() #Capital All Are Converted into Lower Cases
    count = {}.fromkeys(vowels, 0) # Value INItialize Process
    for character in LowerString: 
        if character in count: 
            count[character] += 1    
    return count 
def main():
    Args = ArgParser() #Function Calling Process
    fileName = Args.path
    Document_Open =open(fileName,"r")
    List_Convert = list(Document_Open) # The opened File is Converted into List
    String= str(List_Convert) #All Letters are Converted into String 
    Vowels = ['a','e','i','o','u' ]
    print (Check_Vowels(String, Vowels)) #Function Calling Process
if __name__ == '__main__':
    main()
