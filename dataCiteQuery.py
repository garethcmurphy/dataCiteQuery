#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

_transport = RequestsHTTPTransport(
    url='https://api.datacite.org/graphql',
    use_json=True,
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)
query = gql( """{
   researcher(id: "https://orcid.org/0000-0003-1419-2405") {
    id
    name
    publications(first: 50) {
      totalCount
      nodes {
        id
        relatedIdentifiers {
          relatedIdentifier
        }
      }
    }
  }
}""")
data=client.execute(query)
print(data["researcher"]["name"])

#print(data.researcher.name)


# In[8]:


print(data["researcher"]["publications"]["totalCount"])


# In[9]:



publications=pd.DataFrame(data["researcher"]["publications"]["nodes"])


# In[10]:


mylist=publications['id'].map(lambda x: x[16:])
catlist=",".join(mylist[1:20])




# In[11]:


import requests
contents = requests.get(
    "https://api.datacite.org/dois?style=apa&page[size]=250&sort=created&ids="+catlist,
    headers={'Accept': "text/x-bibliography"},
)


# In[12]:


from IPython.display import display, Markdown, Latex
display(Markdown('## Publications'))
display(Markdown(contents.text))


# In[ ]:




