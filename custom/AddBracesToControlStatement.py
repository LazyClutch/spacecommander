from AbstractCustomFormatter import AbstractCustomFormatter

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class AddBracesToControlStatement(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        tem_line_number = -1
        tem_line_indent = -1
        str_stack = Stack()
        indent_stack = Stack()
        for line_number, line in enumerate(lines):
            # Criteria for a macro in need of semicolon:
            # - Starts with uppercase letter, ends with )
            rstripped_line = line.rstrip()
            stripped_line = line.strip()

            if (stripped_line.startswith("if") or stripped_line.startswith("for") or stripped_line.startswith("while")) and stripped_line.endswith(")"):
            	line = line.rstrip() + " {\n"
            	tem_line_number = line_number
            	str_stack.push(line)
            	line_indent = len(rstripped_line) - len(rstripped_line.lstrip())
            	indent_stack.push(line_indent)
            else:
            	if tem_line_number == line_number - 1 and str_stack.size() > 0:
            		str_stack.pop()
            		line = line.rstrip() + "\n" + indent_stack.peek() * " " + "}\n" 
            		indent_stack.pop()
            	elif tem_line_number == line_number - 2 and str_stack.size() > 0:
            		tem_line = ""
            		while str_stack.size() > 0:
            			tem_line = indent_stack.peek() * " " + "}\n"
            			indent_stack.pop()
            			str_stack.pop()
            		line = tem_line + line
            #if tem_line_number == line_number - 1 and tem_line_number > 0:
            #	line = line.rstrip() + "\n" + tem_line_indent * " " + "}\n" 

            lines_to_write.append(line)

        return "".join(lines_to_write)

if __name__ == "__main__":
    AddBracesToControlStatement().run()
