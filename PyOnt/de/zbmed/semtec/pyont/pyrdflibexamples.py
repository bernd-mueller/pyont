'''
Created on 06.05.2024

@author: Muellerb
'''

from rdflib import Graph

def firstExample():
    # Create a Graph
    g = Graph()
    
    # Parse in an RDF file hosted on the Internet
    g.parse("http://www.w3.org/People/Berners-Lee/card")
    
    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
           raise Exception("It better be!")
    
    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.
    
    # Print out the entire Graph in the RDF Turtle format
    print(g.serialize(format="turtle"))

def secondExample():
    # Create a Graph, pare in Internet data
    g = Graph().parse("http://www.w3.org/People/Berners-Lee/card")
    
    # Query the data in g using SPARQL
    # This query returns the 'name' of all ``foaf:Person`` instances
    q = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    
        SELECT ?name
        WHERE {
            ?p rdf:type foaf:Person .
    
            ?p foaf:name ?name .
        }
    """
    
    # Apply the query to the graph and iterate through results
    for r in g.query(q):
        print(r["name"])
    
    # prints: Timothy Berners-Lee
    
if __name__ == '__main__':
    # firstExample()
    secondExample()