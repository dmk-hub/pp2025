import subprocess, os, sys

def execute_command(cmd_line):
    # Handle Pipe (|)
    if '|' in cmd_line:
        cmds = [c.strip() for c in cmd_line.split('|')]
        prev_proc = None
        for i, c in enumerate(cmds):
            # Set stdin/stdout for each stage of the pipe
            stdin = prev_proc.stdout if prev_proc else None
            stdout = subprocess.PIPE if i < len(cmds) - 1 else None
            
            prev_proc = subprocess.Popen(c.split(), stdin=stdin, stdout=stdout, text=True)
            if stdin: stdin.close()
            
        if prev_proc: prev_proc.wait()
        return

    # Handle Redirection
    parts = cmd_line.split()
    input_file = output_file = None
    append = False
    clean_cmd = []

    i = 0
    while i < len(parts):
        if parts[i] == '<':
            input_file = parts[i+1]; i += 1
        elif parts[i] == '>':
            output_file = parts[i+1]; append = False; i += 1
        elif parts[i] == '>>':
            output_file = parts[i+1]; append = True; i += 1
        else:
            clean_cmd.append(parts[i])
        i += 1

    # Execute single command
    try:
        fin = open(input_file, 'r') if input_file else None
        fout = open(output_file, 'a' if append else 'w') if output_file else None
        
        subprocess.run(clean_cmd, stdin=fin, stdout=fout)
        
        if fin: fin.close()
        if fout: fout.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Custom Shell (Simplified)")
    while True:
        try:
            line = input("shell> ").strip()
            if not line or line.lower() in ['exit', 'quit']: break
            execute_command(line)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!"); break

if __name__ == "__main__":
    main()
