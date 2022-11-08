import time

import pywikibot
from pywikibot \
    import pagegenerators

import data


class Frame:
    def __init__( self ):
        self.booted = False
        self.Site = None

    def __first_time( self ):
        if self.booted == False:
            self.booted = True
            self.Site = pywikibot.Site('commons:commons')

    def run( self ):
        self.__first_time()

        files = self.get_data_urls()

        for e in files:
            print('currently-selected:' + e)

            if not (e is None or e == ''):
                page = pywikibot.Page(self.get_site(), e)
                body = page.text

                if '{{Template:Designermadsen:source}}' in body:
                    #print('Nothing to do here')
                    pass
                else:
                    new = self.replace_author(body)
                    
                    page.text = new
                    page.save(summary='this edit is made by a boy: added template in author field.')

    def replace_author(self, text):
        in_information = False

        lines = str(text).splitlines()

        for idx in range(0, len(lines)):
            cl = lines[idx]
            cl_lower = cl.lower()

            if str('{{information') in cl_lower:
                in_information = True

            if str('}}') in cl_lower and not '|' in cl_lower and not '==' in cl_lower:
                in_information = False

            if in_information:
                if '|author=' in cl_lower:
                    lines[idx] = '|author={{Template:Designermadsen:source}}'


        newBody = ''
        for l in lines:
            newBody = newBody + l + '\r\n'

        return newBody



    def get_site( self ):
        return self.Site

    def set_site( self, v ):
        self.Site = v

    def get_data_urls(self):
        return  data.list.splitlines()