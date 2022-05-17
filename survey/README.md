### 1.Semantic Scholar

#### Link to API documentation <br>
https://api.semanticscholar.org/api-docs/graph
#### API endpoint and description <br>
https://api.semanticscholar.org/graph/v1/paper/search <br>
#### Query Parameters <br> 
keyword, limit, offset
#### Return Format <br>
JSON
#### Return Fields <br>
```paperId - Always included
externalIds
url
title - Included if no fields are specified
abstract
venue
year
referenceCount
citationCount
influentialCitationCount
isOpenAccess
fieldsOfStudy
s2FieldsOfStudy
authors - Up to 500 will be returned
authorId - Always included
name - Always included
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 2.CORE
#### Link to API documentation <br>
https://api.core.ac.uk/docs/v3#operation/null
#### API endpoint and description <br>
https://api.core.ac.uk/v3/search/{identifier} <br>
#### Query Parameters <br> 

#### Return Format <br>
JSON
#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>
30 days free trial
#### Comments <br>

#### Rate <br>

### 3.DBLP
#### Link to API documentation <br>
https://dblp.uni-trier.de/xml/docu/dblpxmlreq.pdf
#### API endpoint and description <br>
http://dblp.uni-trier.de/search/author?xauthor=Schek <br>Returns Authors profile links whose names match the author name in query parameter
#### Query Parameters <br> 
author_name
#### Return Format <br>
XML
#### Return Fields <br>
```author pid, urlpt (authors name that match)
<author pid=""90/11128"" urlpt=""f/Fateh:Schekeb"">Schekeb Fateh</author>
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 4.Research Gate
#### Link to API documentation <br>
No API documentation. Web Scraper available - https://github.com/kaleguy/scraper-api
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>
#### Subscription <br>

#### Comments <br>
The scraper is nodejs application. The application needs to be installed and then used to scrape data from research gate
#### Rate <br>

### 5.EuropePMC
#### Link to API documentation <br>
http://europepmc.org/RestfulWebService
#### API endpoint and description <br>
https://www.ebi.ac.uk/europepmc/webservices/rest/search <br>Returns Publications that match the query
#### Query Parameters <br> 
keyword or authors name
#### Return Format <br>
XML,JSON
#### Return Fields <br>
```""id"": ""35085174"",
""source"": ""MED"",
""pmid"": ""35085174"",
""doi"": ""10.1097/rlu.0000000000004080"",
""title"": ""18F-Fluciclovine Uptake in Intramuscular Injecting Site of Antiandrogen."",
""authorString"": ""Hsieh TC, Wu YC, Kao CH, Yen KY, Sun SS."",
""journalTitle"": ""Clin Nucl Med"",
""issue"": ""5"",
""journalVolume"": ""47"",
""pubYear"": ""2022"",
""journalIssn"": ""0363-9762; 1536-0229; "",
""pageInfo"": ""e401-e402"",
""pubType"": ""journal article; case reports"",
""isOpenAccess"": ""N"",
""inEPMC"": ""N"",
""inPMC"": ""N"",
""hasPDF"": ""N"",
""hasBook"": ""N"",
""hasSuppl"": ""N"",
""citedByCount"": 0,
""hasReferences"": ""N"",
""hasTextMinedTerms"": ""Y"",
""hasDbCrossReferences"": ""N"",
""hasLabsLinks"": ""Y"",
""hasTMAccessionNumbers"": ""N"",
""firstIndexDate"": ""2022-01-28"",
""firstPublicationDate"": ""2022-05-01""
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 6.SCOPUS
#### Link to API documentation <br>
https://dev.elsevier.com/api_docs.html
#### API endpoint and description <br>
https://api.elsevier.com/content/search/scopus <br>
#### Query Parameters <br> 

#### Return Format <br>
JSON
#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 7.Enginering Village
#### Link to API documentation <br>

#### API endpoint and description <br>
https://api.elsevier.com/content/ev/results	 <br>Returns list of results from Engineering Village Search Database
#### Query Parameters <br> 
keyword
#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
No access to API Key without an institutional profile
#### Rate <br>

### 8.Embase
#### Link to API documentation <br>

#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
No access to API Key without an institutional profile
#### Rate <br>

### 9.Aminer
#### Link to API documentation <br>
http://doc.aminer.org/en/latest/s/pub/basic.html#request-parameters
#### API endpoint and description <br>
https://api.aminer.org/api/search/pub <br>Return publications that match keyword
#### Query Parameters <br> 
keyword
#### Return Format <br>
JSON
#### Return Fields <br>
```{
            ""retrieve_info"": {},
            ""num_viewed"": 87,
            ""wos_type"": [],
            ""num_wos_citation"": 0,
            ""classes"": [],
           
            ""urls"": [
                ""http://dx.doi.org/10.1038/s41418-020-0530-3"",
                ""https://app.dimensions.ai/details/publication/pub.1125823278"",
                ""https://www.nature.com/articles/s41418-020-0530-3"",
                ""https://www.ncbi.nlm.nih.gov/pubmed/32205856"",
                ""https://www.nature.com/articles/s41418-020-0530-3.pdf"",
                ""https://www.scilit.net/article/979333b91152ad132fd045a1205a5fba"",
                ""https://pubmed.ncbi.nlm.nih.gov/32205856/?from_term=trending%5Bsb%5D&from_pos=9"",
                ""http://www.webofknowledge.com/""
            ],
            ""pdf"": ""https://static.aminer.cn/upload/pdf/984/1843/900/5e8f12769e795ec180f4799d_0.pdf"",
            ""highlight"": {
                ""abstract"": """"
            },
            ""score"": 2036531.25,
            ""author_ids"": [
                ""53f46ff5dabfaec09f264dc0"",
                ""53f56269dabfae5d2ef8047e"",
                ""560f851945cedb3397746bd0"",
                """",
                ""542ccddfdabfae498ae11391"",
                ""5406da44dabfae8faa626a03"",
                """",
                ""540fe352dabfae450f4b175a"",
                ""53fa0925dabfae7f97b01739"",
                ""54059e94dabfae450f3bd785""
            ],
            ""pages"": {
                ""s"": ""1451.0"",
                ""e"": ""1454.0""
            },
            ""num_citation"": 857,
            ""year"": 2020,
            ""id"": ""5e8f12769e795ec180f4799d"",
            ""authors"": [
                {
                    ""aff"": {
                        ""desc"": ""Soochow Univ, Affiliated Hosp 1, State Key Lab Radiat Med & Protect, Inst Translat Med,Med Coll, Suzhou, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Yufang Shi"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": true,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Chinese Acad Sci, Shanghai Inst Biol Sci, Shanghai Inst Nutr & Hlth, 320 Yueyang Rd, Shanghai 200031, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Ying Wang"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Soochow Univ, Affiliated Hosp 1, State Key Lab Radiat Med & Protect, Inst Translat Med,Med Coll, Suzhou, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Changshun Shao"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Soochow Univ, Affiliated Hosp 1, State Key Lab Radiat Med & Protect, Inst Translat Med,Med Coll, Suzhou, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Jianan Huang"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Soochow Univ, Affiliated Hosp 1, State Key Lab Radiat Med & Protect, Inst Translat Med,Med Coll, Suzhou, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Jianhe Gan"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Soochow Univ, Affiliated Hosp 1, State Key Lab Radiat Med & Protect, Inst Translat Med,Med Coll, Suzhou, Peoples R China"",
                        ""id"": """"
                    },
                    ""name"": ""Xiaoping Huang"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Temple Univ, Sbarro Hlth Res Org, Philadelphia, PA 19122 USA"",
                        ""id"": """"
                    },
                    ""name"": ""Enrico Bucci"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Natl Inst Infect Dis Lazzaro Spallanzani IRCCS, I-00149 Rome, Italy"",
                        ""id"": """"
                    },
                    ""name"": ""Mauro Piacentini"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Natl Inst Infect Dis Lazzaro Spallanzani IRCCS, I-00149 Rome, Italy"",
                        ""id"": """"
                    },
                    ""name"": ""Giuseppe Ippolito"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                },
                {
                    ""aff"": {
                        ""desc"": ""Univ Roma Tor Vergata, TOR, Dept Expt Med, I-00133 Rome, Italy"",
                        ""id"": """"
                    },
                    ""name"": ""Gerry Melino"",
                    ""num_viewed"": 0,
                    ""avatar"": """",
                    ""indices"": {},
                    ""is_following"": false,
                    ""revised"": {
                        ""cname"": """",
                        ""mid"": """",
                        ""mtime"": ""1970-01-01 00:00:00"",
                        ""cid"": """",
                        ""mname"": """",
                        ""ctime"": ""1970-01-01 00:00:00""
                    },
                    ""locks"": {},
                    ""acm_citations"": [],
                    ""pos"": [],
                    ""hidden"": false,
                    ""award"": [],
                    ""bind"": false,
                    ""contact"": {
                        ""affiliation"": """",
                        ""has_email_cr"": false,
                        ""work"": """",
                        ""bio"": """",
                        ""edu"": """",
                        ""fax"": """",
                        ""homepage"": """",
                        ""address"": """",
                        ""has_email"": false,
                        ""phone"": """"
                    },
                    ""work"": [],
                    ""links"": [],
                    ""edu"": [],
                    ""id"": """",
                    ""is_holding"": false,
                    ""src"": [],
                    ""intr"": [],
                    ""num_followed"": 0,
                    ""seminar_viewed"": 0,
                    ""honor"": []
                }
            ],
            ""labels"": [],
            ""title"": ""COVID-19 infection: the perspectives on immune responses"",
            ""lang"": ""en"",
            ""doi"": ""10.1038/s41418-020-0530-3"",
            ""num_starred"": 0,
            ""venue"": {
                ""name"": ""CELL DEATH AND DIFFERENTIATION"",
                ""indices"": {},
                ""mid"": """",
                ""info"": {
                    ""name"": ""CELL DEATH AND DIFFERENTIATION""
                },
                ""issue"": ""5.0"",
                ""id"": """",
                ""type"": 0,
                ""volume"": ""27.0""
            },
            ""issn"": ""1350-9047""
        },
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 10.arxiv
#### Link to API documentation <br>
https://arxiv.org/help/api/basics
#### API endpoint and description <br>
http://export.arxiv.org/api/ <br>Returns publication that match keyword, authors name or institutaion name
#### Query Parameters <br> 
keyword, author name, affiliation name
#### Return Format <br>
XML
#### Return Fields <br>
```  <id>http://arxiv.org/abs/math/0412226v1</id>
        <updated>2004-12-11T22:18:14Z</updated>
        <published>2004-12-11T22:18:14Z</published>
        <title>Some combinatorial aspects of movies and movie-moves in the theory of
  smoothly knotted surfaces in R4</title>
        <summary>  For proper subsets U of {1,2,...,31} we define and construct U-regular
isotopy invariants of the Carter-Rieger-Saito movies (representing knotted
surfaces) and use these to show that there are ambient isotopic knotted
surfaces represented by movies M1 and M2 for which movie-moves of type 31 are
required to get from M1 to M2.
</summary>
        <author>
            <name>Glenn Lancaster</name>
            <arxiv:affiliation xmlns:arxiv=""http://arxiv.org/schemas/atom"">DePaul University, Chicago, Illinois</arxiv:affiliation>
        </author>
        <author>
            <name>Richard Larson</name>
            <arxiv:affiliation xmlns:arxiv=""http://arxiv.org/schemas/atom"">University of Illinois at Chicago</arxiv:affiliation>
        </author>
        <author>
            <name>Jacob Towber</name>
            <arxiv:affiliation xmlns:arxiv=""http://arxiv.org/schemas/atom"">DePaul University, Chicago, Illinois</arxiv:affiliation>
        </author>
        <arxiv:comment xmlns:arxiv=""http://arxiv.org/schemas/atom"">Submitted to Contemporary Math, subseries of Israel Math. Conf.,
  Proceedings of July 5-12 Haifa Conference on Quantum Groups</arxiv:comment>
        <link href=""http://arxiv.org/abs/math/0412226v1"" rel=""alternate"" type=""text/html""/>
        <link title=""pdf"" href=""http://arxiv.org/pdf/math/0412226v1"" rel=""related"" type=""application/pdf""/>
        <arxiv:primary_category xmlns:arxiv=""http://arxiv.org/schemas/atom"" term=""math.GT"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""math.GT"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""math.CT"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""math.QA"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""57Q45; 18D05"" scheme=""http://arxiv.org/schemas/atom""/>
    </entry>
    <entry>
        <id>http://arxiv.org/abs/funct-an/9501006v2</id>
        <updated>1995-03-11T14:03:24Z</updated>
        <published>1995-01-25T14:05:01Z</published>
        <title>Toward a general theory of transmutation</title>
        <summary>  A general construction of transmutation operators is developed for
selfadjoint operators in Gelfand triples. Theorems regarding analyticity of
generalized eigenfunctions and Paley-Wiener properties are proved.
</summary>
        <author>
            <name>A. Boumenir</name>
            <arxiv:affiliation xmlns:arxiv=""http://arxiv.org/schemas/atom"">K.F.U.P.M, Dhahran, Saudi Arabia, visiting University of Illinois</arxiv:affiliation>
        </author>
        <author>
            <name>R. Carroll</name>
            <arxiv:affiliation xmlns:arxiv=""http://arxiv.org/schemas/atom"">Mathematics Dept., University of Illinois, Urbana</arxiv:affiliation>
        </author>
        <arxiv:comment xmlns:arxiv=""http://arxiv.org/schemas/atom"">Clarification of domains, 18 pages, latex</arxiv:comment>
        <link href=""http://arxiv.org/abs/funct-an/9501006v2"" rel=""alternate"" type=""text/html""/>
        <link title=""pdf"" href=""http://arxiv.org/pdf/funct-an/9501006v2"" rel=""related"" type=""application/pdf""/>
        <arxiv:primary_category xmlns:arxiv=""http://arxiv.org/schemas/atom"" term=""funct-an"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""funct-an"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""math.FA"" scheme=""http://arxiv.org/schemas/atom""/>
        <category term=""math.RT"" scheme=""http://arxiv.org/schemas/atom""/>
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 11.CiteSeerX
#### Link to API documentation <br>
http://citeseer.ist.psu.edu/api/
#### API endpoint and description <br>
http://citeseerx.ist.psu.edu/oai2 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
Could not use the API. Request took longer than 30 seconds. Datasets available here - https://csxstatic.ist.psu.edu/downloads/data
#### Rate <br>

### 12.HAL
#### Link to API documentation <br>
https://api.archives-ouvertes.fr/docs/search
#### API endpoint and description <br>
http://api.archives-ouvertes.fr/search/ <br>Returns docid, title,uri and author names that match
#### Query Parameters <br> 
keyword, author name
#### Return Format <br>
XML,JSON
#### Return Fields <br>
```<doc>
            <int name=""docid"">1731382</int>
            <str name=""label_s"">Pooja Khatri, Werner Hacke, Jens Fiehler, Jeffrey Saver, Hans-Christoph Diener, et al.. State of Acute Endovascular Therapy. Stroke, American Heart Association, 2015, 46 (6), pp.1727 - 1734. &amp;#x27E8;10.1161/STROKEAHA.115.008782&amp;#x27E9;. &amp;#x27E8;hal-01731382&amp;#x27E9;</str>
            <str name=""uri_s"">https://hal.univ-lorraine.fr/hal-01731382</str>
        </doc>
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 13.SSRN
#### Link to API documentation <br>
https://github.com/karthiktadepalli1/ssrn-scraper
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>
#### Subscription <br>

