import sys
import main_converter
import codecs

def main(path):
    try:
        ust = codecs.open(path, "r", encoding="shift_jis")
        ustlines = ust.readlines()
        ust.close()
        conv_ust = []
        for line in ustlines:
            for key in main_converter.rom_dict.keys():
                line = line.replace("Lyric=" + key, "Lyric=" + main_converter.rom_dict[key])
            conv_ust.append(line)
        f = codecs.open(path, "w", encoding="shift_jis")
        f.writelines(conv_ust)
        f.close()
    except Exception as e:
        print(e)
        test = input(" ")
    

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("arg")
    else: 
        main(sys.argv[1])
