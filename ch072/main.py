def main():
    file_name = ".\ch072\hello.txt"
    with open(file_name,'w') as f:
        print("fred;dev;45",file=f)
        print("robert;boulanger;62",file=f)
        print("kevin;commercial;30",file=f)

    with open(file_name) as f:
        clean_lines = [line.strip() for line in f.readlines()]
        print(clean_lines)
        for line in clean_lines:
            data = line.split(';')
            print(data)              


if __name__ == "__main__":
    main()