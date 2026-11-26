class Murabiy:
    def __init__(self, ism, sport):
        self.ism = ism
        self.sport = sport

    def malumot(self):
        return f"{self.ism} — {self.sport}"


class Sportchi:
    def __init__(self, ism, yosh, murabiy):
        self.ism = ism
        self.yosh = yosh
        self.murabiy = murabiy

    def malumot(self):
        return f"{self.ism} ({self.yosh} yosh) — murabiy: {self.murabiy.ism} ({self.murabiy.sport})"

    def saqlash(self):
        with open("sportchilar.txt", "a", encoding="utf-8") as f:
            f.write(self.malumot() + "\n")



m1 = Murabiy("Pep Guardiola", "Futbol")
m2 = Murabiy("Carlo Ancelotti", "Futbol")


s1 = Sportchi("Mbappe", 25, m1)
s2 = Sportchi("Haaland", 24, m1)
s3 = Sportchi("Vinicius", 24, m2)
s4 = Sportchi("Bellingham", 21, m2)


print(s1.malumot())
print(s2.malumot())
print(s3.malumot())
print(s4.malumot())


s1.saqlash()
s2.saqlash()
s3.saqlash()
s4.saqlash()