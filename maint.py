class Book:
    def __init__(self):
        pass
    
    def malumot(self):
        with open("royxat.csv", "r") as a:
            return a.read()
    
    def almashtir(self, almashmoq):
        if "xa" in almashmoq or "ha" in almashmoq:
            return "Hurmatli mijoz, bizni tanlaganingiz uchun minnatdorchiligimizni qabul qiling\nva birinchi qaytarib kelgan kitobingiz uchun 50% chegirma qilib beramiz"
        elif "yo'q" in almashmoq or "yoq" in almashmoq:
            return "Ho'p, agar qaroringiz o'zgarib qolsa biz bilan bog'lanishingiz mumkin!"
        else:
            print("Iltimos, hurmatli mijoz, 'xa' yoki 'yo'q' javobini bering.")
            almashtirish = input("Hurmatli mijoz, bizda siz uchun yana bir taklif bor.\nAgar xohlasangiz, bizda kitoblarni almashtirish xizmati mavjud.\nBunda bizdan harid qilgan kitobni o'qib bo'lganingizdan keyin bizga qaytarib kelsangiz,\nbiz kitobning holatiga qarab uni olib qolamiz va keyingi kitob uchun 70% chegirma qilamiz.\nTaklifimizga rozimisiz? 'xa' yoki 'yo'q'\n>>> ")
            return self.almashtir(almashtirish)

    def mijoz(self, s):
        kitob_nomi = []
        with open("royxat.csv", "r") as a:
            content = a.read().split("\n")
        
        for line in content:
            b = line.split(",")
            if len(b) > 1:  # Bajarilishini tekshirish uchun
                kitob_nomi.append(b[1])

        mavjud_kitoblar = [line for line in content if s in line.lower()]
        
        if len(mavjud_kitoblar) == 0:
            return "Ming bora uzur so'raymiz! Mijozlarimiz ko'pligi uchun siz xohlagan kitob qolmagan.\nXohlasangiz, ertaga ertaroq kelishga harakat qilsangiz, kitobni olishga ulgurasiz! :)"
        else:
            print(f"Kitob haqida qisqacha ma'lumot:\n{mavjud_kitoblar}")
            almashtirish = input("Hurmatli mijoz, bizda siz uchun yana bir taklif bor.\nAgar xohlasangiz, bizda kitoblarni almashtirish xizmati mavjud.\nBunda bizdan harid qilgan kitobni o'qib bo'lganingizdan keyin bizga qaytarib kelsangiz,\nbiz kitobning holatiga qarab uni olib qolamiz va keyingi kitob uchun 70% chegirma qilamiz.\nTaklifimizga rozimisiz? 'xa' yoki 'yo'q'\n>>> ")
            return self.almashtir(almashtirish)

    def sotish(self):
        pass

# Obyekt yaratish
book = Book()

# Kitoblar ro'yxatini chiqarish
print(book.malumot())

# Foydalanuvchidan kitobni tanlashni so'rash
sorash = input("Assalomu alaykum hurmatli mijoz! Yuqorida bizning kitoblarimiz ro'yxati mavjud.\nSizga qaysi kitob kerak?\nIltimos, faqat kitobning nomini yozing:\n>>> ").lower()

# Mijoz so'ragan kitob haqida ma'lumotni ko'rsatish
print(book.mijoz(sorash))
