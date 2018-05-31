import lxml.etree
import pprint
import pandas as pd

# Load XML file from PubMed
XMLFile = "pubmed_result.xml"
root = lxml.etree.parse(XMLFile)
PMID_Dict = {}

# Sort out XML data
def findingCitation():
    results = root.findall('PubmedArticle/MedlineCitation')
    counter = 0
    for r in results:
        counter += 1
        PMID_Dict[counter] = {}
        author_list = []
        grant_list = []
        journal_info = ""
        try:
            # Grab PMID Number
            PMID_Number = r.find('PMID').text

            # Grab Title
            PMID_Title = r.find('Article/ArticleTitle').text

            # Create URL
            PMID_URL = "/pubmed/" + PMID_Number

            # Grab Author List
            author_info = r.findall('Article/AuthorList/Author')
            for author in author_info:
                lastName = author.find('LastName').text
                initials = author.find('Initials').text
                authorName = lastName + " " + initials
                author_list.append(authorName)
            authorNameList = ", ".join(author_list)

            # Grab Publication Information
            try: 
                journalAbbrv = r.find('Article/Journal/ISOAbbreviation').text
                journalPubYr = r.find('Article/Journal/JournalIssue/PubDate/Year').text
                journalPubMt = r.find('Article/Journal/JournalIssue/PubDate/Month').text
                journalVol = r.find('Article/Journal/JournalIssue/Volume').text
                journalIssue = r.find('Article/Journal/JournalIssue/Issue').text
                journalPages = r.find('Article/Pagination/MedlinePgn').text
                journalDOI = r.find('Article/ELocationID').text
            except:
                pass
            journal_info = journalAbbrv + " " + journalPubYr + " " + journalPubMt + ";" + \
                           journalVol + "(" + journalIssue + "):" + journalPages + ". " + \
                           "doi: " + journalDOI + "." 
            
            # Grab Grant Information
            grant_info = r.findall('Article/GrantList/Grant')
            for grant in grant_info:
                grant_list.append(grant.find('GrantID').text)
        except:
            pass
        # Generate a dictionary with the above information and add it to the blank PMID dictionary
        temp_dict = {'PMID Number': PMID_Number, \
                    "Title": PMID_Title, \
                    "URL": PMID_URL, \
                    "Description": authorNameList, \
                    "Details": journal_info, \
                    "Grants": grant_list}
        PMID_Dict[counter].update(temp_dict)
    # Convert dictionary to pandas dataframe for future manipulation 
    df = pd.DataFrame.from_dict(PMID_Dict, orient='index')
    df.to_csv("PMIDs.csv")
    print(df.head())

findingCitation()