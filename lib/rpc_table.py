"""
Define RPC functions needed to generate
"""

# [ <ret-type>, [<arg_types>] ]
func_table = [
    [ "int", [] ],
    [ "int", ["int"] ],
    [ "int", ["int", "int"] ],
    [ "int", ["int", "string"] ],
    [ "int", ["int", "string", "int"] ],
    [ "int", ["int", "string", "string"] ],
    [ "int", ["int", "string", "int", "int"] ],    
    [ "int", ["int", "int", "string", "string"] ],
    [ "int", ["string"] ],
    [ "int", ["string", "int"] ],
    [ "int", ["string", "int", "int"] ],
    [ "int", ["string", "int", "string"] ],
    [ "int", ["string", "int", "string", "string"] ],
    [ "int", ["string", "int", "int", "string", "string"] ],
    [ "int", ["string", "string"] ],
    [ "int", ["string", "string", "int"] ],
    [ "int", ["string", "string", "int64"] ],
    [ "int", ["string", "string", "string"] ],
    [ "int", ["string", "string", "int", "int"] ],
    [ "int", ["string", "string", "string", "int"] ],
    [ "int", ["string", "string", "string", "int", "string"] ],
    [ "int", ["string", "string", "string", "string"] ],
    [ "int", ["string", "string", "string", "string", "string"] ],
    [ "int", ["string", "int", "string", "int", "int"] ],
    [ "int", ["string", "string", "string", "string", "string", "string"] ],
    [ "int", ["string", "string", "string", "int", "string", "string"] ],
    [ "int", ["string", "string", "string", "string", "string", "string", "string"] ],
    [ "int", ["string", "int64"]],
    [ "int", ["int", "int64"]],
    [ "int", ["int", "string", "int64"]],
    [ "int64", [] ],
    [ "int64", ["string"] ],
    [ "int64", ["int"]],
    [ "int64", ["int", "string"]],
    [ "int64", ["string", "string"]],
    [ "int64", ["string", "int", "string"] ],
    [ "string", [] ],
    [ "string", ["int"] ],
    [ "string", ["int", "int"] ],
    [ "string", ["int", "string"] ],
    [ "string", ["int", "int", "string"] ],
    [ "string", ["string"] ],
    [ "string", ["string", "int"] ],
    [ "string", ["string", "int", "int"] ],
    [ "string", ["string", "string"] ],
    [ "string", ["string", "string", "int"] ],
    [ "string", ["string", "string", "int", "int"] ],
    [ "string", ["string", "string", "string"] ],
    [ "string", ["string", "string", "string", "int"] ],
    [ "string", ["string", "string", "string", "string"] ],
    [ "string", ["string", "string", "string", "string", "int"] ],
    [ "string", ["string", "string", "string", "string", "string"] ],
    [ "string", ["string", "string", "string", "string", "string", "int"] ],
    [ "string", ["string", "string", "string", "int", "string", "string"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "int"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "int", "int"] ],
    [ "string", ["string", "string", "string", "string", "string", "string"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "int64"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "int64", "int"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "string"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "string", "int"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "string", "int64"] ],
    [ "string", ["string", "string", "string", "string", "string", "string", "string", "string", "string"] ],
    [ "string", ["string", "int", "string", "string", "string", "string", "string", "string", "string", "string", "string", "string", "int", "string"] ],
    [ "string", ["string", "int", "string", "int", "int"] ],
    [ "string", ["string", "int", "string", "string", "string"] ],
    [ "objlist", [] ],
    [ "objlist", ["int"] ],
    [ "objlist", ["int", "int"] ],
    [ "objlist", ["int", "string"] ],
    [ "objlist", ["int", "int", "int"] ],
    [ "objlist", ["string"] ],        
    [ "objlist", ["string", "int"] ],
    [ "objlist", ["string", "int", "int"] ],
    [ "objlist", ["string", "int", "int", "int"] ],
    [ "objlist", ["string", "int", "string"] ],
    [ "objlist", ["string", "string"] ],        
    [ "objlist", ["string", "string", "string"] ],
    [ "objlist", ["string", "string", "int"] ],
    [ "objlist", ["string", "string", "string", "int"] ],
    [ "objlist", ["string", "string", "int", "int"] ],
    [ "objlist", ["string", "int", "int", "string"] ],
    [ "objlist", ["string", "string", "int", "int", "int"] ],
    [ "objlist", ["string", "string", "string", "int", "int", "int"] ],
    [ "objlist", ["int", "string", "string", "int", "int"] ],
    [ "objlist", ["string", "int", "string", "string", "string"] ],
    [ "objlist", ["string", "int", "string", "int", "int"] ],
    [ "objlist", ["string", "int", "string", "string", "int"] ],
    [ "objlist", ["string", "string", "string", "string", "int", "int"] ],
    [ "object", [] ],
    [ "object", ["int"] ],
    [ "object", ["string"] ],
    [ "object", ["string", "string"] ],
    [ "object", ["string", "string", "string"] ],
    [ "object", ["string", "int", "string"] ],
    [ "object", ["int", "string", "string"] ],
    [ "object", ["string", "string", "int", "int"] ],
    [ "object", ["string", "string", "string", "int"] ],
    [ "object", ["string", "string", "string", "string", "string", "string", "string", "int", "int"] ],
    [ "object", ["string", "string", "string", "string", "string", "string", "int", "string", "int", "int"] ],
    ["json", ["string"]],
]
