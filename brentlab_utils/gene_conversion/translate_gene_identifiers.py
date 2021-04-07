#!/usr/bin/env python

# third party packages
import requests
import pandas as pd

def translateGeneIdentifiers(organism, target, query, url='https://biit.cs.ut.ee/gprofiler/api/convert/convert/'):
    """translate gene list from current state to target identifiers.
    Using gprofilr (https://biit.cs.ut.ee/gprofiler/gost), translate from input gene list ids to some target ids (see )
    :usage: df = gene_conversion.translateGeneIdentifiers('scerevisiae', 'ENTREZGENE_ACC', ["YDR189W", "YER105C", "YGR005C", "YKL062W", "YPR181C", "YPL218W", "YHR046C"])
    :param str url: url to the conversion. default is to appropriate gprofilr endpoint
    :param str organism: eg hsapiens. see here for list of organisms: https://biit.cs.ut.ee/gprofiler/page/organism-list
    :param str target: what type of identifiers to translate to. Here are a list of name spaces https://biit.cs.ut.ee/gprofiler/page/namespaces-list
    :param list query: a LIST of gene identifiers, eg ["YDR189W", "YER105C", "YGR005C", "YKL062W", "YPR181C", "YPL218W", "YHR046C"]
    :raise: None handled yet TODO
    :returns:  a dataframe created from the response of the http request
    :rtype: pandas dataframe
    """

    r = requests.post(
            url='https://biit.cs.ut.ee/gprofiler/api/convert/convert/',
            json={
                'organism': organism,
                'target': target,
                'query': query,
            }
        )
    return pd.DataFrame(r.json()['result'])