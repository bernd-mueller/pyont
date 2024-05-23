---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

The Python Ontology Project makes use of the python libraries rdflib and OwlReady2 for processing
graphs in RDF and OWL format. rdflib incorporates methods for processing SPARQL queries on RDF.
The OwlReady2 provides features to describe classes with their properties in OWL format. Examples
for each of the libraries are implemented in the package de.zbmed.semtec.pyont.

This repository is maintained by
<ul>
{% for member in site.data.members %}
  <li>
    <a href="https://github.com/{{ member.github }}">
      {{ member.name }}
    </a>
  </li>
{% endfor %}
</ul>