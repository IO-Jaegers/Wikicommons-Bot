import pywikibot


def main():
    Site = pywikibot.Site('commons:commons')
    page = pywikibot.Page(Site, 'File:JerneSorgn-144908.jpg')
    page.text = page.text.replace('|author=[[User:Designermadsen|Kent Vejrup Madsen]]', '|author={{Designermadsen:source}}')
    page.save("test - Replacing author with template instead")


if __name__ == '__main__':
    main()