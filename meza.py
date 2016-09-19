#!/usr/bin/env python
# coding: utf-8
import codecs
import time
import commands
import random
f = codecs.open("/home/pi/voice/voice.txt","w","utf-8")

#f = codecs.lookup('utf_8')[-1](f)


#f = open('voice.txt','w')

prob_10_overn = 15

#f.write(u'こんにちは\n')
#exit

adj = [u"ガーリーな",u"どっちみち",u"フルーティーな",u"いざ",u"たんぱくな",u"スパークちゅうの",u"なれたセリフで",u"トロピカール",u"マロンふうみ"]

sub = [u"ダージリン",u"ウォッチャー",u"イケメン",u"もこみち",u"ジャスティンビーバー",u"ふかキョン",u"きっぽう",u"ガガ",u"モーニング",u"プーチン",u"サマンサタバサ",u"コペンハーゲン",u"ペッパーペッパー",u"スリッポン", "キャミワンピ",u"メルボルン",u"ダルビッシュ",u"パフィー"]

adv = [u"が",u"は",u"に",u"と"]

ver = [u"ぱっさぱさ",u"キャンキャン",u"げせん",u"プロフェッショナル",u"ルポライターきしつ",u"オーライ",u"ほりふかい",u"にがい",u"クールダウン",u"ジャケットプレイきた",u"ノリノリ",u"いいじゃん",u"シャウトシャウト",u"スキルアップ",u"コスメティック",u"クーポンクー",u"プルプル"]

len_adj = len(adj)
len_sub = len(sub)
len_adv = len(adv)
len_ver = len(ver)
random.randint(1,5)


if random.randint(1,prob_10_overn) < 10:
    adj_go = adj[random.randint(0,len_adj-1)]
else:
    adj_go =""

sentence = adj_go + sub[random.randint(0,len_sub-1)]+adv[random.randint(0,len_adv-1)]+ver[random.randint(0,len_ver-1)]

#print sentece


f.write(sentence)
print sentence

f.close()


check = commands.getoutput("open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow  /home/pi/voice/voice.wav /home/pi/voice/voice.txt")

#print check

check = commands.getoutput("aplay /home/pi/voice/voice.wav")
time.sleep(10)
check = commands.getoutput("aplay /home/pi/voice/voice.wav")
time.sleep(10)
check = commands.getoutput("aplay /home/pi/voice/voice.wav")
time.sleep(10)
check = commands.getoutput("aplay /home/pi/voice/voice.wav")



# Comitt to Github 2016/09/19


