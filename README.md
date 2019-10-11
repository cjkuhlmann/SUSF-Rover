# SUSF-Rover

This version uses a binary tree to hold all values. 
I have no idea whether this is better but binary trees by nature are quite efficient.
The tree also allows efficient searching of data and easy fina and replacement of it.
Additionally since all variable names are stored in the control state modification of keymappings will
be quite easy in a gui and so will being able to get all data from the tree.

~~Still need to implement pre-, in- and post- order traversals although they may not be necessary.

~~```python    #------------------------------------------------------------------CREATE NETWORK STRING-------------------------------------
    def create_network_string(self):
        output = ""
        for name in self.names:
            value = find_replace(self.root,name)
            if value != 0:
                output += name + "," + str(value) + ";"
            return output
```
~~This code will likely be more efficient with a traversal e.g. pre-order but the find_replace function would not be available to use unless an additional paramater is added to return the name when necessary too.
