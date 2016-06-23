from AbstractCustomFormatter import AbstractCustomFormatter

class AddSpaceToNonnull(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []

        for line_number, line in enumerate(lines):
            # Criteria for a macro in need of semicolon:
            # - Starts with uppercase letter, ends with )
            if "*_Nonnull" in line:
                line = line.replace("*_Nonnull", "* _Nonnull")

            if "*_Nullable" in line:
                line = line.replace("*_Nullable", "* _Nullable")

            lines_to_write.append(line)

        return "".join(lines_to_write)

if __name__ == "__main__":
    AddSpaceToNonnull().run()
