# -*- coding: utf-8 -*-
import copy
import sys

card_list = [[0+i for i in range(4)],[1+i for i in range(13)]]
name_list = [[0 for i in range(5)],[0 for i in range(5)]]
your_hand = [[0 for i in range(5)],[0 for i in range(5)]]

print('＊0：スペード,1：クラブ,2：ダイヤ,3：ハート＊')
print('入力例：***0 01 3 06 3 10 3 01 1 01***')

draw=[1,1,1,10,1,11,1,12,1,13]
#list(map(int, input('>>>').split()))
for i in range(5):
      your_hand[0][i] = draw[i*2]
      your_hand[1][i] = draw[1+i*2]
#print(your_hand)

w = 0
s = ''

for i in range(4):
      if your_hand[1][0] > your_hand[1][i+1]:
            w =your_hand[1][0]
            your_hand[1][0] =  your_hand[1][i+1]
            your_hand[1][i+1] = w
            s =your_hand[0][0]
            your_hand[0][0] =  your_hand[0][i+1]
            your_hand[0][i+1] = s
            
for i in range(3):
             if your_hand[1][1] > your_hand[1][i+2]:
                  w =your_hand[1][1]
                  your_hand[1][1] =  your_hand[1][i+2]
                  your_hand[1][i+2] = w

                  s =your_hand[0][1]
                  your_hand[0][1] =  your_hand[0][i+2]
                  your_hand[0][i+2] = s

for i in range(2):
             if your_hand[1][2] > your_hand[1][i+3]:
                  w =your_hand[1][2]
                  your_hand[1][2] =  your_hand[1][i+3]
                  your_hand[1][i+3] = w

                  s =your_hand[0][2]
                  your_hand[0][2] =  your_hand[0][i+3]
                  your_hand[0][i+3] = s

for i in range(1):
             if your_hand[1][3] > your_hand[1][i+4]:
                  w =your_hand[1][3]
                  your_hand[1][3] =  your_hand[1][i+4]
                  your_hand[1][i+4] = w

                  s =your_hand[0][3]
                  your_hand[0][3] =  your_hand[0][i+4]
                  your_hand[0][i+4] = s




name_list  =  copy.deepcopy(your_hand)
for i in range(5):
      if your_hand[0][i] == 0:
            name_list[0][i]  = 'S'
      elif your_hand[0][i] == 1:
            name_list[0][i]  = 'C'
      elif your_hand[0][i] == 2:
            name_list[0][i]  = 'D'
      elif your_hand[0][i] == 3:
            name_list[0][i]  = 'H'
for i in range(5):
      if your_hand[1][i] == 1:
            name_list[1][i]  = 'A'
      elif your_hand[1][i] == 11:
             name_list[1][i]  = 'J'
      elif your_hand[1][i] == 12:
            name_list[1][i]  = 'Q'
      elif your_hand[1][i] == 13:
            name_list[1][i]  = 'K'

for i in range(5):
      print(str(name_list[0][i])+str(name_list[1][i]),end=" ")
print()

"ロイヤルストレートフラッシュの判定"
count = 0
for i in range(4):
      if  your_hand[0][0] == your_hand[0][i+1]:
            count+=1
if count == 4:
      for i in range(5):
            if your_hand[1][i] == 1 or your_hand[1][i] == 10 or your_hand[1][i] == 11 or your_hand[1][i] == 12 or your_hand[1][i] == 13:
                  count+=1
if count == 9:
      print("ロイヤルストレートフラッシュ")
      sys.exit()

"ストレートフラッシュの判定"
count=0
count1=0
count2=0
for i in range(4):
      if  your_hand[0][0] == your_hand[0][i+1]:
            count2+=1

for i in range(4):
      count1+=1
      if your_hand[1][i]+1 == your_hand[1][i+1]:
            count+=1
      else:
            break
for i in range(count1):
      if your_hand[1][i]+9 == your_hand[1][i+1]:
            count+=1
            n=4-count1
            for i in range(n):
                  if your_hand[1][i+count1]+1 == your_hand[1][(i+count1)+1]:
                        count+=1
if count==4 and count2==4:
      print("ストレートフラッシュ")
      sys.exit()          

"フォーカードの判定"
for j in range(2):
      count=0
      for i in range(3):
            if your_hand[1][i+j] == your_hand[1][i+j+1]:
                  count+=1
      if count == 3:
            print("フォーカード")
            sys.exit()

"フルハウス判定"
count = 0
for i in range(4):
      if your_hand[1][i] == your_hand[1][i+1]:
            count+=1
for i in range(3):
      if your_hand[1][i] == your_hand[1][i+1]:
            count+=1
if count ==5:
      print("フルハウス")
      sys.exit()

"フラッシュ判定"
count=0
w =your_hand[0][0]
for i in range(4):
      if w == your_hand[0][i+1]:
            count+=1
            if count == 4:
                  print("フラッシュ")
                  sys.exit()

"ストレート判定"   
count=0
count1=0
for i in range(4):
      count1+=1
      if your_hand[1][i]+1 == your_hand[1][i+1]:
            count+=1
      else:
            break
for i in range(count1):
      if your_hand[1][i]+9 == your_hand[1][i+1]:
            count+=1
            n=4-count1
            for i in range(n):
                  if your_hand[1][i+count1]+1 == your_hand[1][(i+count1)+1]:
                        count+=1
if count==4:
      print("ストレート")
      sys.exit()          

"スリーカード"
for i in range(3):
      if your_hand[1][i] == your_hand[1][i+1] and your_hand[1][i+1] == your_hand[1][i+2]:
            print("スリーカード")
            sys.exit()
        
"ワンペア&ツーペア"
count=0
for i in range(4):
            if  your_hand[1][i] == your_hand[1][i+1]:
                  count+=1
if count == 1:
      print("ワンペア")
      sys.exit()
if count ==2:
      print("ツーペア")
      sys.exit()

print("ハイカード(ブタ)")
