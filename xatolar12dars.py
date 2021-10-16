# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:22:34 2021

@author: 131565
"""
#on = float(input("Juft son kiriting: "))
#if not son%2==0:
 #   print("Bu son juft emas.")
#else:
 #   print("Rahmat!")
 
 
#yosh = int(input("Yoshingiz nechida? "))
#if yosh<=4 or yosh>=60:
 #   print("narh = 0")
    
#elif yosh < 18:
#    print("narh = 10000")
    
#else:
#    print("Chipta 20000 so'm")



#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")
    

# =============================================================================
# mahsulotlar = ['un', 'yog', "sovun", 'tuxum', 'piyoz',
#              'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# savat = []
# for n in range(5):
#     x = input(f"Savatga {n+1}-mahsulotni qo'shing: ")
#     if x != '': 
#         savat.append(x)
# 
# # print(savat)
# if not savat: print("Savatingiz bo'sh") 
# else:
#     for s in savat:
#         if s not in mahsulotlar: print(f'Not found {s}')
#         else: print(f'Found {s}')
#      
# =============================================================================
# =============================================================================
# mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# 
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# 
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# 
#   
# for mahsulot in mavjud_emas:
# print(f"Do'konimizda quyidagi mahsulotlar yo'q:{mavjud_emas} ") 
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# =============================================================================
      
                 

users = ['alisher1983','aziza','yasina', 'umar']

login = str(input("Yangi login tanlang: " )).lower()

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print(f"Xush kelibsiz, {login.title()}!")

