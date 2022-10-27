import pywikibot


def main():
    Site = pywikibot.Site('commons:commons')
    page = pywikibot.Page(Site, 'User:Designermadsen')

    print(page.text)

if __name__ == '__main__':
    main()