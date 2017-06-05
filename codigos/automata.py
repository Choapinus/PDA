import NPDA
 
npda = NPDA()
 
npda.add_initial_states("p")
 
npda.set_initial_stack_symbol("Z")
 
#L(M) = {0^n1^n | n >= 0}
npda.add_transition("p", "0", "Z", "p", "AZ")
npda.add_transition("p", "0", "A", "p", "AA")
 
npda.add_transition("p", "", "Z", "q", "Z")
npda.add_transition("p", "", "A", "q", "A")
 
npda.add_transition("q", "1", "A", "q", "")
npda.add_transition("q", "", "Z", "r", "Z")
 
npda.add_final_states("r")
 
#npda.print_npda()
 
l = ["01", "001", "0011", "", "00", "0111", "1111111"]
for i in l:
    print "'%s' %s" % (i, npda.evaluate(i))