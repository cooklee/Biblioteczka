class Zwierze:

    def przedstaw_sie(self):
        print("jestem zwierze")

class Ssak(Zwierze):

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print('jestem ssak')

class Latawiec:
    def lataj(self):
        print('latam sobie')

class Kot(Ssak):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("jestem Kot")

class Nietoperz(Ssak, Latawiec):
    pass


k = Kot()

k.przedstaw_sie()
