"""Main module."""

import os
import re
import logging
import bibtexparser

with open(os.environ.get('PATH_MENDELEY_BIB', os.path.join(os.environ.get('HOME'), 'drafts/mendeley.bib/zotero.bib'))) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

logging.getLogger('bibtexparser').setLevel(logging.INFO)

def cite(*tags):
    # why not use one string? forclarity

    logger = logging.getLogger('bibtexparser')

    entries = []
    for e in bib_database.entries:
        match = True
        for tag in tags:
            tag_match = False
            #e_tags = re.split(r"[,]",e.get('mendeley-tags',"").lower())
            e_tags = e.get('mendeley-tags',"").lower()
            e_tags += e.get('keywords',"").lower()

            if tag.lower() in e_tags:
                logger.debug("tag match",tag,e_tags)
                tag_match = True

            author_list = re.split(r"[\b, ]",e.get('author',"").lower())
            if tag.lower() in author_list:
                logger.debug("author match",tag,author_list)
                tag_match = True

            if tag.startswith('t:') and e.get('title') is not None and tag[2:].lower() in e.get('title').lower():
                logger.debug("title match",tag,e.get('title'))
                tag_match = True
            
            if not tag_match:
                match = False
                

        if match:
            entries.append(e)
            
    
    return ",".join([entry['ID'] for entry in entries])

