#!/usr/bin/env python3

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

df=pd.DataFrame(data["researcher"]["publications"]["nodes"])
print(df)
#print(data.researcher.name)
