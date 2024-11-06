class Car:
    def __init__(self, make, model, year, mileage, price, how_mane):
        self.make = make
        self.model = model
        self.year =  year
        self.mileage = mileage
        self.price = price
        
        self.how_mane = how_mane

    def get_info(self):

        return f"Car is: marke: {self.make}, model: {self.model}, year: {self.year}, mil: {self.mileage}, price: {self.price} $"

    def apply_discount(self, foiz = 5):
        a = 5
        if foiz > 20:
            return f"Agar bizning 'Avtosug'urta'mizga avtamabilizni sug'urta qilsangiz siz o'ylatgan foizga yaqin chegirma qilib bera olamiz :)"
        elif foiz > 5:
            return f"Bizni tanlaganiz uchun sizga o'z minnatdorchiligimizni bildiramiz :)\n sizga bonus sifatida {foiz}% chegirma qilib beramiz \n>>> {self.price - (self.price * (foiz / 100))}$"
        elif foiz <= 5:
            return f"Bizni tanlaganiz uchun sizga o'z minnatdorchiligimizni bildiramiz :)\n sizga bonus sifatida {a}% chegirma qilib beramiz \n>>> {self.price - (self.price * (a / 100))}$"
    
    def mark_as_sold(self):
        if self.how_mane > 0:
            return f"Bizda bu mashinadan sotuvda bor! \nbemalol o'z imkoniyatizga qaragan holda xohlagan mashinani xarid qilishingiz mumkin"
        return f"siz hard qilmoqchi bo'lgan mashina tez orada avtosalonimizga yetib keladi! \nChunki siz uchun mashinani chet eldan olib keltiramiz"

car1 = Car("BMW", "M5", 2024,0,50000,1)
print(car1.get_info())
print(car1.apply_discount(int(input(f"iltimos nech foiz chegirma qilib berishimizni xohlaysiz!\niltimos faqat raqamlarda yozing >>> "))))
print(car1.mark_as_sold())