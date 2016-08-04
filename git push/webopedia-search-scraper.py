

import requests
from bs4 import BeautifulSoup
x=raw_input("Enter a term... : ")
r = requests.get("http://www.webopedia.com/sgsearch/results?cx=partner-pub-8768004398756183:6766915980&cof=FORID:10&ie=UTF-8&q="+x)
html=r.content
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select('#search_results_main_column .result_container p p')
for link in bsObj:
    print link.get_text()
    #break