#### Comments <br>
No API found
#### Rate <br>

### 14.RePec: Research Papers in Economics
#### Link to API documentation <br>
https://ideas.repec.org/api.html
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
account available to economic academics 
#### Rate <br>

### 15.PhilPapers
#### Link to API documentation <br>
https://philpapers.org/help/api/json.html
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
API endpoint download all bibliographic data requires us to contact and make a request 
#### Rate <br>

### 16.Academic Labs
#### Link to API documentation <br>
https://www.academiclabs.com/
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>
#### Subscription <br>
Subscription based. 7-day free trial.
#### Comments <br>

#### Rate <br>

### 17.AGRIS
#### Link to API documentation <br>
https://agris.fao.org/agris-search/search.do?recordID=US2019X00154
#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>
Offers a programatic interface search API
#### Rate <br>

### 18.MedilinePlus
#### Link to API documentation <br>
https://medlineplus.gov/about/developers/webservices/
#### API endpoint and description <br>
https://wsearch.nlm.nih.gov/ws/query <br>database (it should be set to healthTopics) and keyword
#### Query Parameters <br> 

#### Return Format <br>
XML
#### Return Fields <br>
```<document rank=""1"" url=""https://medlineplus.gov/asthma.html"">
            <content name=""title"">&lt;span class=""qt0""&gt;Asthma&lt;/span&gt;</content>
            <content name=""organizationName"">National Library of Medicine</content>
            <content name=""altTitle"">Bronchial &lt;span class=""qt0""&gt;Asthma&lt;/span&gt;</content>
            <content name=""FullSummary"">What is &lt;span class=""qt0""&gt;asthma&lt;/span&gt;?&lt;p&gt;&lt;span class=""qt0""&gt;Asthma&lt;/span&gt; is a chronic (long-term) lung disease. It affects your airways, the tubes that carry air in and out of your lungs. When you have &lt;span class=""qt0""&gt;asthma&lt;/span&gt;, your airways can become inflamed and narrowed. This can cause wheezing, coughing, and tightness in your chest. When these symptoms get worse than usual, it is called an &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attack or flare-up.&lt;/p&gt;What causes &lt;span class=""qt0""&gt;asthma&lt;/span&gt;?&lt;p&gt;The exact cause of &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is unknown. Genetics and your environment likely play a role in who gets &lt;span class=""qt0""&gt;asthma&lt;/span&gt;.&lt;/p&gt;&lt;p&gt;An &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attack can happen when you are exposed to an &lt;span class=""qt0""&gt;asthma&lt;/span&gt; trigger. An &lt;span class=""qt0""&gt;asthma&lt;/span&gt; trigger is something that can set off or worsen your &lt;span class=""qt0""&gt;asthma&lt;/span&gt; symptoms. Different triggers can cause different types of &lt;span class=""qt0""&gt;asthma&lt;/span&gt;:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Allergic &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is caused by allergens. Allergens are substances that cause an allergic reaction. They can include
        &lt;ul&gt;&lt;li&gt;Dust mites&lt;/li&gt;&lt;li&gt;Mold&lt;/li&gt;&lt;li&gt;Pets&lt;/li&gt;&lt;li&gt;Pollen from grass, trees, and weeds&lt;/li&gt;&lt;li&gt;Waste from pests such as cockroaches and mice&lt;/li&gt;&lt;/ul&gt;
&lt;/li&gt;&lt;li&gt;Nonallergic &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is caused by triggers that are not allergens, such as
        &lt;ul&gt;&lt;li&gt;Breathing in cold air&lt;/li&gt;&lt;li&gt;Certain medicines&lt;/li&gt;&lt;li&gt;Household chemicals&lt;/li&gt;&lt;li&gt;Infections such as colds and the flu&lt;/li&gt;&lt;li&gt;Outdoor air pollution&lt;/li&gt;&lt;li&gt;Tobacco smoke&lt;/li&gt;&lt;/ul&gt;
&lt;/li&gt;&lt;li&gt;Occupational &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is caused by breathing in chemicals or industrial dusts at work&lt;/li&gt;&lt;li&gt;Exercise-induced &lt;span class=""qt0""&gt;asthma&lt;/span&gt; happens during physical exercise, especially when the air is dry&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;span class=""qt0""&gt;Asthma&lt;/span&gt; triggers may be different for each person and can change over time.&lt;/p&gt;Who is at risk for &lt;span class=""qt0""&gt;asthma&lt;/span&gt;?&lt;p&gt;&lt;span class=""qt0""&gt;Asthma&lt;/span&gt; affects people of all ages, but it often starts during childhood. Certain factors can raise your risk of having &lt;span class=""qt0""&gt;asthma&lt;/span&gt;:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Being exposed to secondhand smoke when your mother is pregnant with you or when you are a small child&lt;/li&gt;&lt;li&gt;Being exposed to certain substances at work, such as chemical irritants or industrial dusts&lt;/li&gt;&lt;li&gt;Genetics and family history. You are more likely to have &lt;span class=""qt0""&gt;asthma&lt;/span&gt; if one of your parents has it, especially if it's your mother.&lt;/li&gt;&lt;li&gt;Race or ethnicity. Black and African Americans and Puerto Ricans are at higher risk of &lt;span class=""qt0""&gt;asthma&lt;/span&gt; than people of other races or ethnicities.&lt;/li&gt;&lt;li&gt;Having other diseases or conditions such as obesity and allergies&lt;/li&gt;&lt;li&gt;Often having viral respiratory infections as a young child&lt;/li&gt;&lt;li&gt;Sex. In children, &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is more common in boys. In teens and adults, it is more common in women.&lt;/li&gt;&lt;/ul&gt;What are the symptoms of &lt;span class=""qt0""&gt;asthma&lt;/span&gt;?&lt;p&gt;The symptoms of &lt;span class=""qt0""&gt;asthma&lt;/span&gt; include:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Chest tightness&lt;/li&gt;&lt;li&gt;Coughing, especially at night or early morning&lt;/li&gt;&lt;li&gt;Shortness of breath&lt;/li&gt;&lt;li&gt;Wheezing, which causes a whistling sound when you breathe out&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;These symptoms can range from mild to severe. You may have them every day or only once in a while.&lt;/p&gt;&lt;p&gt;When you are having an &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attack, your symptoms get much worse. The attacks may come on gradually or suddenly. Sometimes they can be life-threatening. They are more common in people who have severe &lt;span class=""qt0""&gt;asthma&lt;/span&gt;. If you are having &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attacks, you may need a change in your treatment.&lt;/p&gt;How is &lt;span class=""qt0""&gt;asthma&lt;/span&gt; diagnosed?&lt;p&gt;Your health care provider may use many tools to diagnose &lt;span class=""qt0""&gt;asthma&lt;/span&gt;:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Physical exam&lt;/li&gt;&lt;li&gt;Medical history&lt;/li&gt;&lt;li&gt;Lung function tests, including spirometry, to test how well your lungs work&lt;/li&gt;&lt;li&gt;Tests to measure how your airways react to specific exposures. During this test, you inhale different concentrations of allergens or medicines that may tighten the muscles in your airways. Spirometry is done before and after the test.&lt;/li&gt;&lt;li&gt;Peak expiratory flow (PEF) tests to measure how fast you can blow air out using maximum effort&lt;/li&gt;&lt;li&gt;Fractional exhaled nitric oxide (FeNO) tests to measure levels of nitric oxide in your breath when you breathe out. High levels of nitric oxide may mean that your lungs are inflamed.&lt;/li&gt;&lt;li&gt;Allergy skin or blood tests, if you have a history of allergies. These tests check which allergens cause a reaction from your immune system.&lt;/li&gt;&lt;/ul&gt;What are the treatments for &lt;span class=""qt0""&gt;asthma&lt;/span&gt;?&lt;p&gt;If you have &lt;span class=""qt0""&gt;asthma&lt;/span&gt;, you will work with your health care provider to create a treatment plan. The plan will include ways to manage your &lt;span class=""qt0""&gt;asthma&lt;/span&gt; symptoms and prevent &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attacks. It will include:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Strategies to avoid triggers. For example, if tobacco smoke is a trigger for you, you should not smoke or allow other people to smoke in your home or car.&lt;/li&gt;&lt;li&gt;Short-term relief medicines,  also called quick-relief medicines. They help prevent symptoms or relieve symptoms during an &lt;span class=""qt0""&gt;asthma&lt;/span&gt; attack. They include an inhaler to carry with you all the time. It may also include other types of medicines which work quickly to help open your airways.&lt;/li&gt;&lt;li&gt;Control medicines.  You take them every day to help prevent symptoms. They work by reducing airway inflammation and preventing narrowing of the airways.&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;If you have a severe attack and the short-term relief medicines do not work, you will need emergency care.&lt;/p&gt;&lt;p&gt;Your provider may adjust your treatment until &lt;span class=""qt0""&gt;asthma&lt;/span&gt; symptoms are controlled.&lt;/p&gt;&lt;p&gt;Sometimes &lt;span class=""qt0""&gt;asthma&lt;/span&gt; is severe and cannot be controlled with other treatments. If you are an adult with uncontrolled &lt;span class=""qt0""&gt;asthma&lt;/span&gt;, in some cases your provider might suggest bronchial thermoplasty. This is a procedure that uses heat to shrink the smooth muscle in the lungs. Shrinking the muscle reduces your airway's ability to tighten and allows you to breathe more easily. The procedure has some risks, so it's important to discuss them with your provider.&lt;/p&gt;</content>
            <content name=""mesh"">&lt;span class=""qt0""&gt;Asthma&lt;/span&gt;</content>
            <content name=""groupName"">Lungs and Breathing</content>
            <content name=""groupName"">Immune System</content>
            <content name=""snippet"">What is &lt;span class=""qt0""&gt;asthma? Asthma&lt;/span&gt; is a chronic (long-term) lung disease. It affects your airways, the tubes that carry air in and out of your lungs. When you have  ... </content>
        </document>
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>
Did not offer required fields such as year, authors
#### Rate <br>

### 19.MySciencWork
#### Link to API documentation <br>

#### API endpoint and description <br>
 <br>
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>
#### Subscription <br>

#### Comments <br>
Commericial Product
#### Rate <br>

### 20.Openalex
#### Link to API documentation <br>
https://docs.openalex.org/api
#### API endpoint and description <br>
https://api.openalex.org/authors <br>Returns author profile and keywords associated with author
#### Query Parameters <br> 

#### Return Format <br>
JSON
#### Return Fields <br>
```{
            ""id"": ""https://openalex.org/A2410387637"",
            ""orcid"": ""https://orcid.org/0000-0003-4064-388X"",
            ""display_name"": ""P. Chang"",
            ""display_name_alternatives"": [],
            ""relevance_score"": 7499.687,
            ""works_count"": 2460,
            ""cited_by_count"": 133948,
            ""ids"": {
                ""openalex"": ""https://openalex.org/A2410387637"",
                ""orcid"": ""https://orcid.org/0000-0003-4064-388X"",
                ""mag"": ""2410387637""
            },
            ""last_known_institution"": {
                ""id"": ""https://openalex.org/I16733864"",
                ""ror"": ""https://ror.org/05bqach95"",
                ""display_name"": ""National Taiwan University"",
                ""country_code"": ""TW"",
                ""type"": ""education""
            },
            ""x_concepts"": [
                {
                    ""id"": ""https://openalex.org/C121332964"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q413"",
                    ""display_name"": ""Physics"",
                    ""level"": 0,
                    ""score"": 97.1
                },
                {
                    ""id"": ""https://openalex.org/C109214941"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q18334"",
                    ""display_name"": ""Particle physics"",
                    ""level"": 1,
                    ""score"": 92.8
                },
                {
                    ""id"": ""https://openalex.org/C62520636"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q944"",
                    ""display_name"": ""Quantum mechanics"",
                    ""level"": 1,
                    ""score"": 91.1
                },
                {
                    ""id"": ""https://openalex.org/C185544564"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q81197"",
                    ""display_name"": ""Nuclear physics"",
                    ""level"": 1,
                    ""score"": 90.8
                },
                {
                    ""id"": ""https://openalex.org/C87668248"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q40605"",
                    ""display_name"": ""Large Hadron Collider"",
                    ""level"": 2,
                    ""score"": 66.4
                },
                {
                    ""id"": ""https://openalex.org/C19694890"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q101667"",
                    ""display_name"": ""Hadron"",
                    ""level"": 2,
                    ""score"": 54.8
                },
                {
                    ""id"": ""https://openalex.org/C192562407"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q228736"",
                    ""display_name"": ""Materials science"",
                    ""level"": 0,
                    ""score"": 40.8
                },
                {
                    ""id"": ""https://openalex.org/C205649164"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q1071"",
                    ""display_name"": ""Geography"",
                    ""level"": 0,
                    ""score"": 39.6
                },
                {
                    ""id"": ""https://openalex.org/C7602139"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q6718"",
                    ""display_name"": ""Quark"",
                    ""level"": 2,
                    ""score"": 39.3
                },
                {
                    ""id"": ""https://openalex.org/C33923547"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q395"",
                    ""display_name"": ""Mathematics"",
                    ""level"": 0,
                    ""score"": 36.1
                },
                {
                    ""id"": ""https://openalex.org/C95457728"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q309"",
                    ""display_name"": ""History"",
                    ""level"": 0,
                    ""score"": 35.9
                },
                {
                    ""id"": ""https://openalex.org/C166957645"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q23498"",
                    ""display_name"": ""Archaeology"",
                    ""level"": 1,
                    ""score"": 35.9
                },
                {
                    ""id"": ""https://openalex.org/C191897082"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q11467"",
                    ""display_name"": ""Metallurgy"",
                    ""level"": 1,
                    ""score"": 35.8
                },
                {
                    ""id"": ""https://openalex.org/C40976572"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q2330873"",
                    ""display_name"": ""Gauge (firearms)"",
                    ""level"": 2,
                    ""score"": 35.7
                },
                {
                    ""id"": ""https://openalex.org/C101454708"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q17106019"",
                    ""display_name"": ""Standard Model (mathematical formulation)"",
                    ""level"": 3,
                    ""score"": 35.6
                },
                {
                    ""id"": ""https://openalex.org/C147120987"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q2225"",
                    ""display_name"": ""Electron"",
                    ""level"": 2,
                    ""score"": 35.1
                },
                {
                    ""id"": ""https://openalex.org/C179203047"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q82586"",
                    ""display_name"": ""Lepton"",
                    ""level"": 3,
                    ""score"": 34.2
                },
                {
                    ""id"": ""https://openalex.org/C184748400"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q2599934"",
                    ""display_name"": ""Physics beyond the Standard Model"",
                    ""level"": 2,
                    ""score"": 34.1
                },
                {
                    ""id"": ""https://openalex.org/C79118098"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q43101"",
                    ""display_name"": ""Boson"",
                    ""level"": 2,
                    ""score"": 33.5
                },
                {
                    ""id"": ""https://openalex.org/C127413603"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q11023"",
                    ""display_name"": ""Engineering"",
                    ""level"": 0,
                    ""score"": 32.2
                },
                {
                    ""id"": ""https://openalex.org/C184779094"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q26383"",
                    ""display_name"": ""Atomic physics"",
                    ""level"": 1,
                    ""score"": 31.6
                },
                {
                    ""id"": ""https://openalex.org/C86803240"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q420"",
                    ""display_name"": ""Biology"",
                    ""level"": 0,
                    ""score"": 30.6
                },
                {
                    ""id"": ""https://openalex.org/C1276947"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q333"",
                    ""display_name"": ""Astronomy"",
                    ""level"": 1,
                    ""score"": 29.5
                },
                {
                    ""id"": ""https://openalex.org/C46460574"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q370559"",
                    ""display_name"": ""Branching fraction"",
                    ""level"": 2,
                    ""score"": 28.2
                },
                {
                    ""id"": ""https://openalex.org/C120665830"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q14620"",
                    ""display_name"": ""Optics"",
                    ""level"": 1,
                    ""score"": 28.2
                },
                {
                    ""id"": ""https://openalex.org/C2524010"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q8087"",
                    ""display_name"": ""Geometry"",
                    ""level"": 1,
                    ""score"": 27.4
                },
                {
                    ""id"": ""https://openalex.org/C158129726"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q402"",
                    ""display_name"": ""Higgs boson"",
                    ""level"": 2,
                    ""score"": 26.9
                },
                {
                    ""id"": ""https://openalex.org/C44870925"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q37547"",
                    ""display_name"": ""Astrophysics"",
                    ""level"": 1,
                    ""score"": 26.7
                },
                {
                    ""id"": ""https://openalex.org/C127313418"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q1069"",
                    ""display_name"": ""Geology"",
                    ""level"": 0,
                    ""score"": 25.6
                },
                {
                    ""id"": ""https://openalex.org/C152290109"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q2033879"",
                    ""display_name"": ""Collider"",
                    ""level"": 2,
                    ""score"": 24.5
                },
                {
                    ""id"": ""https://openalex.org/C47085818"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q115238"",
                    ""display_name"": ""Pair production"",
                    ""level"": 2,
                    ""score"": 23.9
                },
                {
                    ""id"": ""https://openalex.org/C117137515"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q238170"",
                    ""display_name"": ""Quantum chromodynamics"",
                    ""level"": 2,
                    ""score"": 23.3
                },
                {
                    ""id"": ""https://openalex.org/C41008148"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q21198"",
                    ""display_name"": ""Computer science"",
                    ""level"": 0,
                    ""score"": 23.0
                },
                {
                    ""id"": ""https://openalex.org/C71924100"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q11190"",
                    ""display_name"": ""Medicine"",
                    ""level"": 0,
                    ""score"": 23.0
                },
                {
                    ""id"": ""https://openalex.org/C105702510"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q514"",
                    ""display_name"": ""Anatomy"",
                    ""level"": 1,
                    ""score"": 22.2
                },
                {
                    ""id"": ""https://openalex.org/C107165499"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q1366833"",
                    ""display_name"": ""Rapidity"",
                    ""level"": 3,
                    ""score"": 21.5
                },
                {
                    ""id"": ""https://openalex.org/C162324750"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q8134"",
                    ""display_name"": ""Economics"",
                    ""level"": 0,
                    ""score"": 21.3
                },
                {
                    ""id"": ""https://openalex.org/C139719470"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q39680"",
                    ""display_name"": ""Macroeconomics"",
                    ""level"": 1,
                    ""score"": 20.2
                },
                {
                    ""id"": ""https://openalex.org/C175444787"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q39072"",
                    ""display_name"": ""Microeconomics"",
                    ""level"": 1,
                    ""score"": 20.2
                },
                {
                    ""id"": ""https://openalex.org/C2778348673"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q739302"",
                    ""display_name"": ""Production (economics)"",
                    ""level"": 2,
                    ""score"": 20.2
                }
            ],
            ""counts_by_year"": [
                {
                    ""year"": 2022,
                    ""works_count"": 7,
                    ""cited_by_count"": 1040
                },
                {
                    ""year"": 2021,
                    ""works_count"": 110,
                    ""cited_by_count"": 13649
                },
                {
                    ""year"": 2020,
                    ""works_count"": 109,
                    ""cited_by_count"": 13027
                },
                {
                    ""year"": 2019,
                    ""works_count"": 155,
                    ""cited_by_count"": 14600
                },
                {
                    ""year"": 2018,
                    ""works_count"": 268,
                    ""cited_by_count"": 14708
                },
                {
                    ""year"": 2017,
                    ""works_count"": 210,
                    ""cited_by_count"": 13497
                },
                {
                    ""year"": 2016,
                    ""works_count"": 230,
                    ""cited_by_count"": 16336
                },
                {
                    ""year"": 2015,
                    ""works_count"": 215,
                    ""cited_by_count"": 14145
                },
                {
                    ""year"": 2014,
                    ""works_count"": 211,
                    ""cited_by_count"": 9997
                },
                {
                    ""year"": 2013,
                    ""works_count"": 195,
                    ""cited_by_count"": 8644
                },
                {
                    ""year"": 2012,
                    ""works_count"": 140,
                    ""cited_by_count"": 4854
                }
            ],
            ""works_api_url"": ""https://api.openalex.org/works?filter=author.id:A2410387637"",
            ""updated_date"": ""2022-03-09"",
            ""created_date"": ""2016-06-24""
        }
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>
100,000 calls per day

