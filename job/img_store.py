# -*- coding: utf-8 -*-
import jieba

def job():
    s = jieba.cut("小名跑了出去", cut_all = True)
    print '/'.join(s)

def main():
    job()
if __name__ == "__main__":
    main()
