import Batiment
#n'oublier pas que python otorise 
# l'heritage multiple () heritage en diamant )on les séparer 
# par des virgures au niveau de classe entre parentése

class Maison(Batiment):
    #definition d'une maison
    nbr_maison=0
    max_maison=100
    def __init__(self,categori,long,larg,model,orientation):
        #initialisateur de MAison
        if Maison.nbr_maison>=Maison.max_maison:
            raise RuntimeError("trop de maisons construites")
        #appleler l'initialisateur de la classe aprente batiment .__init_
        super().__init__("habitat",long,larg)
        self.model=model
        self.orientation=orientation
        Maison.nbr_maison +=1
    def orienter_soleil(self):
        #changement de sens d'orientation de la maison vers le sud
        self.orientation="sud"