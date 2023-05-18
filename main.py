import sys
import main_converter
import codecs # シフトジス対応のため必要です

def main(path):
    try:
        ust = codecs.open(path, "r", encoding="shift_jis") # USTファイルを開く
        ustlines = ust.readlines() #各行を取得する
        ust.close() # また書く前に閉じる必要があります
        conv_ust = []
        for line in ustlines:
            for key in main_converter.rom_dict.keys(): # ディクトのキーを取得し、ひらがなをARPAbetの音素材に変換する。
                line = line.replace("Lyric=" + key, "Lyric=" + main_converter.rom_dict[key])
            conv_ust.append(line)
        f = codecs.open(path, "w", encoding="shift_jis")
        f.writelines(conv_ust)
        f.close() # USTを保存し、プログラムを終了する
    except Exception as e:
        print(e)
        test = input(" ")
    

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("arg")
    else: 
        main(sys.argv[1])
