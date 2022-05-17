# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.


import argparse
import json
from source import Source


def main(args):
    inst = args.affiliation
    sources = args.sources
    q = args.query_keyword
    author = args.author

    if sources == 'all':
        sources = 'europemc,scopus,semanticscholar,ieee,arxiv,hal,openalex,crossref_works,google_scholar,doaj'

    final_list = []
    for pub_source in sources.split(','):
        pub_source_list = []

        # Define source class object

        source = Source(q, author, inst)
        try:
            # call source from class
            eval_str = "source." + pub_source + "()"
            pub_source_list = eval(eval_str)
            final_list.extend(pub_source_list)
            print("Extracted records from ", pub_source)
        except:
            print("could not query ", pub_source)
    print("Completed extracting " + str(len(final_list)) + " records")
    print("Saving file in ", args.file_name)
    with open(args.file_name, 'w') as f:
        json.dump(final_list, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Publications')

    parser.add_argument('--sources', dest='sources', type=str, default='all',
                        help='Enter sources seperated by comma ')
    parser.add_argument('--term', dest='query_keyword', type=str, default='',
                        help='Enter search query term')
    parser.add_argument('--author', default="",
                        help="Author name")
    parser.add_argument('--affiliation', dest="affiliation", type=str, default='',
                        help='Name of Affiliation')
    parser.add_argument('--filename', dest="file_name", type=str, default='records.json',
                        help='Name of json file')
    args = parser.parse_args()
    main(args)
