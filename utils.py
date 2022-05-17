import re


# Contains utils functions to extract attributes from JSON or XML data for the given source

def extract_arxiv_xml(tree, title_attrib, author_attrib, year_attrib, venue_attrib):
    list_of_pubs = []
    for child in tree:
        new_dict = {}
        author_string = ''
        if child.tag.endswith('entry'):
            for gc in child:
                if gc.tag.split('}')[1] == year_attrib:
                    new_dict['year'] = gc.text.split('-')[0]
                elif gc.tag.split('}')[1] == title_attrib:
                    new_dict['title'] = gc.text
                elif gc.tag.split('}')[1] == author_attrib:
                    for author_name in gc:
                        if author_string != '':
                            author_string = author_string + ',' + author_name.text
                        else:
                            author_string = author_name.text
                elif gc.tag.split('}')[1] == venue_attrib:
                    new_dict['venue'] = gc.text
            if "venue" not in new_dict.keys():
                new_dict['venue'] = "None"
            new_dict['authors'] = author_string
            list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_crossref(res_list, l):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        if 'title' in res_list[i].keys():
            new_dict['title'] = res_list[i]['title'][0]
        else:
            new_dict['title'] = 'Not found'
        if 'author' in res_list[i].keys():
            if type(res_list[i]['author']) == list:
                author_string = ''
                for author in res_list[i]['author']:
                    first_name = ''
                    last_name = ''
                    if 'given' in author.keys():
                        first_name = author['given'] + ' '
                    if 'family' in author.keys():
                        last_name = author['family']
                    if author_string == '':
                        author_string = first_name + last_name
                    else:
                        author_string = author_string + ',' + first_name + last_name
                new_dict['authors'] = author_string
            else:
                new_dict['authors'] = res_list[i]['author']
        new_dict['year'] = res_list[i]['indexed']['date-time'].split('-')[0]
        new_dict['venue'] = res_list[i]['publisher']
        list_of_pubs.append(new_dict)

    return list_of_pubs


def extract_doaj(res_list, l):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = res_list[i]['bibjson']['title']
        new_dict['year'] = res_list[i]['bibjson']['year']
        new_dict['venue'] = res_list[i]['bibjson']['journal']['publisher']
        author_string = ''
        for author in res_list[i]['bibjson']['author']:
            if author_string == '':
                author_string = author['name']
            else:
                author_string = author_string + ',' + author['name']
        new_dict['authors'] = author_string
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_emc(l, entire_list, title_attrib, author_attrib, year_attrib, venue_attrib):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = entire_list[i][title_attrib]
        if author_attrib in entire_list[i].keys():
            new_dict['authors'] = entire_list[i][author_attrib]
        else:
            new_dict['authors'] = ''
        new_dict['year'] = entire_list[i][year_attrib]
        if 'journalTitle' in entire_list[i].keys():
            new_dict['venue'] = entire_list[i][venue_attrib]
        else:
            new_dict['venue'] = ''
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_google(res_list, l):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = res_list[i]['title']
        new_dict['year'] = re.match(r'.*([1-2][0-9]{3})', res_list[i]['publication_info']['summary']).group(1)
        new_dict['venue'] = res_list[i]['publication_info']['summary'].split('-')[-1]
        new_dict['authors'] = res_list[i]['publication_info']['summary'].split('-')[0]
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_hal(res_list, l):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        if "et al.." in res_list[i]['label_s']:
            delimeter = "et al.."
            str_joining_authors = res_list[i]['label_s'].split(delimeter)
            new_dict['authors'] = str_joining_authors[0]
            new_dict['title'] = str_joining_authors[1].split(".")[0]
            new_dict['venue'] = str_joining_authors[1].split(".")[1]
        else:
            new_dict['title'] = res_list[i]['label_s'].split('.')[1]
            new_dict['authors'] = res_list[i]['label_s'].split('.')[0]
            new_dict['venue'] = res_list[i]['label_s'].split('.')[2]
        new_dict['year'] = 'None'
        if re.match(r'.*([1-2][0-9]{3})', new_dict['venue']) is not None:
            new_dict['year'] = re.match(r'.*([1-2][0-9]{3})', new_dict['venue']).groups()[0]

        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_ieee(l, entire_list, title_attrib, author_attrib, year_attrib, venue_attrib):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = entire_list[i][title_attrib]
        author_string = ''
        for author in entire_list[i][author_attrib][author_attrib]:
            if author_string != '':
                author_string = author_string + ',' + author['full_name']
            else:
                author_string = author['full_name']
        new_dict['authors'] = author_string
        new_dict['year'] = entire_list[i][year_attrib]
        new_dict['venue'] = entire_list[i][venue_attrib]
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_alex(res_list, l):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = res_list[i]['title']
        new_dict['year'] = res_list[i]['publication_year']
        new_dict['venue'] = res_list[i]['host_venue']['display_name']
        author_string = ''
        for list_author in res_list[i]['authorships']:
            if author_string == '':
                author_string = list_author['author']['display_name']
            else:
                author_string += ',' + list_author['author']['display_name']
        new_dict['authors'] = author_string
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_scopus(l, entire_list, title_attrib, author_attrib, year_attrib, venue_attrib):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = entire_list[i][title_attrib]
        new_dict['authors'] = entire_list[i][author_attrib]
        new_dict['year'] = entire_list[i][year_attrib].split('-')[0]
        new_dict['venue'] = entire_list[i][venue_attrib]
        list_of_pubs.append(new_dict)
    return list_of_pubs


def extract_ss(l, entire_list, title_attrib, author_attrib, year_attrib, venue_attrib):
    list_of_pubs = []
    for i in range(0, l, 1):
        new_dict = {}
        new_dict['title'] = entire_list[i][title_attrib]
        author_string = ''
        for author in entire_list[i][author_attrib]:
            if author_string != '':
                author_string = author_string + ',' + author['name']
            else:
                author_string = author['name']
        new_dict['authors'] = author_string
        new_dict['year'] = entire_list[i][year_attrib]
        new_dict['venue'] = entire_list[i][venue_attrib]
        list_of_pubs.append(new_dict)
    return list_of_pubs
