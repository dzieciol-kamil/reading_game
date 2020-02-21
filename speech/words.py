import random


class Words:
    words = ["adres", "aktor", "arbuz", "balkon", "bałwan", "doktor", "garnek", "handel", "hejnał", "indyk", "kasjer",
             "kompot", "kotlet", "kundel", "mostek", "mundur", "obrus", "odlot", "ponton", "rolnik", "sernik", "listek",
             "termos", "warkot", "Bartek", "Henryk", "Marcin", "Waldek", "Wojtek", "aparat", "budynek", "hamulec",
             "koperek", "makaron", "parasol", "pomidor", "samolot", "telefon", "tulipan", "widelec", "zegarek",
             "antena", "apteka", "benzyna", "konfitura", "sandały", "butelka", "cebulka", "kapusta", "koperta",
             "latarka", "rysunki", "sałatka", "zabawki", "lotnisko", "lusterko", "listopad", "telewizor", "kaloryfer",
             "koleżanka", "umywalka", "cebula", "banany", "fasola", "sałata", "buraki", "jagoda", "malina", "morele",
             "topola", "patyki", "motyle", "koguty", "zające", "papuga", "żyrafa", "owoce", "bilety", "fotele",
             "robota", "balony", "gotuje", "pomaga", "ląduje", "litery", "Dorota", "Agata", "Monika", "Maryla",
             "Danuta", "gazeta", "zabawa", "wizyta", "rowery", "robimy", "pakuje", "lala", "baba", "jaja", "papa",
             "data", "pada", "mapa", "rano", "pole", "łapa", "kino", "waza", "zupa", "fala", "kura", "data", "pada",
             "tama", "mapa", "luty", "rano", "pole", "fala", "sala", "woda", "ryba", "łapa", "waza", "zupa", "gapa",
             "hala", "żaba", "Ala", "Ela", "Ewa", "Ula", "Iza", "Dana", "Jola", "Lena", "Cela", "Tola", "Mira", "Aga",
             "balon", "baran", "basen", "biwak", "domek", "dywan", "kotek", "kubek", "kogut", "kajak", "lasek", "lisek",
             "fotel", "motyl", "murek", "nosek", "nurek", "pasek", "palec", "pokój", "pilot", "ranek", "rower", "rynek",
             "regał", "rybak", "serek", "synek", "wazon", "wagon", "wózek", "worek", "zając", "zamek", "zegar", "żurek",
    ]

    def get_text(self):
        return random.choice(self.words)