### b. OpenAlex
#### Link to API documentation <br>

#### API endpoint and description <br>
https://api.openalex.org/works <br>Returns publications 
#### Query Parameters <br> 

#### Return Format <br>
JSON
#### Return Fields <br>
```{
            ""id"": ""https://openalex.org/W1931972414"",
            ""doi"": ""https://doi.org/10.1109/iccv.1998.710781"",
            ""title"": ""A cubist approach to object recognition"",
            ""display_name"": ""A cubist approach to object recognition"",
            ""relevance_score"": 525.6624,
            ""publication_year"": 1998,
            ""publication_date"": ""1998-01-04"",
            ""ids"": {
                ""openalex"": ""https://openalex.org/W1931972414"",
                ""doi"": ""https://doi.org/10.1109/iccv.1998.710781"",
                ""mag"": ""1931972414""
            },
            ""host_venue"": {
                ""id"": null,
                ""issn_l"": null,
                ""issn"": null,
                ""display_name"": ""international conference on computer vision"",
                ""publisher"": ""IEEE Computer Society"",
                ""type"": ""publisher"",
                ""url"": ""https://doi.org/10.1109/iccv.1998.710781"",
                ""is_oa"": false,
                ""version"": null,
                ""license"": null
            },
            ""type"": ""proceedings-article"",
            ""open_access"": {
                ""is_oa"": false,
                ""oa_status"": ""closed"",
                ""oa_url"": null
            },
            ""authorships"": [
                {
                    ""author_position"": ""first"",
                    ""author"": {
                        ""id"": ""https://openalex.org/A2109915147"",
                        ""display_name"": ""Randal C. Nelson"",
                        ""orcid"": null
                    },
                    ""institutions"": [
                        {
                            ""id"": ""https://openalex.org/I5388228"",
                            ""display_name"": ""University of Rochester"",
                            ""ror"": ""https://ror.org/022kthw22"",
                            ""country_code"": ""US"",
                            ""type"": ""education""
                        }
                    ],
                    ""raw_affiliation_string"": ""Dept. of Comput. Sci., Rochester Univ., NY, USA#TAB#""
                },
                {
                    ""author_position"": ""last"",
                    ""author"": {
                        ""id"": ""https://openalex.org/A2059637848"",
                        ""display_name"": ""Andrea Selinger"",
                        ""orcid"": null
                    },
                    ""institutions"": [],
                    ""raw_affiliation_string"": null
                }
            ],
            ""cited_by_count"": 96,
            ""biblio"": {
                ""volume"": null,
                ""issue"": null,
                ""first_page"": ""614"",
                ""last_page"": ""621""
            },
            ""is_retracted"": false,
            ""is_paratext"": false,
            ""concepts"": [
                {
                    ""id"": ""https://openalex.org/C41008148"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q21198"",
                    ""display_name"": ""Computer science"",
                    ""level"": 0,
                    ""score"": ""0.680749""
                },
                {
                    ""id"": ""https://openalex.org/C154945302"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q11660"",
                    ""display_name"": ""Artificial intelligence"",
                    ""level"": 1,
                    ""score"": ""0.61252""
                },
                {
                    ""id"": ""https://openalex.org/C31972630"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q844240"",
                    ""display_name"": ""Computer vision"",
                    ""level"": 1,
                    ""score"": ""0.4432""
                },
                {
                    ""id"": ""https://openalex.org/C2781238097"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q175026"",
                    ""display_name"": ""Object (grammar)"",
                    ""level"": 2,
                    ""score"": ""0.397139""
                },
                {
                    ""id"": ""https://openalex.org/C64876066"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q5141226"",
                    ""display_name"": ""Cognitive neuroscience of visual object recognition"",
                    ""level"": 3,
                    ""score"": ""0.381616""
                },
                {
                    ""id"": ""https://openalex.org/C2776151529"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q3045304"",
                    ""display_name"": ""Object detection"",
                    ""level"": 3,
                    ""score"": ""0.368442""
                },
                {
                    ""id"": ""https://openalex.org/C153180895"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q7148389"",
                    ""display_name"": ""Pattern recognition (psychology)"",
                    ""level"": 2,
                    ""score"": ""0.362901""
                },
                {
                    ""id"": ""https://openalex.org/C182521987"",
                    ""wikidata"": ""https://www.wikidata.org/wiki/Q2493877"",
                    ""display_name"": ""Viola–Jones object detection framework"",
                    ""level"": 5,
                    ""score"": ""0.322733""
                }
            ],
            ""mesh"": [],
            ""alternate_host_venues"": [],
            ""referenced_works"": [
                ""https://openalex.org/W2053197265"",
                ""https://openalex.org/W2157418942"",
                ""https://openalex.org/W2113949814"",
                ""https://openalex.org/W2157837724"",
                ""https://openalex.org/W2131806657"",
                ""https://openalex.org/W2154204736"",
                ""https://openalex.org/W2100871152"",
                ""https://openalex.org/W2111371393"",
                ""https://openalex.org/W2113341759"",
                ""https://openalex.org/W2103497972""
            ],
            ""related_works"": [
                ""https://openalex.org/W2131806657"",
                ""https://openalex.org/W2057175746"",
                ""https://openalex.org/W2061511666"",
                ""https://openalex.org/W2151103935"",
                ""https://openalex.org/W2154422044"",
                ""https://openalex.org/W2033554200"",
                ""https://openalex.org/W2135884851"",
                ""https://openalex.org/W2156406284"",
                ""https://openalex.org/W1513966746"",
                ""https://openalex.org/W1553558465"",
                ""https://openalex.org/W1949116567"",
                ""https://openalex.org/W1994297893"",
                ""https://openalex.org/W2138451337"",
                ""https://openalex.org/W2124386111"",
                ""https://openalex.org/W2123977795"",
                ""https://openalex.org/W1578226009"",
                ""https://openalex.org/W2111371393"",
                ""https://openalex.org/W2914885528"",
                ""https://openalex.org/W2085207288"",
                ""https://openalex.org/W2151709124""
            ],
            ""abstract_inverted_index"": {
                ""We"": [
                    0,
                    82
                ],
                ""describe"": [
                    1
                ],
                ""an"": [
                    2,
                    53
                ],
                ""appearance-based"": [
                    3
                ],
                ""object"": [
                    4
                ],
                ""recognition"": [
                    5,
                    60
                ],
                ""system"": [
                    6,
                    57,
                    126
                ],
                ""using"": [
                    7
                ],
                ""a"": [
                    8,
                    41,
                    47,
                    62
                ],
                ""keyed,"": [
                    9
                ],
                ""multi-level"": [
                    10
                ],
                ""contest"": [
                    11,
                    50
                ],
                ""representation"": [
                    12
                ],
                ""reminiscent"": [
                    13
                ],
                ""of"": [
                    14,
                    17,
                    61,
                    64,
                    86,
                    101,
                    109,
                    119,
                    152
                ],
                ""certain"": [
                    15
                ],
                ""aspects"": [
                    16
                ],
                ""cubist"": [
                    18
                ],
                ""art."": [
                    19
                ],
                ""Specifically,"": [
                    20
                ],
                ""we"": [
                    21,
                    141
                ],
                ""utilize"": [
                    22
                ],
                ""distinctive"": [
                    23
                ],
                ""intermediate-level"": [
                    24
                ],
                ""features"": [
                    25
                ],
                ""in"": [
                    26,
                    103,
                    106,
                    146
                ],
                ""this"": [
                    27
                ],
                ""case"": [
                    28
                ],
                ""automatically"": [
                    29
                ],
                ""extracted"": [
                    30
                ],
                ""2-D"": [
                    31
                ],
                ""boundary"": [
                    32
                ],
                ""fragments,"": [
                    33
                ],
                ""as"": [
                    34
                ],
                ""keys,"": [
                    35
                ],
                ""which"": [
                    36
                ],
                ""are"": [
                    37,
                    143
                ],
                ""then"": [
                    38
                ],
                ""verified"": [
                    39
                ],
                ""within"": [
                    40,
                    46
                ],
                ""local"": [
                    42
                ],
                ""contest,"": [
                    43
                ],
                ""and"": [
                    44,
                    71,
                    76,
                    113,
                    115,
                    157
                ],
                ""assembled"": [
                    45
                ],
                ""loose"": [
                    48
                ],
                ""global"": [
                    49
                ],
                ""to"": [
                    51,
                    74
                ],
                ""evoke"": [
                    52
                ],
                ""overall"": [
                    54
                ],
                ""percept."": [
                    55
                ],
                ""This"": [
                    56
                ],
                ""demonstrates"": [
                    58
                ],
                ""good"": [
                    59
                ],
                ""variety"": [
                    63
                ],
                ""3-D"": [
                    65
                ],
                ""shapes,"": [
                    66
                ],
                ""ranging"": [
                    67
                ],
                ""from"": [
                    68
                ],
                ""sports"": [
                    69
                ],
                ""cars"": [
                    70
                ],
                ""fighter"": [
                    72
                ],
                ""planes"": [
                    73
                ],
                ""snakes"": [
                    75
                ],
                ""lizards"": [
                    77
                ],
                ""with"": [
                    78,
                    98,
                    155
                ],
                ""full"": [
                    79
                ],
                ""orthographic"": [
                    80
                ],
                ""invariance."": [
                    81
                ],
                ""report"": [
                    83,
                    142
                ],
                ""the"": [
                    84,
                    104,
                    107,
                    117,
                    125,
                    139,
                    144,
                    147
                ],
                ""results"": [
                    85,
                    118,
                    140
                ],
                ""large-scale"": [
                    87
                ],
                ""tests,"": [
                    88
                ],
                ""involving"": [
                    89
                ],
                ""over"": [
                    90
                ],
                ""2000"": [
                    91
                ],
                ""separate"": [
                    92
                ],
                ""test"": [
                    93
                ],
                ""images,"": [
                    94
                ],
                ""that"": [
                    95
                ],
                ""evaluate"": [
                    96
                ],
                ""performance"": [
                    97
                ],
                ""increasing"": [
                    99
                ],
                ""number"": [
                    100
                ],
                ""items"": [
                    102
                ],
                ""database,"": [
                    105
                ],
                ""presence"": [
                    108
                ],
                ""clutter,"": [
                    110
                ],
                ""background"": [
                    111
                ],
                ""change,"": [
                    112
                ],
                ""occlusion,"": [
                    114
                ],
                ""also"": [
                    116
                ],
                ""some"": [
                    120
                ],
                ""generic"": [
                    121
                ],
                ""classification"": [
                    122
                ],
                ""experiments"": [
                    123
                ],
                ""where"": [
                    124
                ],
                ""is"": [
                    127
                ],
                ""tested"": [
                    128
                ],
                ""on"": [
                    129
                ],
                ""objects"": [
                    130
                ],
                ""never"": [
                    131
                ],
                ""previously"": [
                    132
                ],
                ""seen"": [
                    133
                ],
                ""or"": [
                    134
                ],
                ""modeled."": [
                    135
                ],
                ""To"": [
                    136
                ],
                ""our"": [
                    137
                ],
                ""knowledge,"": [
                    138
                ],
                ""best"": [
                    145
                ],
                ""literature"": [
                    148
                ],
                ""for"": [
                    149
                ],
                ""full-sphere"": [
                    150
                ],
                ""tests"": [
                    151
                ],
                ""general"": [
                    153
                ],
                ""shapes"": [
                    154
                ],
                ""occlusion"": [
                    156
                ],
                ""clutter"": [
                    158
                ],
                ""resistance."": [
                    159
                ]
            },
            ""cited_by_api_url"": ""https://api.openalex.org/works?filter=cites:W1931972414"",
            ""counts_by_year"": [
                {
                    ""year"": 2020,
                    ""cited_by_count"": 2
                },
                {
                    ""year"": 2017,
                    ""cited_by_count"": 1
                },
                {
                    ""year"": 2016,
                    ""cited_by_count"": 1
                },
                {
                    ""year"": 2015,
                    ""cited_by_count"": 2
                },
                {
                    ""year"": 2014,
                    ""cited_by_count"": 3
                },
                {
                    ""year"": 2013,
                    ""cited_by_count"": 5
                },
                {
                    ""year"": 2012,
                    ""cited_by_count"": 5
                }
            ],
            ""updated_date"": ""2021-12-23"",
            ""created_date"": ""2016-06-24""
        }
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>
100,000 calls per day

### 21.IEEE Explorer
#### Link to API documentation <br>
https://developer.ieee.org/doc
#### API endpoint and description <br>
https://ieeexploreapi.ieee.org/api/v1/search/articles <br>Returns matched publications metadata
#### Query Parameters <br> 

#### Return Format <br>

#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>
Request for API key still pending
#### Rate <br>
10 calls per second, 200 calls per day

### 22.ACM or CrossRef
#### Link to API documentation <br>
NO API found. Alternate is to use CrossRef
#### API endpoint and description <br>
https://api.crossref.org/works <br>Searches records that match query
#### Query Parameters <br> 
title, author
#### Return Format <br>
JSON
#### Return Fields <br>
```{
                ""indexed"": {
                    ""date-parts"": [
                        [
                            2022,
                            4,
                            2
                        ]
                    ],
                    ""date-time"": ""2022-04-02T01:52:49Z"",
                    ""timestamp"": 1648864369152
                },
                ""update-to"": [
                    {
                        ""updated"": {
                            ""date-parts"": [
                                [
                                    2018,
                                    1,
                                    1
                                ]
                            ],
                            ""date-time"": ""2018-01-01T00:00:00Z"",
                            ""timestamp"": 1514764800000
                        },
                        ""DOI"": ""10.5555/12345678"",
                        ""type"": ""corrigendum"",
                        ""label"": ""Corrigendum""
                    }
                ],
                ""reference-count"": 1,
                ""publisher"": ""Test accounts"",
                ""issue"": ""11"",
                ""license"": [
                    {
                        ""start"": {
                            ""date-parts"": [
                                [
                                    2011,
                                    11,
                                    21
                                ]
                            ],
                            ""date-time"": ""2011-11-21T00:00:00Z"",
                            ""timestamp"": 1321833600000
                        },
                        ""content-version"": ""tdm"",
                        ""delay-in-days"": 1195,
                        ""URL"": ""http://psychoceramicsproprietrylicenseV1.com""
                    },
                    {
                        ""start"": {
                            ""date-parts"": [
                                [
                                    2011,
                                    11,
                                    21
                                ]
                            ],
                            ""date-time"": ""2011-11-21T00:00:00Z"",
                            ""timestamp"": 1321833600000
                        },
                        ""content-version"": ""vor"",
                        ""delay-in-days"": 1195,
                        ""URL"": ""http://psychoceramicsproprietrylicenseV1.com""
                    },
                    {
                        ""start"": {
                            ""date-parts"": [
                                [
                                    2011,
                                    11,
                                    21
                                ]
                            ],
                            ""date-time"": ""2011-11-21T00:00:00Z"",
                            ""timestamp"": 1321833600000
                        },
                        ""content-version"": ""am"",
                        ""delay-in-days"": 1195,
                        ""URL"": ""http://psychoceramicsproprietrylicenseV1.com""
                    },
                    {
                        ""start"": {
                            ""date-parts"": [
                                [
                                    2022,
                                    2,
                                    1
                                ]
                            ],
                            ""date-time"": ""2022-02-01T00:00:00Z"",
                            ""timestamp"": 1643673600000
                        },
                        ""content-version"": ""stm-asf"",
                        ""delay-in-days"": 4920,
                        ""URL"": ""https://doi.org/10.15223/policy-001""
                    }
                ],
                ""funder"": [
                    {
                        ""DOI"": ""10.13039/100000001"",
                        ""name"": ""National Science Foundation"",
                        ""doi-asserted-by"": ""publisher"",
                        ""award"": [
                            ""12345678""
                        ]
                    },
                    {
                        ""DOI"": ""10.13039/100006151"",
                        ""name"": ""Basic Energy Sciences, Office of Science, U.S. Department of Energy"",
                        ""doi-asserted-by"": ""publisher"",
                        ""award"": [
                            ""12345679""
                        ]
                    }
                ],
                ""content-domain"": {
                    ""domain"": [
                        ""psychoceramics.labs.crossref.org""
                    ],
                    ""crossmark-restriction"": false
                },
                ""chair"": [
                    {
                        ""name"": ""Friends of Josiah Carberry"",
                        ""sequence"": ""additional"",
                        ""affiliation"": []
                    }
                ],
                ""short-container-title"": [
                    ""Journal of Psychoceramics""
                ],
                ""published-print"": {
                    ""date-parts"": [
                        [
                            2008,
                            8,
                            14
                        ]
                    ]
                },
                ""abstract"": ""<jats:p>The characteristic theme of the works of Stone is the bridge between culture and society. Several narratives concerning the fatal !aw, and subsequent dialectic, of semioticist class may be found. Thus, Debord uses the term ‘the subtextual paradigm of consensus’ to denote a cultural paradox. The subject is interpolated into a neocultural discourse that includes sexuality as a totality. But Marx’s critique of prepatriarchialist nihilism states that consciousness is capable of signi\""cance. The main theme of Dietrich’s[1]model of cultural discourse is not construction, but neoconstruction. Thus, any number of narratives concerning the textual paradigm of narrative exist. Pretextual cultural theory suggests that context must come from the collective unconscious.</jats:p>"",
                ""DOI"": ""10.5555/12345678"",
                ""type"": ""journal-article"",
                ""created"": {
                    ""date-parts"": [
                        [
                            2011,
                            11,
                            9
                        ]
                    ],
                    ""date-time"": ""2011-11-09T14:42:05Z"",
                    ""timestamp"": 1320849725000
                },
                ""page"": ""1-3"",
                ""update-policy"": ""http://dx.doi.org/10.5555/something"",
                ""source"": ""Crossref"",
                ""is-referenced-by-count"": 3,
                ""title"": [
                    ""Toward a Unified Theory of High-Energy Metaphysics: Silly String Theory""
                ],
                ""prefix"": ""10.5555"",
                ""volume"": ""5"",
                ""clinical-trial-number"": [
                    {
                        ""clinical-trial-number"": ""isrctn12345"",
                        ""registry"": ""10.18810/isrctn""
                    }
                ],
                ""author"": [
                    {
                        ""ORCID"": ""http://orcid.org/0000-0002-1825-0097"",
                        ""authenticated-orcid"": false,
                        ""suffix"": ""Jr."",
                        ""given"": ""Josiah"",
                        ""family"": ""Carberry"",
                        ""sequence"": ""first"",
                        ""affiliation"": [
                            {
                                ""name"": ""Department of Psychoceramics, Brown University""
                            }
                        ]
                    }
                ],
                ""member"": ""7822"",
                ""published-online"": {
                    ""date-parts"": [
                        [
                            2008,
                            8,
                            13
                        ]
                    ]
                },
                ""container-title"": [
                    ""Journal of Psychoceramics""
                ],
                ""language"": ""en"",
                ""link"": [
                    {
                        ""URL"": ""http://psychoceramics.labs.crossref.org/10.5555-12345678.html"",
                        ""content-type"": ""unspecified"",
                        ""content-version"": ""vor"",
                        ""intended-application"": ""similarity-checking""
                    }
                ],
                ""deposited"": {
                    ""date-parts"": [
                        [
                            2022,
                            3,
                            13
                        ]
                    ],
                    ""date-time"": ""2022-03-13T11:15:56Z"",
                    ""timestamp"": 1647170156000
                },
                ""score"": 70.83164,
                ""resource"": {
                    ""primary"": {
                        ""URL"": ""https://sandbox.publicknowledgeproject.org/index.php/jpc/article/view/497""
                    }
                },
                ""issued"": {
                    ""date-parts"": [
                        [
                            2008,
                            8,
                            13
                        ]
                    ]
                },
                ""references-count"": 1,
                ""journal-issue"": {
                    ""issue"": ""11"",
                    ""published-online"": {
                        ""date-parts"": [
                            [
                                2008,
                                2,
                                29
                            ]
                        ]
                    },
                    ""published-print"": {
                        ""date-parts"": [
                            [
                                2008,
                                2,
                                29
                            ]
                        ]
                    }
                },
                ""URL"": ""http://dx.doi.org/10.5555/12345678"",
                ""archive"": [
                    ""CLOCKSS""
                ],
                ""relation"": {
                    ""is-reply-to"": [
                        {
                            ""id-type"": ""doi"",
                            ""id"": ""10.5555/24242424x"",
                            ""asserted-by"": ""subject""
                        }
                    ]
                },
                ""ISSN"": [
                    ""0264-3561""
                ],
                ""issn-type"": [
                    {
                        ""value"": ""0264-3561"",
                        ""type"": ""electronic""
                    }
                ],
                ""published"": {
                    ""date-parts"": [
                        [
                            2008,
                            8,
                            13
                        ]
                    ]
                },
                ""assertion"": [
                    {
                        ""URL"": ""http://orcid.org/0000-0002-1825-0097"",
                        ""order"": 0,
                        ""name"": ""orcid"",
                        ""label"": ""ORCID"",
                        ""explanation"": {
                            ""URL"": ""IDs for Or""
                        }
                    },
                    {
                        ""value"": ""2012-07-24"",
                        ""order"": 0,
                        ""name"": ""received"",
                        ""label"": ""Received"",
                        ""group"": {
                            ""name"": ""publication_history"",
                            ""label"": ""Publication History""
                        }
                    },
                    {
                        ""value"": ""2012-08-29"",
                        ""order"": 1,
                        ""name"": ""accepted"",
                        ""label"": ""Accepted"",
                        ""group"": {
                            ""name"": ""publication_history"",
                            ""label"": ""Publication History""
                        }
                    },
                    {
                        ""value"": ""2012-09-26"",
                        ""order"": 2,
                        ""name"": ""published_online"",
                        ""label"": ""Published Online"",
                        ""group"": {
                            ""name"": ""publication_history"",
                            ""label"": ""Publication History""
                        }
                    },
                    {
                        ""value"": ""2012-10-27"",
                        ""order"": 3,
                        ""name"": ""published_print"",
                        ""label"": ""Published Print"",
                        ""group"": {
                            ""name"": ""publication_history"",
                            ""label"": ""Publication History""
                        }
                    },
                    {
                        ""URL"": ""http://psychoceramics.labs.crossref.org/10.5555-12345678.html"",
                        ""order"": 0,
                        ""name"": ""peer_reviewed"",
                        ""label"": ""Peer reviewed"",
                        ""explanation"": {
                            ""URL"": ""thrice""
                        },
                        ""group"": {
                            ""name"": ""peer_review"",
                            ""label"": ""Peer review""
                        }
                    },
                    {
                        ""URL"": ""http://www.silly-string.com/silly-info/index.cfm"",
                        ""order"": 0,
                        ""name"": ""supplementary_Material"",
                        ""label"": ""Supplementary Material"",
                        ""explanation"": {
                            ""URL"": ""Helpful Silly String resource""
                        }
                    },
                    {
                        ""URL"": ""http://psychoceramics.labs.crossref.org/10.5555-12345678.html"",
                        ""order"": 0,
                        ""name"": ""licensing"",
                        ""label"": ""Licensing Information"",
                        ""explanation"": {
                            ""URL"": ""Complicated license information available""
                        },
                        ""group"": {
                            ""name"": ""copyright_licensing"",
                            ""label"": ""Copyright & Licensing""
                        }
                    },
                    {
                        ""URL"": ""http://psychoceramics.labs.crossref.org/10.5555-12345678.html"",
                        ""order"": 1,
                        ""name"": ""copyright_statement"",
                        ""label"": ""Copyright Statement"",
                        ""explanation"": {
                            ""URL"": ""Lorem Copyrightsum""
                        },
                        ""group"": {
                            ""name"": ""copyright_licensing"",
                            ""label"": ""Copyright & Licensing""
                        }
                    }
                ]
            }
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>


