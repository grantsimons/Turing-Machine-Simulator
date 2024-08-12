def read_tm_file(file_path):
    tm = {}
    with open(file_path, 'r') as f:
        # Read states
        states = f.readline().strip().split(',')
        tm['states'] = states

        # Read input alphabet
        input_alphabet = f.readline().strip().split(',')
        tm['input_alphabet'] = input_alphabet

        # Read tape alphabet
        tape_alphabet = f.readline().strip().split(',')
        tm['tape_alphabet'] = tape_alphabet

        # Read starting state
        tm['start_state'] = f.readline().strip()

        # Read transition rules
        tm['transitions'] = {}
        for line in f:
            a, b, c, d, e = line.strip().split(',')
            tm['transitions'][(a, b)] = (c, d, e)
    return tm


def simulate_turing_machine(tm, input_string):
    tape = ['_'] * 30
    current_state = tm['start_state']
    head_position = 0

    # Preload input to tape (probably the problem)
    for symbol in input_string:
        tape[head_position] = symbol
        print("processing symbol: ", tape[head_position])
        head_position += 1

    # Reset head position
    head_position = 0

    # Process
    while True:
        symbol = tape[head_position]
        if (current_state, symbol) not in tm['transitions']:
            return 'reject'
        write_symbol, new_state, move_direction = tm['transitions'][(current_state, symbol)]
        tape[head_position] = write_symbol
        current_state = new_state
        if move_direction == 'R':
            head_position += 1
        elif move_direction == 'L':
            head_position -= 1
        print(''.join(tape))
        print((head_position-1) * " " + "^ ", head_position)
        print("Current state:", current_state)
        if head_position < 0:
                tape.insert(0, '_')
                head_position = 0
        if current_state in ['accept', 'reject']:
            return current_state


def main():
    tm_file_path = 'tm.txt'
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    tm = read_tm_file(tm_file_path)

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            input_string = line.strip()
            result = simulate_turing_machine(tm, input_string)
            output_file.write(result + '\n')


if __name__ == '__main__':
    main()
