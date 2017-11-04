#!/usr/bin/python
import sys
varValue = {}
varType = {}
pos = 0

def prog():
    while nextToken[pos] == 'let':
        let_in_end()
        varValue.clear()
        varType.clear()

def let_in_end():
    match('let')
    decl()
    match('in')
    varType = nextToken[pos]
    match(nextToken[pos])
    match('(')
    value = expr(varType)
    match(')')
    match('end')
    match(';')
    print value

def decl():
    if nextToken[pos] != 'in':
        i = nextToken[pos] #variable name
        lex()
        match(':')
        varType[i] = nextToken[pos]
        match(nextToken[pos])
        match('=')
        varValue[i] = expr(varType[i])
        match(';')
        decl()

def expr(t):
    opp = term(t)
    while nextToken[pos] == '+' or nextToken[pos] == '-':
        if nextToken[pos] == '+':
            match(nextToken[pos])
            opp += term(t)
        elif nextToken[pos] == '-':
            match(nextToken[pos])
            opp -= term(t)
    return opp

def term(t):
    opp = factor(t)
    while nextToken[pos] == '*' or nextToken[pos] == '/':
        if nextToken[pos] == '*':
            match(nextToken[pos])
            opp *= factor(t)
        elif nextToken[pos] == '/':
            match(nextToken[pos])
            try:
                opp /= factor(t)
            except ZeroDivisionError:
                error()
    return opp

def factor(t):
    if nextToken[pos] == '(':
        match(nextToken[pos])
        value = expr(t)
        match(')')
    elif (t == 'real' and '.' in nextToken[pos]): #float
        try:
            value = float(nextToken[pos])
        except ValueError:
            error()
        lex()
    elif (t == 'int' and nextToken[pos].isdigit()): #int
        value = int(nextToken[pos])
        lex()
    elif nextToken[pos] in varValue and t == varType[nextToken[pos]]:
        value = varValue[nextToken[pos]]
        lex()
    elif nextToken[pos] == 'int' or nextToken[pos] == 'real':
        typeHolder = nextToken[pos]
        match(nextToken[pos])
        match('(')
        try:
            if typeHolder == 'int':
                value = int(varValue[nextToken[pos]])
            else:
                value = float(varValue[nextToken[pos]])
        except KeyError:
                error()
        lex()
        match(')')
    else:
        error()
    return value

def match(passedToken):
    if nextToken[pos] != passedToken:
        error()
    lex()

def error():
    print "Error"
    exit(1)

def lex():
    global pos
    pos += 1
    if pos == len(nextToken):
        nextToken.append(None)

#userfile = raw_input("Enter a file\n")
#readfile = open(userfile, 'r')
nextToken = []
readfile = open(sys.argv[1], 'r')
for commands in readfile.read().lower().split():
    nextToken.append(commands)

readfile.close()
prog()