drive = input('你有開過車嗎？')
age = int(input('請問你的年齡？'))

if drive == "有":
    if age >= 20:
        print('你通過測試')
    else:
        print('你不能開車')
elif drive == "沒有":
    if age >= 20:
        print('你可以考駕照了')
    else:
        print('再等幾年就可以考了')
else:
    print('只能輸有/沒有')
