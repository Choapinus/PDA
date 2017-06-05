class NPDA:
    def __init__(self):
        self.__table = {}
        self.__initial_states = set()
        self.__final_states = set()
        self.__stack = []
        self.__initial_stack_symbol = ""
 
    def add_transition(self, state, symbol, stack_symbol, new_states, stack_action):
        try:
            self.__table[state]
        except KeyError:
            self.__table[state] = {}
            
        try:
            self.__table[state][symbol]
        except KeyError:
            self.__table[state][symbol] = {}
            
        if type(new_states) == str:
            self.__table[state][symbol][stack_symbol] = [(new_states, stack_action)]
        else:
            self.__table[state][symbol][stack_symbol] = zip(new_states, stack_action)
 
    def add_initial_states(self, states):
        if type(states) == str:
            self.__initial_states.update([states])
        else:
            self.__initial_states.update(states)
 
    def add_final_states(self, states):
        if type(states) == str:
            self.__final_states.update([states])
        else:
            self.__final_states.update(states)
 
    def set_initial_stack_symbol(self, symbol):
        self.__initial_stack_symbol = symbol
 
    def __get_new_states_e(self, states):
        visited_states_b = set()
        visited_states_a = states.copy()
        current_states = visited_states_a.difference(visited_states_b)
        while current_states:
            visited_states_b.update(visited_states_a)
            for state in current_states:
                try:
                    self.__table[state][""]
                except KeyError:
                    pass
                else:
                    try:
                        top = self.__stack.pop()
                        for nstate, stack_action in self.__table[state][""][top]:
                            visited_states_a.update([nstate])
                            self.__stack.extend(stack_action[::-1])
                    except IndexError:
                        return set()
                    except KeyError:
                        self.__stack.append(top)
            current_states = visited_states_a.difference(visited_states_b)
        states.update(visited_states_a)
 
    def __get_new_states(self, symbol, states):
        new_states = set()
        for state in states:
            try:
                self.__table[state][symbol]
            except KeyError:
                pass
            else:
                try:
                    top = self.__stack.pop()
                    for nstate, stack_action in self.__table[state][symbol][top]:
                        new_states.update([nstate])
                        self.__stack.extend(stack_action[::-1])
                except IndexError:
                    return set()
                except KeyError:
                    self.__stack.append(top)
        return new_states
 
    def evaluate(self, string):
        states = self.__initial_states.copy()
        self.__stack = [self.__initial_stack_symbol]
 
        self.__get_new_states_e(states)
        print self.__stack
        for i in string:
            new_states = self.__get_new_states(i, states)
            self.__get_new_states_e(new_states)
            states = new_states
            if not states:
                break
            print self.__stack
            
        return bool(states.intersection(self.__final_states))
 
    def print_npda(self):
        print "Table"
        for state in self.__table:
            for symbol in self.__table[state]:
                for stack_symbol in self.__table[state][symbol]:
                    print "(%s, '%s', '%s') -> %s" % (state, symbol, stack_symbol, self.__table[state][symbol][stack_symbol])
        print "\nInitial States:"
        print self.__initial_states
        print "\nFinal States:"
        print self.__final_states
        print "\nInitial Stack Symbol"
        print self.__initial_stack_symbol
        print ""