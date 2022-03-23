import csv


def main():
    luoti = csv.DictReader(open('jasenet.csv', 'r'))

    newlist = []

    skip = False

    print(
    """
    Komennot:

     1   : pääsee kokoukseen
     2   : ei pääse kokoukseen
    skip : Ohita kysely, siirry suoraan osallistuja listaukseen
    """
    )

    for i in luoti:
        if not skip:        
            paikalla = input('Pääsee kokoukseen:')
        
        if paikalla == 'skip':
            skip = True
        
        if paikalla == '1' and not skip:
            i['paikalla'] = 'True'
        elif not skip:
            i['paikalla'] = 'False'
        newlist.append(i)

    print(
    """
    Kokoukseen osallistujat:
    """
    )

    md = 'Kokoukseen osallistujat:\n\n'

    osallistujat = {}

    for i in range(5):
        temp = newlist[i]
        if temp['paikalla'] == 'True':
            osallistujat[temp['Nimi']] = ''
            print(temp['Nimi'])
            md = md + str(temp['Nimi']) + '<br>'
        else:
            for j in range(5, len(newlist)):
                temp2 = newlist[j]
                if temp2['Nimi'] not in osallistujat.keys() and temp2['paikalla'] == 'True':
                    print(temp['Nimi'], 'este, tilalla', temp2['Nimi'])
                    md = md + str(temp['Nimi']) + ' este, tilalla ' + str(temp2['Nimi']) + '<br>'
                    osallistujat[temp2['Nimi']] = ''
                    break


    print(
    """
    Muut varat:
    """
    )

    md = md  + '\n\n' + 'Muut varat:\n\n'

    for i in newlist:
        if i['Nimi'] not in osallistujat.keys() and i['paikalla'] == 'True':
            print(i['Nimi'])
            md = md + str(i['Nimi']) + '<br>'

    writer = csv.DictWriter(open('jasenet.csv', 'w'), fieldnames=newlist[0].keys())
    writer.writeheader()
    writer.writerows(newlist)

    with open('README.md', 'w') as mdFile:
        mdFile.write(md)

if __name__ == '__main__':
    main()