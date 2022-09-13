from datetime import datetime

class JatoMilitar:
    def __init__(self, modelo, base) -> None:
        self.modelo = modelo
        self.baseinicial = base
        self.base = base
        self.history = []
    def designar_piloto(self, piloto):
        self.piloto = piloto
    def rebasear_aeronave(self, base):
        if hasattr(self, 'piloto'):
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
            self.history.append({"Base Anterior":self.base,
                                "Nova Base": base,
                                "Data e Hora": data_e_hora_em_texto})
            self.base = base
        else:
            print("Nave sem piloto")
    def __str__(self):
        if hasattr(self, 'piloto'):
            piloto = self.piloto
        else:
            piloto = "Nave sem piloto"
        return f"""
        Jato: {self.modelo}
        Base Inicial: {self.baseinicial}
        Piloto: {piloto}
        Histórico: {self.history}
        """

jato = JatoMilitar("Falcon-192", "Base-01")
jato.designar_piloto("Piloto-01")
jato.rebasear_aeronave("Base-02")
jato.rebasear_aeronave("Base-05")
print(jato)