def openBox():
    print('종이상자를 엽니다. ^^')
    openBox() # 자기 자신을 다시 호출
    

if __name__ == '__main__':
    print(openBox())