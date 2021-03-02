import json

libri = {
    'scienze' : {
                'titolo':'La_nuova_biologia',
                 'autore1':"David_Sadava",
                 "autore2":"David_M._Hillis",
                 "casa editrice":"Zanichelli",
                 "prezzo":"€24,40"
                },

    "storia" : {
                "titolo": "Le_pietre_parlano",
                "autore1":"Mauro_Reali", 
                "casa editrice": "Loescher",
                "prezzo":"€26,20"
                },

    "matematica" : {
                    "titolo":"Matematica_multimediale",
                    "autore1":"Grazziella_Barozzi",
                    "autore2":"Massimo_Bergamini",
                    "casa editrice":"Zanichelli",
                    "prezzo":"€41,0"
                    },

    "arte": {
            "titolo": "L'initerario_nell'arte",
             "autore1":"Giorgio_Cricco", 
             "casa editrice": "Zanichelli",
             "prezzo":"€36,70"
             },

    "grammatica" : {
                    "titolo":"Parola_chiave",
                    "autore1":"Marta_Meneghini",
                    "autore2":"Pietro_Bellesi",
                    "casa editrice":"Loescher",
                    "prezzo":"€17,90"
                    },

    "latino" : {
                "titolo":"Mirum_iter",
                "autore1":"Angela_Diotti",
                "autore2":"Mariapia_Ciuffarella",
                "casa editrice":"Pearson",
                "prezzo":"€24,40"
                },

    "fisica" : {
                "titolo":"L'Amaldi_per_i_licei_scientifici",
                "autore1":"Ugo_Amaldi",
                "casa editrice":"Zanichelli",
                "prezzo":"€28,20"
                },

    "poesia" : {
                "titolo":"Leggere_a_colori",
                "autore1":"Alberta_mariotti",
                "autore2":"Maria_Concetta_Sclafani",
                "autore3":"Amelia_Stancanelli",
                "casa editrice":"G.D'ANNA",
                "prezzo":"€17,25"
               },

    "inglese" : {
                "titolo":"Performer",
                 "autore1":"Marina_Spiazzi",
                 "autore2":"arina_Tavella",
                 "casa editrice":"Zanichelli",
                 "prezzo":"€24,00"
                },

    "epica" :  {
               "titolo":"Epica",
               "autore1":"Alberta_Mariotti",
               "autore2":"Amelia_Stancanelli",
               "casa editrice":"G.D'ANNA",
               "prezzo":"€14,90"
               },
}



with open("data.json", "w") as f:
    json.dump(libri, f, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, separators=None, default=None, sort_keys=False,  indent=3)

f.close()

with open("data.json", "r") as f:
    libri_da_file = json.load(f)

f.close()

print(libri_da_file)