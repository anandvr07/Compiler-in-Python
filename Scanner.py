import re

# Reading the input file from the path given. In this case, the input file is in the same folder as the program.
FileRead = open("InputProgram.txt", 'r')
FileStream = FileRead.read()


def gettoken(InputStream):
    # This method accepts the Input file stream as an argument and gives out the corresponding token type for every
    # word, number or an operator.

    # Parsing the input stream using regular expressions and removing the extra spaces and line breaks using the
    # lambda function.
    StringParse = filter(None, re.split("([ ]|[.]|[:]|[\[]|[\]]|[;]|[,]|[()]|[\n]|[:]=|[=]|[<>]=|[<]|[>]|[{]|[}]|[%]|[+]|[-]|[!]|[%]|[*]|[/])", InputStream))
    SpaceParse = filter(lambda a: a != " ", StringParse)
    LineParse = filter(lambda a: a != "\n", SpaceParse)

    WordList = []
    NumList = []
    OpList = []

    # Finding out the type of token for every item in the delimited list and printing the type of the token along with
    # list item. Storing the list items in their corresponding token type lists, for adding to the symbol table in the
    # future.
    for every_item in LineParse:
        if every_item[0].isalpha():
            WordList.append(every_item)
            if len(every_item) < 4:
                    print "%s" % every_item + "\t\t\t\ttokword"
            elif len(every_item) > 7:
                    print "%s" % every_item + "\t\ttokword"
            else:
                    print "%s" % every_item + "\t\t\ttokword"
        elif every_item[0].isdigit():
            NumList.append(every_item)
            if len(every_item) < 4:
                    print "%s" % every_item + "\t\t\t\ttoknumber"
            elif len(every_item) > 7:
                    print "%s" % every_item + "\t\ttoknumber"
            else:
                    print "%s" % every_item + "\t\t\ttoknumber"
        else:
            OpList.append(every_item)
            if len(every_item) < 4:
                    print "%s" % every_item + "\t\t\t\ttokop"
            elif len(every_item) > 7:
                    print "%s" % every_item + "\t\ttokop"
            else:
                    print "%s" % every_item + "\t\t\ttokop"

    return

# Calling the gettoken() method to tokenise the input file stream, which is passed as a parameter to the gettoken()
# method.
gettoken(FileStream)





