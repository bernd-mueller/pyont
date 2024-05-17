from rdflib import Graph
from pandas import DataFrame

from SPARQLWrapper import SPARQLWrapper, JSON

def wrapperQuery ():
    pref = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
        PREFIX mesh: <http://id.nlm.nih.gov/mesh/>
        PREFIX mesh2024: <http://id.nlm.nih.gov/mesh/2024/>
        PREFIX mesh2023: <http://id.nlm.nih.gov/mesh/2023/>
        PREFIX mesh2022: <http://id.nlm.nih.gov/mesh/2022/>
        """
    sparql = SPARQLWrapper("http://id.nlm.nih.gov/mesh/sparql")
    sparql.setQuery(pref + """        
        SELECT * 
        FROM <http://id.nlm.nih.gov/mesh>
        WHERE {
          mesh:D015242 meshv:pharmacologicalAction ?pa .
          ?pa rdfs:label ?paLabel .
        }         
    """)
    
    print(sparql)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    print (results)
    for result in results["results"]["bindings"]:
        print(result)
    
    
    
def conductQuery ():
    print('asd')
    g = Graph()
    qres = g.query(
        """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
        PREFIX mesh: <http://id.nlm.nih.gov/mesh/>
        PREFIX mesh2024: <http://id.nlm.nih.gov/mesh/2024/>
        PREFIX mesh2023: <http://id.nlm.nih.gov/mesh/2023/>
        PREFIX mesh2022: <http://id.nlm.nih.gov/mesh/2022/>
        
        SELECT distinct ?d ?dLabel 
        FROM <http://id.nlm.nih.gov/mesh>
        WHERE {
          ?d meshv:allowableQualifier ?q .
          ?q rdfs:label 'adverse effects'@en . 
          ?d rdfs:label ?dLabel . 
        } 
        ORDER BY ?dLabel 
        """
    )
    print(qres)


if __name__ == '__main__':
    wrapperQuery()
    #conductQuery()