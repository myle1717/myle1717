a=1
b=0
while a!=0:
    a=int(input(" Nhập số kwh đã sử dụng: "))
    def tinhtiendien(a):
        if a <= 10:
            b = a * 1000
        elif 10< a <=100:
            b=10*1000+ (a-10)*1500
        else:
            b=10*1000+90*1500+(a-100)*2000
        return(b)
    print(tinhtiendien(a), "đồng")
    print(tinhtiendien(20))





