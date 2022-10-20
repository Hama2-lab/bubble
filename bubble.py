import random

def bubblesort():
    a = int(input("データ数を指定:"))

    x = random.sample(range(100), k=a)
    print(x)
    b = int(input("昇順なら0、降順なら1を入力:"))

    # 昇順
    if b == 0:
      for i in range(0,a):
        for j in range(0,a):
          if x[i]>=x[j]:
            continue
          else:
            x[i],x[j]=x[j],x[i]
      print(x)

    # 降順
    elif b == 1:
      for i in range(0,a):
        for j in range(0,a):
          if x[i]<=x[j]:
            continue
          else:
            x[i],x[j]=x[j],x[i]
      print(x)

    else:
      print("エラー")

if __name__ == '__main__':
    bubblesort()
