def main():
    with open('data_files/male_first.txt', 'r', encoding='utf-8') as infile:
        with open('data_files/male_first.txt', 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.strip()
                if len(line) > 1 and ':' not in line:
                    outfile.write(line+'\n')


if __name__ == '__main__':
    main()