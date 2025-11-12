chuoi = input("Nhap chuoi dau ngoac")
def kiem_tra_ngoac(chuoi):
    stack=[]
    cap_ngoac={")":"(","}":"{","]":"["}
    for ch in  chuoi:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}': 
            if not stack or stack[-1]!= cap_ngoac[ch]:
                return False
            stack.pop()
    return not stack
if kiem_tra_ngoac(chuoi):
    print(f"{chuoi} có tất cả ngoặc đã mở và đóng")
else:
    print(f"{chuoi} thieu ngoac")