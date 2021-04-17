def formatTitle(title):
    title = title.replace(' ','_').split(',')
    output = ''
    if len(title) > 0:
        output += title[0]
    if len(title) > 1:
        output += f',tag={title[1]}'
    if len(title) > 2:
        output += f',subtag={title[2]}'
    return output
