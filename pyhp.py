import re

class pyhp:
    def __init__(self,template):
        self.template = template
        self.variables = {}

    def set(self, name, val):
        self.variables[name] = val

    def print_html(self):
        def get_print(string):
            return '\n'+'print("'+string+'")'
        code = ''

        for item in re.split('\?\>',self.template):
            if '<?py' in item: 
                rs = re.split('\<\?py ',item)
                code += get_print(rs[0])
                code += '\n'+rs[1]
            else:
                code += get_print(item)

        exec(code,self.variables)
