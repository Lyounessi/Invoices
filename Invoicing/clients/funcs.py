def cNumbs(*args):
    '''
    Function to insert number in clients creation
    arg[0] = obj
    arg[1] = request
    '''
    numb = 0
    lastC = args[0].objects.filter(createdBy=args[1].user).order_by('-id')[:1]
    lastC = lastC[0]
    if lastC:
        if lastC.number:
            numb += int(lastC.number) 
    else : 
        numb = 1 

    return str(numb)