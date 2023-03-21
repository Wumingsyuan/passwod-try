#密碼重設程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入三次
#如果正確 就印出'登入成功'
#如果不正確 就印出 '密碼錯誤! 還有_次機會!'

password = 'a123456'
i = 3 #剩餘機會
while True :
    pwd = input('請輸入密碼') #不能用password，因為重複使用
    if pwd == password : #不要寫'a123456' 不好!
        print('登入成功')
        break  #逃出迴圈
    else :
        i = i - 1
        print('登入失敗,還有', i, '次機會')
        if i ==0 :
            break
        