import time

class Musica:
    def __init__(self, string) -> None:
        self.string  = string
    def cante_para_mim(self):
        estrofes = self.string.split(" ")
        for i in estrofes:
            print(i)
            time.sleep(0.3)

Musica("""arittakeno yume o kakiatsume
sagashi mono sagashini yuku no sa one piece

rashinban nante jyutai no moto
netsu ni ukasare kaji o toru no sa

hokori ka butteta takara no chizu mo
tashikameta no nara densetsu jyanai!

kojin teki na arashi wa dareka no
baiorizumu nokkatte
omoi sugose ba ii

arittakeno yume o kakiatsume
sagashi mono sagashi ni yuku no sa
Pocket no coin, soreto
You wanna be my friend?
We are, we are on the cruise! We are!

zembu mani ukete shinji chattemo
kata o osarete iippo lead sa

kondo aetanara hanasu tsumorisa
sore kara no koto to kore kara no koto

tsumari itsumo pinch wa dareka ni
appeal dekiru ii chance
ji ishiki kajyoo ni!

shimittareta yoru o buttobase!
takara bako ni kyoumi wa nai kedo
Pocket ni roman, soreto
You wanna be my friend?
We are, we are on the cruise! We are!

arittakeno yume o kakiatsume
sagashi mono sagashini yuku no sa
Pocket no coin, soreto
You wanna be my friend?
We are, we are on the cruise! We are!

We are! We are!

""").cante_para_mim()