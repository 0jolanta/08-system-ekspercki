from experta import KnowledgeEngine, DefFacts, Fact, Rule, NOT, W, MATCH
import ast


class MedicalExpert(KnowledgeEngine):
    username = "", 

    @DefFacts()
    def needed_data(self):
        yield Fact(findDisease = 'true')
        print("Witam! Jestem Dr Ekspert.","Zadam ci 10 pytań. Na każde pytanie odpowiedz tak lub nie")
        
    @Rule(Fact(findDisease = 'true'),NOT(Fact(name=W())),salience = 1000)
    def ask_name(self):
        self.username = input("Jak masz na imię?\n")
        self.declare(Fact(name=self.username))

    @Rule(Fact(findDisease='true'), NOT (Fact(chestPain = W())),salience = 995)
    def hasChestPain(self):
        self.chest_pain = input("\n Czy masz ból w klatce piersiowej? \n")
        self.chest_pain = self.chest_pain.lower()
        self.declare(Fact(chestPain = self.chest_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        self.cough = input("\n Czy masz kaszel? \n")
        self.cough = self.cough.lower()
        self.declare(Fact(cough = self.cough.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
        self.fainting = input("\n Czy zdaża ci się mieć omdlenia? \n")
        self.fainting = self.fainting.lower()
        self.declare(Fact(fainting = self.fainting.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        self.fatigue = input("\n Czy sporadycznie odczuwasz zmęczenie? \n")
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        self.headache = input("\n Czy masz bóle głowy? \n")
        self.headache = self.headache.lower()
        self.declare(Fact(headache = self.headache.strip().lower()))
    

    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        self.back_pain = input("\n Czy miewasz bóle pleców?\n")
        self.back_pain = self.back_pain.lower()
        self.declare(Fact(back_pain = self.back_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(sunken_eyes = W())),salience = 950)
    def hasSunkenEyes(self):
        self.sunken_eyes = input("\n Czy zdarzają Ci się mieć zapadnięte oczy? \n")
        self.sunken_eyes = self.sunken_eyes.lower()
        self.declare(Fact(sunken_eyes = self.sunken_eyes.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fever = W())),salience = 945)
    def hasfever(self):
        self.fever = input("\n Czy masz gorączkę? \n")
        self.fever=self.fever.lower()
        self.declare(Fact(fever = self.fever.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sore_throat = W())),salience = 940)
    def hassorethroat(self):
        self.sore_throat = input("\n Czy masz ból gardła? \n")
        self.sore_throat = self.sore_throat.lower()
        self.declare(Fact(sore_throat = self.sore_throat.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(restlessness = W())),salience = 935)
    def hasrestlessness(self):
        self.restlessness = input("\n Czy odczuwasz niepokój? \n")
        self.restlessness = self.restlessness.lower()
        self.declare(Fact(restlessness = self.restlessness.strip().lower()))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'tak'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headche = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'tak'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'tak'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'tak'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_1(self):
        self.declare(Fact(disease = 'Alzheimer'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'tak'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'tak'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'no'))
    def disease_2(self):
        self.declare(Fact(disease = 'Astma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'tak'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'tak'))
    def disease_3(self):
        self.declare(Fact(disease = 'Cukrzyca'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headache = 'tak'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'tak'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_4(self):
        self.declare(Fact(disease = 'Padaczka'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'tak'),Fact(fever = 'tak'),Fact(sore_throat='tak'),
    Fact(restlessness = 'nie'))
    def disease_5(self):
        self.declare(Fact(disease = 'Jaskra'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'tak'),Fact(fatigue = 'nie'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_6(self):
        self.declare(Fact(disease = 'Choroba serca'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'tak'),Fact(fatigue = 'nie'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'tak'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_7(self):
        self.declare(Fact(disease = 'Udar cieplny'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'tak'),Fact(fever = 'nie'),Fact(sore_throat='nie'),
    Fact(restlessness = 'tak'))
    def disease_8(self):
        self.declare(Fact(disease = 'Nadczynność tarczycy'))
    
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'tak'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'tak'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'nie'),Fact(sore_throat='tak'),
    Fact(restlessness = 'nie'))
    def disease_9(self):
        self.declare(Fact(disease = 'Hipotermia'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'tak'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headache = 'tak'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'tak'),Fact(sore_throat='nie'),
    Fact(restlessness = 'nie'))
    def disease_10(self):
        self.declare(Fact(disease = 'Żółtaczka'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'nie'),
    Fact(headache = 'tak'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'nie'),Fact(fever = 'tak'),Fact(sore_throat='tak'),
    Fact(restlessness = 'nie'))
    def disease_11(self):
        self.declare(Fact(disease = 'Zapalenie zatok'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'nie'), Fact(cough = 'nie'), Fact(fainting = 'nie'),Fact(fatigue = 'tak'),
    Fact(headache = 'nie'),Fact(back_pain = 'nie'),Fact(sunken_eyes = 'tak'),Fact(fever = 'tak'),Fact(sore_throat='nie'),
    Fact(restlessness = 'tak'))
    def disease_12(self):
        self.declare(Fact(disease = 'Gruźlica'))


    @Rule(Fact(findDisease='true'),NOT (Fact(disease = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = 1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            mapDisease = []
            mapDisease.append('back_pain')
            mapDisease.append('chest_pain')
            mapDisease.append('cough')
            mapDisease.append('fainting')
            mapDisease.append('fatigue')
            mapDisease.append('fever')
            mapDisease.append('headache')
            mapDisease.append('sore_throat')
            mapDisease.append('restlessness')
            mapDisease.append('sunken_eyes') 
            print('\n\n Sprawdziliśmy następujące objawy',mapDisease)
            mapDisease_val=[self.back_pain,self.chest_pain,self.cough,self.fainting,self.fatigue
            ,self.fever,self.headache,self.sore_throat,self.restlessness,self.sunken_eyes]
            print('\n\n Objawy u pacjentów to:', mapDisease_val)
            
            file = open("disease_symptoms.txt", "r", encoding="utf-8")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()
            
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'tak':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            print('\n\n Zauważone objawy to: ', yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_symptoms:
                        count+=1
               
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                print("Nie stwierdzono żadnych chorób. Jesteś zdrowy!")
            else:
                print("\n\n Nie jesteśmy w stanie powiedzieć Ci dokładnej choroby. Ale wierzymy, że cierpisz na",pred_dis)
                
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')

                print ('\n\n Kilka informacji na temat choroby:',pred_dis)
                
                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r", encoding="utf-8")
                print(f.read())
                print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n\n Nie musisz się martwić',self.username,'. Mamy dla Ciebie nawet kilka środków zapobiegawczych!\n')
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r", encoding="utf-8")
                print(f.read())
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
        else:
            print('TNajbardziej prawdopodobna choroba, na którą cierpisz to:',disease)
            print('\n\n')
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('Kilka informacji na temat choroby:\n')
            print(disease)
            f = open("disease/disease_descriptions/" + disease + ".txt", "r", encoding="utf-8")
            print(f.read())
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('\n\n Nie musisz się martwić',self.username,'. Mamy dla Ciebie nawet kilka środków zapobiegawczych!\n')
            f = open("disease/disease_treatments/" + disease + ".txt", "r", encoding="utf-8")
            print(f.read())

if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print('Wydruk faktów:',engine.facts)
   