import sys

class VsInterpreter():
    
    def __init__(self):
        self.storage = {}
        self.code = []
        self.pointer = 0

    def parseFile(self, path):
        try:
            file = open(path, "r")
            for line in file:
                line = line.rstrip()
                self.code.append([line, 0])

            self.execute()

        except FileNotFoundError:
            print("Could not run.")
            print("Error: File not found")
            sys.exit(1)
        except Exception as e:
            print("Could not run.")
            print(f"Error: {str(e)}")
            print("At: "+self.code[self.pointer][0]+"\nPointer: "+str(self.pointer))
            sys.exit(1)

    
    def throw_exception(self, exception):
        print("Could not run.")
        print(exception)
        print("At: "+self.code[self.pointer][0]+"\nPointer: "+str(self.pointer))
        sys.exit(1)


    def get_value(self, expression):
        values = []
        es = []
        actions = []
        oneString = False
        for e in str(expression).split(" "):
            if str(e) not in "+-*/%" or str(e) == "//":
                e = e.strip()
                es.append(e)
                try:
                    values.append(self.storage[e])
                    if isinstance(self.storage[e], str):
                        oneString = True
                except KeyError:
                    if isinstance(e, int):
                        values.append(e)
                    else:
                        values.append(str(e))
            else:
                actions.append(e)
        if oneString:
            str_values = []
            for l in values:
                str_values.append(str(l))
            value = ''.join(str_values)
            return value
        else:
            return eval("".join([str(elem) for pair in zip(values, actions) for elem in pair] + [str(elem) for elem in values[len(actions):]]))
    
    def get_boolean(self, expression):
        values = []
        operator = None

        for e in str(expression).split(" "):
            if str(e) in "<>=":
                operator = str(e)
            else:
                if e.startswith("{") and e.endswith("}"):
                    values.append(self.get_value(e[1:-1]))
                else:
                    try:
                        values.append(self.storage[e])
                        if isinstance(self.storage[e], str):
                            self.throw_exception("Unable to compare strings")
                            return False
                    except KeyError:
                        values.append(int(e))
        
        
        if operator == "<":
            return values[0] < values[1]
        elif operator == ">":
            return values[0] > values[1]
        elif operator == "=":
            return values[0] == values[1]
        else:
            self.throw_exception("Unknown operator")
            return False
        
    def execute(self):

        while self.pointer < len(self.code):
            task = self.code[self.pointer][0]
            if self.code[self.pointer][1] == 1:
                self.code.pop(self.pointer)

            for subtask in str(task).split(";"):
                cmd = str(subtask).strip()

                if cmd.startswith("LOG"):
                    string = cmd[4:].strip()
                    if string.startswith("{"):
                        if string.endswith("}"):
                            variable = string.replace("{", "")
                            variable = variable.replace("}", "")

                            if "+" in variable:
                                string = self.get_value(variable)
                            elif "-" in variable:
                                string = self.get_value(variable)
                            elif "*" in variable:
                                string = self.get_value(variable)
                            elif "/" in variable:
                                string = self.get_value(variable)
                            elif "//" in variable:
                                string = self.get_value(variable)
                            elif "%" in variable:
                                string = self.get_value(variable)

                            else:
                                try:
                                    string = self.storage[variable]
                                except KeyError:
                                    self.throw_exception("Variable "+variable+" not defined.")
                        else:
                            self.throw_exception("Missing } or unknown symbol at the end")
                            


                    print(string) # Output, no debug
                

                elif cmd.startswith("VAR"):
                    if "=" in cmd[4:]:
                        declaration = cmd[4:].strip()
                        name = declaration.split(" = ")[0]
                        value = declaration.split(" = ")[1]
                        if value.startswith("{"):
                            if value.endswith("}"):
                                value = self.get_value(value[1:-1])
                            else:
                                self.throw_exception("Missing } or unknown symbol at the end")
                        else:
                            if value == "BLACKHOLE":
                                value = input()

                    else:
                        modification = cmd[4:].strip()
                        
                                         
                        if "+" in modification:
                            name = modification.split(" + ")[0]
                            change = modification.split(" + ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)

                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")
                            except TypeError:
                                self.throw_exception("Can't change type from string to int.")

                            value = self.storage[name]
                            value += change
                            self.storage[name] = value


                        elif "-" in modification:
                            name = modification.split(" - ")[0]
                            change = modification.split(" - ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)
                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")
                            value = self.storage[name]
                            value -= change
                            self.storage[name] = value

                        elif "*" in modification:
                            name = modification.split(" * ")[0]
                            change = modification.split(" * ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)
                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")
                            value = self.storage[name]
                            value *= change
                            self.storage[name] = value

                        elif "/" in modification:
                            name = modification.split(" / ")[0]
                            change = modification.split(" / ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)
                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")

                            value = self.storage[name]
                            value /= change
                            self.storage[name] = value

                        elif "//" in modification:
                            name = modification.split(" // ")[0]
                            change = modification.split(" // ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)
                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")

                            value = self.storage[name]
                            value //= change
                            self.storage[name] = value

                        elif "%" in modification:
                            name = modification.split(" % ")[0]
                            change = modification.split(" % ")[1]
                            try:
                                if not isinstance(self.storage[name], str):
                                    change = int(change)
                            except ValueError:
                                self.throw_exception("Can't change type from string to int.")

                            value = self.storage[name]
                            value %= change
                            self.storage[name] = value

                        else:
                            self.throw_exception("Unknown symbol in "+cmd[4:])
                    try:
                        int_value = int(value)
                        self.storage[name] = int_value
                    except ValueError:
                        self.storage[name] = value


                elif cmd.startswith("WORMHOLE_TO"):
                    new_pointer_val = cmd[11:].strip()
                    try:
                        new_pointer_val = int(new_pointer_val)
                        self.pointer = new_pointer_val-2
                    except ValueError:
                        self.throw_exception("Unable to WORMHOLE to a specific line. Target is not a number.")
                

                elif cmd.startswith("WORMHOLE"):
                    new_pointer_val = cmd[8:].strip()
                    try:
                        new_pointer_val = int(self.get_value(new_pointer_val))
                        self.pointer += (new_pointer_val-1) 
                    except ValueError:
                        self.throw_exception("Unable to WORMHOLE by number. Argument is not a number.")
                
                elif cmd.startswith("IF"):
                    cmd = cmd.strip()
                    left_side = cmd.split(" : ")[0]
                    left_side = left_side[3:]
                    right_side = cmd.split(" : ")[1]
                    
                    true_part = right_side.split(" ~ ")[0]
                    false_part = right_side.split(" ~ ")[1]

                    if self.get_boolean(left_side):
                        self.code.insert(self.pointer+1, [true_part, 1])
                    else:
                        self.code.insert(self.pointer+1, [false_part, 1])

                elif cmd.startswith("PASS"):
                    pass
                elif cmd == "":
                    pass
                elif cmd.startswith("QUIT"):
                    print("Ended (QUIT). Exit code 0")
                    sys.exit(0)

            self.pointer += 1


def main():
    if len(sys.argv) != 2:
        print("Could not run.")
        print("Usage: python voidscript.py <filename>.vs")
        sys.exit(1)
    
    filePath = sys.argv[1]
    if not filePath.endswith(".vs"):
        print("Could not run.")
        print("Filename must end with .vs")
        sys.exit(1)

    interpreter = VsInterpreter()
    interpreter.parseFile(filePath)

    print("\n\nEnded. Exit code 0")

if __name__ == "__main__":
    main()