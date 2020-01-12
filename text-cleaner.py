import codecs

if __name__ == '__main__':
    f_in = codecs.open("new-training-data-in.txt", "r", "utf-8")
    f_out = codecs.open("new-training-data-out.txt", "w", "utf-8")
    for x in f_in:
        y = x.replace('ö', 'o').replace('å', 'a').replace('è', 'e').replace('é', 'e').replace('ë', 'e').replace('ï', 'i').replace('á', 'a').replace('ü', 'u').replace('â', 'a')
        f_out.write(y)

    f_in.close()
    f_out.close()
