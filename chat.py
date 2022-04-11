def read_file(filename):
    lines=[]
    with open(filename ,mode="r",encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new=[]
    person=None
    for line in lines:
        if line == "Shen":
            person = "Shen"
            continue
        elif line == "Leo":
            person = "Leo"
            continue
        if person:
            new.append(person + ":" + line)
    return new


def write_file(filename,lines):
    with open (filename,mode="w") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    a= read_file("input.txt")
    a= convert(a)
    write_file("output.txt",a)

main()