### 23.Academic Search/ EBSCO
#### Link to API documentation <br>
https://connect.ebsco.com/s/article/EBSCOhost-API?language=en_US
#### API endpoint and description <br>
http://eit.ebscohost.com/Services/SearchService.asmx/Search <br>Returns record metadata that match term
#### Query Parameters <br> 
keyword, database
#### Return Format <br>
XML
#### Return Fields <br>
```recordID=""xs:int"">
            <pdfLink></pdfLink>
            <pubinfo></pubinfo>
            <aug></aug>
            <su></su>
            <ab></ab>
            <atl></atl>
            <abody></abody>
         </rec>
```
#### API Key? <br>required profile
#### Subscription <br>

#### Comments <br>
Request for Profile
#### Rate <br>

### 24.DOAJ
#### Link to API documentation <br>
https://doaj.org/api/docs
#### API endpoint and description <br>
https://doaj.org/api/search/articles/{search_query} <br>Returns records that match search query
#### Query Parameters <br> 
keywrod (title search), instituition, author
#### Return Format <br>
JSON
#### Return Fields <br>
```{
            ""last_updated"": ""2022-03-15T14:16:30Z"",
            ""bibjson"": {
                ""identifier"": [
                    {
                        ""id"": ""2228-5806"",
                        ""type"": ""pissn""
                    },
                    {
                        ""id"": ""2228-5814"",
                        ""type"": ""eissn""
                    }
                ],
                ""journal"": {
                    ""volume"": ""15"",
                    ""number"": ""4"",
                    ""country"": ""IR"",
                    ""issns"": [
                        ""2228-5806"",
                        ""2228-5814""
                    ],
                    ""publisher"": ""Royan Institute (ACECR), Tehran"",
                    ""language"": [
                        ""EN""
                    ],
                    ""title"": ""Cell Journal""
                },
                ""end_page"": ""293"",
                ""keywords"": [
                    ""In vitro Maturation"",
                    ""Oocyte"",
                    ""Hydrostatic Pressure"",
                    ""Apoptosis"",
                    ""Mouse""
                ],
                ""year"": ""2013"",
                ""start_page"": ""282"",
                ""subject"": [
                    {
                        ""code"": ""R"",
                        ""scheme"": ""LCC"",
                        ""term"": ""Medicine""
                    },
                    {
                        ""code"": ""Q"",
                        ""scheme"": ""LCC"",
                        ""term"": ""Science""
                    }
                ],
                ""author"": [
                    {
                        ""name"": ""Isac Karimi""
                    },
                    {
                        ""name"": ""Ali Amini""
                    },
                    {
                        ""name"": ""Mehri Azadbakht""
                    },
                    {
                        ""name"": ""Zahra Rashidi""
                    }
                ],
                ""link"": [
                    {
                        ""type"": ""fulltext"",
                        ""url"": ""http://celljournal.org/library/upload/article/af_4242286323327245323625234522626624742334Rashidi-1.pdf""
                    }
                ],
                ""abstract"": ""Objective: This study examines the effects of hydrostatic pressure on in vitro maturation (IVM) of oocytes derived from in vitro grown follicles.Materials and Methods: In this experimental study, preantral follicles were isolated from 12-day-old female NMRI mice. Each follicle was cultured individually in Alpha Minimal Essential Medium (α-MEM) under mineral oil for 12 days. Then, follicles were induced for IVM and divided into two groups, control and experiment. In the experiment group follicles were subjected to 20 mmHg pressure for 30 minutes and cultured for 24-48 hours. We assessed for viability and IVM of the oocytes. The percentage of apoptosis in cumulus cells was determined by the TUNEL assay. A comparison between groups was made using the student’s t test.Results: The percentage of metaphase II oocytes (MII) increased in hydrostatic pressure-treated follicles compared to controls (p<0.05). Cumulus cell viability reduced in hydrostatic pressure-treated follicles compared to controls (p<0.05). Exposure of follicles to pressure increased apoptosis in cumulus cells compared to controls (p<0.05).Conclusion: Hydrostatic pressure, by inducing apoptosis in cumulus cells, participates in the cumulus oocyte coupled relationship with oocyte maturation."",
                ""title"": ""Hydrostatic Pressure Affects In Vitro Maturation of Oocytes and Follicles and Increases Granulosa Cell Death""
            },
            ""created_date"": ""2013-11-20T07:00:09Z"",
            ""id"": ""00001cb7350c4c5ba3cefe297098f736""
        },
```
#### API Key? <br>
#### Subscription <br>

