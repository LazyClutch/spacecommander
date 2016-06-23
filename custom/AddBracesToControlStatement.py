from AbstractCustomFormatter import AbstractCustomFormatter

class MacroSemicolonAppender(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        tem_line_number = -1
        for line_number, line in enumerate(lines):
            # Criteria for a macro in need of semicolon:
            # - Starts with uppercase letter, ends with )
            stripped_line = line.strip()

            if stripped_line.startswith("if") or stripped_line.startswith("for") or stripped_line.startswith("while"):
            	if stripped_line.endswith(")"):
            		line = line.rstrip() + "{"
            		tem_line_number = line_number

            if tem_line_number == line_number - 2 and tem_line_number > 0:
            	line = line.rstrip() + "}"

            lines_to_write.append(line)

        return "".join(lines_to_write)

if __name__ == "__main__":
    MacroSemicolonAppender().run()
