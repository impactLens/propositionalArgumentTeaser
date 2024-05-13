from logic import *

print ("+"*23)
print ("\n STUDY TERMS TO FORM ARGUMENT: \n")
print ( "       p and q = (p & q) " )
print ( "       p or q (p | q) " )
print ( "       not p (~p) " )
print ( "       p implies q (p => q) " )
print ( "       p is not implied by q (p <= q) " )
print ( "       p if and only iff q ( p.iff(q) ) " )
#print ("+"*23)

# # DECLARING VARIABLE FOR FUNCTION
# P,Q,R = vars ("P","Q","R")

# FORMULA
# proposition = ( P | Q & ~P >> Q )
#
# proposition.print_truth_table()
#
# print ( proposition.is_tautology() )
# print ( proposition.is_contingency() )
# print ( proposition.is_contradiction() )

# # DECLARING VARIABLE FOR FUNCTION
P,Q,R,S = vars ("P","Q","R","S")

# RULES: (first: PREMISES, last: CONCLUSIONS)
# # PREMISES WITH CONCLUSIONS USING FORMULA LOGIC

# PREMISES WITH CONCLUSIONS USING FORMULA LOGIC

# RULES:    proposition = ( PREMISES, CONCLUSION )

statement = "everybody exists and safe, if and only if you are safe"
proposition1 = ( ~P | ~Q & ~P >> ~Q )


proposition = ArgumentForm ( P >> Q, P, conclusion = Q )

valid=proposition.is_valid()

print ("+"*23)
print ("\nCONCLUDING STATEMENT: \n")

print ("STATEMENT RECEIVED: ",statement)
print ("PROPOSITIONAL ARGUMENT RESPONSE: ",proposition)

print ("\n      1)TRUTH TABLE: \n[if you see stars, then it's unusual and followd by C-F and else]\n")
proposition.print_truth_table()

if valid==1:
 print ('''     2) KIND OF PROPOSITION 
                2_A) modus pones  
                2_B) modus tollen 
                2_C) disjunctive syllogism  
                2_D) hypothetocal syllogism 
                2_E) delimma 
                2_F) principle of explotion''') 
else:
 print ('''             2) KIND OF PROPOSITION
                2_A) KIND OF PROPOSITION 
                2_B) denying the antecedent 
                2_C) disfunctional syllogism''')

print ("\n      3) VALIDITY OF PROPOSITION: ", valid )

print ("\n      4) CHECK LIST: ")
print ("            4_i)   TAUTOLOGY:     ", proposition1.is_tautology() )
print ("           4_ii)   CONTRADICTION: ", proposition1.is_contingency() )
print ( "         4_iii)   CONTINGENCY:   ", proposition1.is_contradiction() )

print ("+"*23)

print ("\nNOTED REMARKS: ")
print ( " # modus pones ( PREMISES = true  CONCLUSION = true &  valid = true ) " )
    ## if its raining then i take my umbrella (p>>q), its raining (p), therefore/conclusion i take my umbrella(q) """)

print (" # modus tollen ( PREMISES = true  CONCLUSION = true &  valid = true ) " )
## if its raining then i take my umbrella (p>>q),  i do take my umbrella (q),  therefore/conclusion its raining (p)  """)

print (" # denying the antecedent ( PREMISES = true  CONCLUSION = false ) or vice versa &  valid = false ) " )
## if its raining then i take my umbrella (p>>q), its not raining (~p), therefore/conclusion i dont take my umbrella (~q)""")

print (" # disjunctive syllogism ( PREMISES = true  CONCLUSION = true &  valid = true ) " )
## i either like tea or coffee (p|q), ), i dont like tea (~p), therefore i like coffee (q)""")

print (" # disfunctional syllogism ( PREMISES = true  CONCLUSION = false &  valid = false ) " )
## i either like tea or coffee (p|q), ), i do like tea (p), therefore i dont like coffee (~q)""")

print (" # hypothetical syllogism ( PREMISES = true  CONCLUSION = true &  valid = true ) " )
## if its raining then i take my umbrella (p>>q), i dont take my umbrella then i stay dry (q>>r),       therefore/conclusion if its raining then i will stay dry (p>>r)""")

print (" # delimma ( PREMISES = true  CONCLUSION = true  & valid = true ) " )
## i either like tea or coffee (p|q), if i like tea then i will buy tea bags (p>>r), if i like coffee then i buy coffee beans (q>>s), conclusion is: i either buy tea bags or beans (r|s)""")

print (" # principle of explosion ( PREMISES = CONCLUSION  & valid = true ) " )
## premises is false, conclusion is: does believe the PREMISES, does believe the conclusion
### every unicorn has a horn , as there is no unicorn, u wont able to find any unicorn has a horn, so its true all unicorn (p) have horn""")

print ("+"*23)
