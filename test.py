import xlwt
from datetime import datetime

def human_read_format(size):
    def func(n):
        sub1 = n // ST
        sub2 = (n - sub1 * ST) / ST
        cond = (sub1 > 0)
        return (sub1 + round(sub2), cond)

    ST = 1024
    sp = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ"]

    current = func(size)
    count = 1
    cur_num = size
    while current[1] and count < len(sp):
        cur_num = current[0]
        count += 1
        current = func(cur_num)
    return str(cur_num) + sp[count - 1]

acdvas
asdvijoif;oweifj
sf
sjaskdbvouehslkfnhxlozhcviowencfldxsuiohfenasl
fesdfjkvfhkedvolvgwe[vasd
                     svebnaljcvlacs
                     acasnhclas
                     casc
                     scasa]asc

