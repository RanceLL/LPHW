del_stmt ::=  "del" target_list
global_stmt ::=  "global" identifier ("," identifier)*
#The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals.