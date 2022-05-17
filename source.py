import requests
import xml.etree.ElementTree as ET
from utils import *

# This file contains Source class

# ADD: API Keys: GOOGLE_API_KEY, IEEE_API_KEY, SCOPUS_API_KEY

ARXIV_URL = 'http://export.arxiv.org/api/query?search_query='
CROSSREF_API_URL = 'https://api.crossref.org/works?query='
DOAJ_URL = 'https://doaj.org/api/search/'
EMC_QUERY_URL = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='
GOOG_SCHOLAR_URL = 'https://serpapi.com/search.json?engine=google_scholar&q='
GOOGLE_API_KEY = ''
HAL_URL = 'http://api.archives-ouvertes.fr/search/?q='
IEEE_QUERY_URL = 'https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext='
IEEE_API_KEY = ''
OPENALEX_QUERY_URL = 'https://api.openalex.org/works?search='
SCOPUS_API_KEY = ''
SCOPUS_QUERY_URL = 'https://api.elsevier.com/content/search/scopus?query='
SEM_SCHOLAR_QUERY_URL = 'https://api.semanticscholar.org/graph/v1/paper/search?query='


class source(object):
    """
    Initializes source object. Each method under this class calls the respective source.

    """

    def __init__(self, term, author_name, affiliation_name):
        # initialize table name, schema and load data
        self.author_keyword = author_name
        self.affiliation_keyword = affiliation_name
        self.query_keyword = term

    def arxiv(self):

        title_attrib = 'title'
        author_attrib = 'author'
        year_attrib = 'published'
        venue_attrib = 'journal_ref'

        arxiv_pubs = []
        if self.query_keyword != '':
            response = requests.get(ARXIV_URL + self.query_keyword)
            res_xml = response.text
            tree = ET.fromstring(res_xml)
            arxiv_pubs.extend(extract_arxiv_xml(tree, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.author_keyword != '':
            response = requests.get(ARXIV_URL + self.author_keyword)
            res_xml = response.text
            tree = ET.fromstring(res_xml)
            arxiv_pubs.extend(extract_arxiv_xml(tree, title_attrib, author_attrib, year_attrib, venue_attrib))

        return arxiv_pubs

    def crossref_works(self):

        crossref_works_pubs = []

        if self.query_keyword != '':
            res = requests.get(CROSSREF_API_URL + self.query_keyword).json()
            res_list = res['message']['items']
            l = len(res_list)
            crossref_works_pubs.extend(extract_crossref(res_list, l))

        if self.author_keyword != '':
            res = requests.get(CROSSREF_API_URL + self.author_keyword).json()
            res_list = res['message']['items']
            l = len(res_list)
            crossref_works_pubs.extend(extract_crossref(res_list, l))

        return crossref_works_pubs

    def doaj(self):

        doaj_pubs = []

        if self.query_keyword != '':
            response = requests.get(DOAJ_URL + 'articles/bibjson.keywords:' + self.query_keyword).json()
            res_list = response['results']
            l = len(res_list)
            doaj_pubs.extend(extract_doaj(res_list, l))

        if self.author_keyword != '':
            response = requests.get(DOAJ_URL + 'articles/bibjson.author.name:' + self.author_keyword).json()
            res_list = response['results']
            l = len(res_list)
            doaj_pubs.extend(extract_doaj(res_list, l))

        if self.affiliation_keyword != '':
            response = requests.get(DOAJ_URL + 'articles/bibjson.institution.name:' + self.affiliation_keyword).json()
            res_list = response['results']
            l = len(res_list)
            doaj_pubs.extend(extract_doaj(res_list, l))

        return doaj_pubs

    def europemc(self):

        emc_pubs = []
        title_attrib = 'title'
        author_attrib = 'authorString'
        year_attrib = 'pubYear'
        venue_attrib = 'journalTitle'

        if self.query_keyword != '':
            response = requests.get(EMC_QUERY_URL + self.query_keyword + '&format=json')
            res_list = response.json()['resultList']['result']
            l = len(res_list)
            emc_pubs.extend(extract_emc(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.author_keyword != '':
            response = requests.get(EMC_QUERY_URL + self.author_keyword + '&format=json')
            res_list = response.json()['resultList']['result']
            l = len(res_list)
            emc_pubs.extend(extract_emc(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        return emc_pubs

    def google_scholar(self):

        google_pubs = []

        if self.query_keyword != '':
            res = requests.get(GOOG_SCHOLAR_URL + self.query_keyword + '&api_key= ' + GOOGLE_API_KEY).json()
            res_list = res['organic_results']
            l = len(res_list)
            google_pubs.extend(extract_google(res_list, l))

        if self.author_keyword != '':
            res = requests.get(GOOG_SCHOLAR_URL + self.author_keyword + '&api_key=' + GOOGLE_API_KEY).json()
            res_list = res['organic_results']
            l = len(res_list)
            google_pubs.extend(extract_google(res_list, l))

        return google_pubs

    def hal(self):
        hal_pubs = []

        if self.query_keyword != '':
            response = requests.get(HAL_URL + self.query_keyword + '&wt=json').json()
            res_list = response['response']['docs']
            l = len(res_list)
            hal_pubs.extend(extract_hal(res_list, l))

        if self.author_keyword != '':
            response = requests.get(HAL_URL + self.author_keyword + '&wt=json').json()
            res_list = response['response']['docs']
            l = len(res_list)
            hal_pubs.extend(extract_hal(res_list, l))

        return hal_pubs

    def ieee(self):

        ieee_pubs = []
        title_attrib = 'title'
        author_attrib = 'authors'
        year_attrib = 'publication_year'
        venue_attrib = 'publication_title'

        if self.query_keyword != '':
            response = requests.get(IEEE_QUERY_URL + self.query_keyword + '&apikey=' + IEEE_API_KEY)
            res_list = response.json()['articles']
            l = len(res_list)
            ieee_pubs.extend(extract_ieee(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.author_keyword != '':
            response = requests.get(IEEE_QUERY_URL + self.author_keyword + '&apikey=' + IEEE_API_KEY)
            res_list = response.json()['articles']
            l = len(res_list)
            ieee_pubs.extend(extract_ieee(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.affiliation_keyword != '':
            response = requests.get(IEEE_QUERY_URL + self.affiliation_keyword + '&apikey=' + IEEE_API_KEY)
            res_list = response.json()['articles']
            l = len(res_list)
            ieee_pubs.extend(extract_ieee(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        return ieee_pubs

    def openalex(self):

        openalex_pubs = []

        if self.query_keyword != '':
            response = requests.get(OPENALEX_QUERY_URL + self.query_keyword)
            res_list = response.json()['results']
            openalex_pubs.extend(extract_alex(res_list, len(res_list)))

        if self.author_keyword != '':
            response = requests.get(OPENALEX_QUERY_URL + self.author_keyword)
            res_list = response.json()['results']
            openalex_pubs.extend(extract_alex(res_list, len(res_list)))

        return openalex_pubs

    def scopus(self):

        scopus_pubs = []
        title_attrib = 'dc:title'
        author_attrib = 'dc:creator'
        year_attrib = 'prism:coverDate'
        venue_attrib = 'prism:publicationName'

        if self.query_keyword != '':
            response = requests.get(SCOPUS_QUERY_URL + self.query_keyword + '&apiKey=' + SCOPUS_API_KEY)
            res_list = response.json()['search-results']['entry']
            l = len(res_list)
            scopus_pubs.extend(extract_scopus(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.author_keyword != '':
            response = requests.get(SCOPUS_QUERY_URL + self.author_keyword + '&apiKey=' + SCOPUS_API_KEY)
            res_list = response.json()['search-results']['entry']
            l = len(res_list)
            scopus_pubs.extend(extract_scopus(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        return scopus_pubs

    def semanticscholar(self):

        ss_pubs = []
        title_attrib = 'title'
        author_attrib = 'authors'
        year_attrib = 'year'
        venue_attrib = 'venue'

        if self.query_keyword != '':
            response = requests.get(
                SEM_SCHOLAR_QUERY_URL + self.query_keyword + '&&limit=30&fields=url,title,abstract,authors,venue,year')
            res_list = response.json()['data']
            l = len(res_list)
            ss_pubs.extend(extract_ss(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        if self.author_keyword != '':
            response = requests.get(
                SEM_SCHOLAR_QUERY_URL + self.author_keyword + '&&limit=30&fields=url,title,abstract,authors,venue,year')
            res_list = response.json()['data']
            l = len(res_list)
            ss_pubs.extend(extract_ss(l, res_list, title_attrib, author_attrib, year_attrib, venue_attrib))

        return ss_pubs


source = source('database', 'Kevin+Chang', 'University of Illinois')

print(source.semanticscholar())
