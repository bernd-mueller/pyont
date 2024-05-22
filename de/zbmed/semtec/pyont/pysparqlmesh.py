import json
from sys import getsizeof
from rdflib import RDFS, Graph, Literal, URIRef
from rdflib.namespace import RDF
from pandas import DataFrame

from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML, RDF


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
    
    sparql.setReturnFormat(JSON)
    print(sparql)
    results = sparql.query().convert()
    
    g = Graph()
    d = URIRef("http://id.nlm.nih.gov/mesh/D015242")
    a = URIRef("http://id.nlm.nih.gov/mesh/vocab#pharmacologicalAction")

    print ("--- ", results)
    for result in results["results"]["bindings"]:
        pa = URIRef(result["pa"]["value"])
        print("pa: ", pa)
        paLabel = Literal(result["paLabel"]["value"])
        print("paLabel: ", paLabel)
        g.add((d, a, pa))
        g.add((pa, RDFS.label, paLabel))

    print("--- Printing RDF ---")
    print(g.serialize(format="turtle"))
    
def conductQuery ():
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

    g = Graph()
    q = """
        SELECT *
        WHERE {
                SERVICE <http://id.nlm.nih.gov/mesh/sparql> {
                    mesh:D015242 meshv:pharmacologicalAction ?pa .
                    ?pa rdfs:label ?paLabel .
                }
        }         
    """
    qres = g.query(pref + q)

    print(qres.bindings)
    #for row in qres:
    #    print(row.s)


if __name__ == '__main__':
    wrapperQuery()
    # conductQuery()