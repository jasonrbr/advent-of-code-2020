class Interpreter:
    def __init__(self):
        self.max_line = 0
        self.line = 0
        self.linesHit = set()
        self.acc = 0

    def add(self, num):
        executed = self.execute()

        if not executed:
            return False

        self.acc += num
        self.max_line = self.line if self.line > self.max_line else self.max_line
        self.line += 1

        return executed

    def jmp(self, offset):
        executed = self.execute()

        if not executed:
            return False

        self.max_line = self.line if self.line > self.max_line else self.max_line
        self.line += offset
        return executed

    def execute(self):
        if self.line in self.linesHit:
            return False
        self.linesHit.add(self.line)
        return True

    def noop(self, __):
        executed = self.execute()

        if not executed:
            return False

        self.max_line = self.line if self.line > self.max_line else self.max_line
        self.line += 1
        return executed


def getInterpreter():
    interpreter = Interpreter()
    opMap = {
        'acc': interpreter.add,
        'jmp': interpreter.jmp,
        'nop': interpreter.noop
    }
    return interpreter, opMap


def attemptRun(interpreter, opMap, instructions):
    execute = True
    while (execute and interpreter.line < len(instructions)):
        op, val_str = instructions[interpreter.line].strip().split()
        execute = opMap[op](int(val_str))

    return execute, interpreter.acc


def updatedInstructions(instructions, start_line):
    idx = next(i for i, line in enumerate(
        instructions[start_line:], start_line) if 'jmp' in line)
    copy_instructions = instructions[:]
    copy_instructions[idx] = copy_instructions[idx].replace('jmp', 'nop')
    return copy_instructions, idx


with open('input8.txt') as f:
    instructions = f.readlines()
    acc = 0
    successful_run = False
    line_changed = -1
    while(not successful_run):
        updated_instructions, line_changed = updatedInstructions(
            instructions, line_changed + 1)
        successful_run, acc = attemptRun(
            *getInterpreter(), updated_instructions)

    print(line_changed, acc)
