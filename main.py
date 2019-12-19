def main():
    char_freq_map = {}
    with open("input.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c in char_freq_map:
                char_freq_map[c] = char_freq_map[c] + 1
                continue
            char_freq_map[c] = 1
    # for k,v in char_freq_map.items():
    #     print("{} : {}".format(k, v))
    

if __name__ == "__main__":
    main()