#### Comments <br>

#### Rate <br>

### 24.b. DOAJ
#### Link to API documentation <br>
https://doaj.org/api/docs

#### API endpoint and description <br>
https://doaj.org/api/search/journals/{search_query} <br>Returns records that match search query
#### Query Parameters <br> 
keyword ( title, abstract search), instituition, author
#### Return Format <br>
JSOn
#### Return Fields <br>
```{
            ""id"": ""0f0d806c37d84e3c89f5636bb3bdd5dd"",
            ""created_date"": ""2020-03-02T13:17:25Z"",
            ""last_updated"": ""2021-04-29T13:14:22Z"",
            ""bibjson"": {
                ""boai"": true,
                ""eissn"": ""2659-3580"",
                ""publication_time_weeks"": 6,
                ""title"": ""Journal of Tourism and Heritage Research"",
                ""oa_start"": 2018,
                ""apc"": {
                    ""has_apc"": false,
                    ""url"": ""http://www.jthr.es/index.php/journal/information/authors""
                },
                ""article"": {
                    ""license_display"": [
                        ""No""
                    ]
                },
                ""copyright"": {
                    ""author_retains"": false
                },
                ""deposit_policy"": {
                    ""has_policy"": true,
                    ""service"": [
                        ""Dulcinea""
                    ]
                },
                ""editorial"": {
                    ""review_url"": ""http://www.jthr.es/index.php/journal/about"",
                    ""board_url"": ""http://www.jthr.es/index.php/journal/about/editorialTeam"",
                    ""review_process"": [
                        ""Double blind peer review""
                    ]
                },
                ""institution"": {
                    ""name"": ""INVESTUR (Asociaciones de Investigaciones y Estudios de Turismo)""
                },
                ""other_charges"": {
                    ""has_other_charges"": false,
                    ""url"": ""http://www.jthr.es/index.php/journal/information/authors""
                },
                ""pid_scheme"": {
                    ""has_pid_scheme"": false
                },
                ""plagiarism"": {
                    ""detection"": false
                },
                ""preservation"": {
                    ""has_preservation"": false
                },
                ""publisher"": {
                    ""name"": ""INVESTUR (Asociaciones de Investigaciones y Estudios de Turismo)"",
                    ""country"": ""ES""
                },
                ""ref"": {
                    ""oa_statement"": ""http://www.jthr.es/index.php/journal/OpenAccessPolicy"",
                    ""journal"": ""http://www.jthr.es"",
                    ""aims_scope"": ""http://www.jthr.es/index.php/journal/about"",
                    ""author_instructions"": ""http://www.jthr.es/index.php/journal/about/submissions"",
                    ""license_terms"": ""http://www.jthr.es/index.php/journal/about""
                },
                ""waiver"": {
                    ""has_waiver"": false
                },
                ""keywords"": [
                    ""tourism management of unesco;cultural tourism policies;"",
                    ""the different segments of cultural tourism;"",
                    ""tourist marketing;"",
                    ""tourism""
                ],
                ""language"": [
                    ""EN"",
                    ""ES""
                ],
                ""license"": [
                    {
                        ""type"": ""CC BY-NC-ND"",
                        ""BY"": true,
                        ""NC"": true,
                        ""ND"": true,
                        ""SA"": false
                    }
                ],
                ""subject"": [
                    {
                        ""code"": ""TX901-946.5"",
                        ""scheme"": ""LCC"",
                        ""term"": ""Hospitality industry. Hotels, clubs, restaurants, etc. Food service""
                    },
                    {
                        ""code"": ""GV1-1860"",
                        ""scheme"": ""LCC"",
                        ""term"": ""Recreation. Leisure""
                    },
                    {
                        ""code"": ""DP1-402"",
                        ""scheme"": ""LCC"",
                        ""term"": ""History of Spain""
                    }
                ]
            },
            ""admin"": {
                ""seal"": false,
                ""ticked"": true
            }
        }
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>

#### Rate <br>
No rate limit mentioned for downloading data
"
"### 25.Google Scholar
#### Link to API documentation <br>
https://serpapi.com/google-scholar-organic-results
#### API endpoint and description <br>
https://serpapi.com/search?engine=google_scholar <br>
#### Query Parameters <br> 

#### Return Format <br>
JSON
#### Return Fields <br>
```
```
#### API Key? <br>required
#### Subscription <br>

#### Comments <br>

#### Rate <br>
100 searches per month
"

### 26.OApen
#### Link to API documentation <br>
https://www.oapen.org/article/8185269-search-using-a-rest-api
#### API endpoint and description <br>
 <br>Returns records that match query term
#### Query Parameters <br> 
keyword
#### Return Format <br>
JSON
#### Return Fields <br>
```{
        ""uuid"": ""eb439769-e370-4c55-9195-ed3f0de9f258"",
        ""name"": ""Chapter 5 Mercury Tonics (Rasāyana) in Sanskrit Medical Literature"",
        ""handle"": ""20.500.12657/29633"",
        ""type"": ""item"",
        ""expand"": [
            ""metadata"",
            ""parentCollection"",
            ""parentCollectionList"",
            ""parentCommunityList"",
            ""bitstreams"",
            ""all""
        ],
        ""lastModified"": ""2021-11-12 16:16:16.735"",
        ""parentCollection"": null,
        ""parentCollectionList"": null,
        ""parentCommunityList"": null,
        ""bitstreams"": null,
        ""archived"": ""true"",
        ""withdrawn"": ""false"",
        ""link"": ""/rest/items/eb439769-e370-4c55-9195-ed3f0de9f258"",
        ""metadata"": null
    }
```
#### API Key? <br>not required
#### Subscription <br>

#### Comments <br>
Does not contain required fields 
#### Rate <br>
