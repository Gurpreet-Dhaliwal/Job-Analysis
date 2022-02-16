from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
This method is used to extract all data items from
the XML file
Arguments:
    url -> Url for the job site
    query -> Search key
    items -> Attributes to fetch
"""
def extract_xml_data(url, query, items):
    final_url = create_url(url, query)
    url_xml = urlopen(final_url)
    xml = url_xml.read()
    url_xml.close()
    data  = []

    soup_page = BeautifulSoup(xml,features="lxml")
    for list in soup_page.findAll("item"):
        attrs = {}
        for item in items:
            attrs[item] = "" if not list.find(item) else list.find(item).text
        data.append(attrs)

    return data

def create_url(url, query):
    query = query.replace(" ", "%20%")
    return url + query

"""
if __name__ == "__main__":
    # Testing the xml parser
    url= "http://rss.jobsearch.monster.com/rssquery.ashx?q=" # monster
    query= "engineer"
    item = ["title", "description", "link", "guid", "pubdate"]
    print(extract_xml_data(url, query, item))
    
    url = "https://rss.indeed.com/rss?q=" # indeed
    query = "engineer"
    item = ["title", "link", "source", "guid", "pubdate", "description", "georss"]
    print(extract_xml_data(url, query, item))
"""