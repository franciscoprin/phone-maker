from helper import form_num_str_to_num_dict_mapper
class SymbolFactory:
    def get_string(self, single_simbol):
      return form_num_str_to_num_dict_mapper[single_simbol]


        #"""
          #Returns the corresponding symbol's string shape using only |, _, -, /, \,
          #Look at the example output in README.md.

          #clue 1: use a dictionary to match the hardcode string with the corresponding symbol.
        #"""
        #pass