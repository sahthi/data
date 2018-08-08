def serializable_object(node):
    "Recurse into tree to build a serializable object"
    obj = {'name': node.testcase_name, 'id': node.pk, 'children': []}
    for child in node.get_children():
        obj['children'].append(serializable_object(child))
    return obj
import json

obj = {'name': 'DM', 'id': 10, 'children': [{'name': 'INIT', 'id': 11, 'children': [{'name': 'BLE', 'id': 22, 'children': [{'name': 'BLE discover', 'id': 23, 'children': [{'name': 'BLE get', 'id': 25, 'children': []}, {'name': 'BLE observe', 'id': 24, 'children': []}, {'name': 'BLE put', 'id': 26, 'children': []}]}]}, {'name': 'Bluetooth', 'id': 17, 'children': [{'name': ' BluetBLE ooth discover', 'id': 18, 'children': [{'name': 'Bluetooth get', 'id': 20, 'children': []}, {'name': 'Bluetooth observe', 'id': 19, 'children': []}, {'name': 'Bluetooth put', 'id': 21, 'children': []}]}]}, {'name': 'IP', 'id': 12, 'children': [{'name': 'IP discover', 'id': 13, 'children': [{'name': 'IP get', 'id': 15, 'children': []}, {'name': 'IP observe', 'id': 14, 'children': []}, {'name': 'IP put', 'id': 16, 'children': []}]}]}]}]}
print(json.dumps(obj))

{"name": "DM", "id": 10, "children": [{"name": "INIT", "id": 11, "children": [{"name": "BLE", "id": 22, "children": [{"name": "BLE discover", "id": 23, "children": [{"name": "BLE get", "id": 25, "children": []}, {"name": "BLE observe", "id": 24, "children": []}, {"name": "BLE put", "id": 26, "children": []}]}]}, {"name": "Bluetooth", "id": 17, "children": [{"name": " BluetBLE ooth discover", "id": 18, "children": [{"name": "Bluetooth get", "id": 20, "children": []}, {"name": "Bluetooth observe", "id": 19, "children": []}, {"name": "Bluetooth put", "id": 21, "children": []}]}]}, {"name": "IP", "id": 12, "children": [{"name": "IP discover", "id": 13, "children": [{"name": "IP get", "id": 15, "children": []}, {"name": "IP observe", "id": 14, "children": []}, {"name": "IP put", "id": 16, "children": []}]}]}]}]}

Node.objects.get_queryset_descendants(my_queryset, include_self=False)
get_queryset_ancestors(queryset, include_self=False)

from django.db.models import Q 
   import operator 
   def get_queryset_descendants(nodes, include_self=False): 
       if not nodes: 
           return Node.tree.none() 
       filters = [] 
       for n in nodes: 
           lft, rght = n.lft, n.rght 
           if include_self: 
               lft -=1 
               rght += 1 
           filters.append(Q(tree_id=n.tree_id, lft__gt=lft, rght__lt=rght)) 
       q = reduce(operator.or_, filters) 
       return Node.tree.filter(q) 


T1 
---T1.1 
---T1.2 
T2 
T3 
---T3.3 
------T3.3.3 
Example usage:

   >> some_nodes = [<Node: T1>, <Node: T2>, <Node: T3>]  # QureySet
   >> print get_queryset_descendants(some_nodes)
   [<Node: T1.1>, <Node: T1.2>, <Node: T3.3>, <Node: T3.3.3>] 
   >> print get_queryset_descendants(some_nodes, include_self=True)
   [<Node: T1>, <Node: T1.1>, <Node: T1.2>, <Node: T2>, <Node: T3>, <Node: T3.3>, <Node: T3.3.3>] 