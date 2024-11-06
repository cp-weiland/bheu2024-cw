import sys

from rdflib import Graph, Namespace, URIRef

g = Graph()
#g.parse(sys.argv[1], format="json-ld", base=URIRef("http://biohackathon-europe.org/openml/croissant"))
g.parse(sys.argv[1], format="json-ld", base=URIRef("http://biohackathon-europe.org/openml/croissant"))
g.serialize(destination="./openml.ttl", format='turtle')

