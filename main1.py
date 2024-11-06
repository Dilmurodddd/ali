class Book:
    def __init__(self):
        pass
    
    def malumot():
        a = open("royxat.csv", "r")
        
        return a.read()
    
    malumot()
    

    def almashtir(almashmoq):
        if "xa" in almashmoq or "ha" in almashmoq:
            print(f"Hurmatli mijoz bizni tanlaganiz uchun minnatdorchiligimizni qabul qiling\nva birinchi qaytarib kelgan kitobiz uchun 50% chegirma qilib beramiz")
        elif "yo'q" in almashmoq or "yoq" in almashmoq:
            print(f"Ho'p, agar qarorizni o'zgarib qolsa biz bilan bog'lanishingiz mumkin!")
        else:
            print(f"iltimoz hurmatli mijoz xa yoki yo'q javobini bering")

            almashtirish = input("Hurmatli mijoz bizda siz uchun yana bir taklif bor\nAgar xohlasangiz bizda kitoblarni almashtirish hizmati mavjud\nBunda bizdan harid qilgan kitobni o'qib bo'lganingizdan keyin bizga qaytarib kelsangiz\nbiz kitobning holatiga qarab kitobizni olib qolamiz va sizga keyingi kitob uchun\n 70 foizgacha chegirma qillib berishimiz mumkin!\ntaklifimizga rozimisiz? 'xa' yoki 'yo'q'\n>>> ")

            book.almashtir(almashtirish)

             

    def mijoz(s):
        
        a = open("royxat.csv", "r").read().split("\n")

        mavjud_kitoblar = []
        for n in a:
            if s in n.lower():
                
                mavjud_kitoblar.append(n) 

        if len(mavjud_kitoblar) == 0:
            print(f"ming bora uzur so'raymiz! mijozlarimiz ko'pligi uchun siz xohlagan kitobingiz qolmagan,\nxohlasangiz ertaga ertaroq kelishga harakat qilsangiz kitobni olishga ulgirasiz :)!")
            
        else:

            print(f"kitob haqida qizqacha ma'lumot\n{mavjud_kitoblar}")
            

            almashtirish = input("Hurmatli mijoz bizda siz uchun yana bir taklif bor\nAgar xohlasangiz bizda kitoblarni almashtirish hizmati mavjud\nBunda bizdan harid qilgan kitobni o'qib bo'lganingizdan keyin bizga qaytarib kelsangiz\nbiz kitobning holatiga qarab kitobizni olib qolamiz va sizga keyingi kitob uchun\n 70 foizgacha chegirma qillib berishimiz mumkin!\ntaklifimizga rozimisiz? 'xa' yoki 'yo'q'\n>>> ")

            book.almashtir(almashtirish)

        

    

book = Book




sorash = input("Assalomu alaykum hurmatli mijoz! yuqori qismda bizning kitoblarimizning ro'yxati mavjud\nsizga qaysi kitob berak?\n'iltimos faqat kitobning nomini yozing\n>>> ").lower()


print(book.mijoz(sorash))





































    

#     def checkout(self,sotish):
#         if sotish > self.availability:
#             return f"""Ming bora uzur so'raymiz! hozirda bu kitoblarni juda ko'p mijozlarimiz sotib olmoqda,\nshuning uchun hozircha siz xohlagan kitoblaringiz qolmadi! \nertaga ertaroq kelsangiz xohlagan kitoblaringizni chegirma asosida olishingiz mumkin,\nchegirmalarimiz: 20tadan ko'p kitob olsangiz 10% chegirma, :)\n"""
#         else:
#             if sotish >= 20:
#                 return f"Tabiriklaymiz! Siz bizning bonuslarimizdan biriga ega bo'ldiz\nyangi narx blan tanishing >>> {sotish * self.price - (sotish * self.price * (10/100))}$\n"
#             else:
#                 return f"Siz bizni tanlaganiz va harid qilganiz uchun sizdan juda ham minnatdormiz!\nsiz sotib olmoqchi bo'lgan kitobning narxi {sotish * self.price}$\n"


#     def return_book(self, qaytarmoq):
#         q = qaytarmoq.lower().split()
#         if "xa" in q or "ha" in q:
#             return f"Kitobni qaytarayotgan paytiz biz kitobning holatini tekshirib olamiz \nva sizga 70% foizgacha chegirma qilib berishimiz mumkin!\n"
#         elif "yo'q" in q or "yoq" in q:
#             return f"Ho'p! Agar fikringiz o'zgarib qolsa bemalol bizga murojat qilishingiz  mumkin!"
        


#     def calculate_late_fees(self):
#         pass

# book = Book("Python","Dilmurod",123456789,50,15)

# if book.royxat() == 1:
#     print("Iltimos ro'yxatni to'ldiring!")

# # sotib_olish = int(input("Assalomu alaykum bizning kutubxonamizga tashrif buyurganingiz uchun juda minnatdormiz!\nechta kitop sotib olmoqchisiz?\n>>> "))
# # qaytarish = (input("""Bizda siz uchun yana bir yangiligimiz bor!\nBizning kutubxonamizda, sotib olgan kitobizni boshqasiga almashtirib ketishinzi ham mumkin!\nkitobni o'qib bo'lganizdan keyin almashtirasizmi?\n"""))

