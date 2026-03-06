a=int(input())
if a<1 or a>54:
    print("Недопустимый номер места. В плацкартном вагоне — места с 1 по 54.")
else:
    if a<=36:
        sit="В купе,"
    else:
        sit="Боковое,"
    if a%2==1:
        floor="нижнее"
    else:
        floor="верхнее"
    print(sit,floor)

