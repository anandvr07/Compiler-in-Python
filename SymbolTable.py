#Author - Anand Vijayaragavan Ravikumar               Net ID - avr286

import re



# Reading the input file from the path given. In this case, the input file is in the same folder as the program.
FileRead = open("InputProgram.txt", 'r')
FileStream = FileRead.read()

def removeComments(string):
    #This method removes the comments from the input program. Comments in PASCAL start with { and end with }.

    string = re.sub(re.compile("{.*?}",re.DOTALL ) ,"" ,string)
    return string


def splitting(InputStream):
    # Parsing the input stream using regular expressions and removing the extra spaces and line breaks using the
    # lambda function.

    StringParse = filter(None,re.split("([ ]|[0-9]*[.][0-9]*[Ee]*[+-]*[0-9]*|[.]|[:]|[\[]|[\]]|[;]|[,]|[()]|"
                  "[\n]|[:]=|[=]|[<>]=|[<]|[>]|[{]|[}]|[%]|[+]|[-]|[!]|[%]|[*]|[/])", InputStream))
    SpaceParse = filter(lambda a: a != " ", StringParse)
    LineParse = filter(lambda a: a != "\n", SpaceParse)
    return LineParse


def gettoken(InputStream):
    # This method creates a symbol table and populates it with lexemes and their types. This method also accepts the
    # Input file stream as an argument and appends the lexemes of the file stream to the symbol table. It also
    # displays the type of token for every token in the input stream.

    # Dictionaries in Python are key-value pairs, similar to Hash tables in JAVA/C#. Infact, Python dictionaries are
    # implemented internally as open hashing based on a primitive polynomial over Z/2.

    # Creating 3 dictionaries - One each for Keywords, Operators and Identifiers. Here, Caseless Dictionaries are
    # created to avoid the case sensitivity issue while scanning the lexemes. The Caseless Dictionary class is defined
    # below.

    dict1 = CaselessDictionary()
    dict2 = CaselessDictionary()
    dict3 = CaselessDictionary()

    # Populating the dictionaries with keywords and operators of the PASCAL language.
    dict1['PROGRAM'] = 'TokProgram'
    dict1['if'] = 'TokIf'
    dict1['then'] = 'TokThen'
    dict1['var'] = 'TokVar'
    dict1['array'] = 'TokArray'
    dict1['of'] = 'TokOf'
    dict1['declare'] = 'TokDeclare'
    dict1['endif'] = 'TokEndIf'
    dict1['endwhile'] = 'TokEndWhile'
    dict1['enduntil'] = 'TokEndUntil'
    dict1['read'] = 'TokRead'
    dict1['write'] = 'TokWrite'
    dict1['set'] = 'TokSet'
    dict1['integer'] = 'TokInteger'
    dict1['real'] = 'TokReal'
    dict1['function'] = 'TokFunction'
    dict1['procedure'] = 'TokProcedure'
    dict1['BEGIN'] = 'TokBegin'
    dict1['END'] = 'TokEnd'
    dict1['else'] = 'TokElse'
    dict1['while'] = 'TokWhile'
    dict1['do'] = 'TokDo'
    dict1['CONST'] = 'TokConstant'


    dict2['.'] = 'TokPeriod'
    dict2[','] = 'TokComma'
    dict2['='] = 'TokEquals'
    dict2['>='] = 'TokGE'
    dict2['<='] = 'TokLE'
    dict2['>'] = 'TokGT'
    dict2['<'] = 'TokLT'
    dict2[':='] = 'TokAssignment'
    dict2['!'] = 'TokNE'
    dict2['+'] = 'TokAdd'
    dict2['-'] = 'TokSub'
    dict2['*'] = 'TokMul'
    dict2['/'] = 'TokDiv'
    dict2['['] = 'TokOpenBracket'
    dict2[']'] = 'TokCloseBracket'
    dict2['('] = 'TokOpenParan'
    dict2[')'] = 'TokCloseParan'
    dict2[':'] = 'TokColon'
    dict2[';'] = 'TokSemicolon'
    dict2['%'] = 'TokModulo'


    # Finding out the type of token for every item in the delimited list and printing the type of the token along with
    # list item. Storing the Identifiers in the Identifier Dictionary.
    for every_item in InputStream:
        if every_item[0].isdigit():
            print "%s" % every_item + "\t\t\t\tTokNumber"

        elif dict1.has_key(every_item) or dict2.has_key(every_item):
            if len(every_item) < 4:
                    print "%s" % every_item + "\t\t\t\t" + "%s" % (dict1.get(every_item) or dict2.get(every_item))
            elif len(every_item) > 7:
                    print "%s" % every_item + "\t\t" + "%s" % (dict1.get(every_item) or dict2.get(every_item))
            else:
                    print "%s" % every_item + "\t\t\t" + "%s" % (dict1.get(every_item) or dict2.get(every_item))
        else :
            dict3[every_item] = 'TokIdentifier'
            if len(every_item) < 4:
                    print "%s" % every_item + "\t\t\t\t" + "%s" % (dict3.get(every_item))
            elif len(every_item) > 7:
                    print "%s" % every_item + "\t\t" + "%s" % (dict3.get(every_item))
            else:
                    print "%s" % every_item + "\t\t\t" + "%s" % (dict3.get(every_item))

    return

class CaselessDictionary(dict):
    # Dictionary that enables case insensitive searching while preserving case sensitivity when keys are listed,
    # ie, via keys() or items() methods. Works by storing a lowercase version of the key as the new key and stores
    # the original key-value pair as the key's value (values become dictionaries).

    def __init__(self, initval={}):
        if isinstance(initval, dict):
            for key, value in initval.iteritems():
                self.__setitem__(key, value)
        elif isinstance(initval, list):
            for (key, value) in initval:
                self.__setitem__(key, value)

    def __contains__(self, key):
        return dict.__contains__(self, key.lower())

    def __getitem__(self, key):
        return dict.__getitem__(self, key.lower())['val']

    def __setitem__(self, key, value):
        return dict.__setitem__(self, key.lower(), {'key': key, 'val': value})

    def get(self, key, default=None):
        try:
            v = dict.__getitem__(self, key.lower())
        except KeyError:
            return default
        else:
            return v['val']

    def has_key(self,key):
        if self.get(key):
            return True
        else:
            return False

    def items(self):
        return [(v['key'], v['val']) for v in dict.itervalues(self)]

    def keys(self):
        return [v['key'] for v in dict.itervalues(self)]

    def values(self):
        return [v['val'] for v in dict.itervalues(self)]

    def iteritems(self):
        for v in dict.itervalues(self):
            yield v['key'], v['val']

    def iterkeys(self):
        for v in dict.itervalues(self):
            yield v['key']

    def itervalues(self):
        for v in dict.itervalues(self):
            yield v['val']


# Calling the removeComments() method to remove the comments present in the Input File Stream.
NoCommentFileStream = removeComments(FileStream)

# Calling the splitting() method to split the input file stream into lexemes.
Words = splitting(NoCommentFileStream)

# Calling the gettoken() method to tokenise the input file stream, which is passed as a parameter to the gettoken()
# method.
gettoken(Words)





