'''
Created on 07.05.2024

@author: Muellerb
'''

from owlready2 import *

def firstExample():
    onto = get_ontology("http://test.org/onto.owl")
    with onto:
        class Drug(Thing):
            def get_per_tablet_cost(self):
                return self.cost / self.number_of_tablets
    
        class has_for_cost(Drug >> float, FunctionalProperty):
             python_name = "cost"
    
        class has_for_number_of_tablets(Drug >> int, FunctionalProperty):
             python_name = "number_of_tablets"
    
    my_drug = Drug(cost = 10.0, number_of_tablets = 5)
    print(my_drug.get_per_tablet_cost())
    

if __name__ == '__main__':
    firstExample()