
class CultureFullName:
    def __init__(self) -> None:
        self.nameList: tuple = ()
        self.surnameList: tuple = ()


class Russian(CultureFullName):
    def __init__(self) -> None:
        super().__init__()
        self.nameList = (
            "Alexei", "Boris", "Dmitry", "Evgeny", "Ivan", "Kirill", "Mikhail", "Nikolai", "Pavel", "Sergei", 
            "Vadim", "Yuri", "Vladimir", "Oleg", "Andrei", "Anton", "Maxim", "Viktor", "Arkadiy", "Leonid", 
            "Semyon", "Valery", "Igor", "Roman", "Artur", "Stanislav"
        )
        self.surnameList = (
            "Ivanov", "Petrov", "Sidorov", "Mikhailov", "Kuznetsov", "Smirnov", "Novikov", "Popov", "Fedorov", "Morozov", 
            "Volkov", "Lebedev", "Solovyov", "Vasiliev", "Alekseev", "Belyakov", "Gusev", "Nikiforov", "Karpov", "Tarasov", 
            "Dmitriev", "Zaharov", "Chernyshev", "Kozlov", "Frolov", "Bulgakov"
        )


class English(CultureFullName):
    def __init__(self) -> None:
        super().__init__()
        self.nameList = (
        "James", "John", "Michael", "David", "William", "Richard", "Joseph", "Charles", "Thomas", "Christopher", 
        "Daniel", "Matthew", "Anthony", "Mark", "Andrew", "Joshua", "Ethan", "Samuel", "Ryan", "Alexander", 
        "Benjamin", "Henry", "Isaac", "Jack", "Luke", "Nathan"
    )
        self.surnameList = (
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", 
        "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Roberts", 
        "Walker", "Young", "Allen", "King", "Scott", "Adams"
    )


class Scandinavian(CultureFullName):
    def __init__(self) -> None:
        super().__init__()
        self.nameList = (
        "Erik", "Lars", "Nils", "Karl", "Anders", "Oskar", "Henrik", "Sven", "Bjorn", "Magnus", 
        "Frederik", "Johan", "Daniel", "Axel", "Mats", "Rolf", "Lennart", "Viktor", "Per", "Tomas", 
        "Gustav", "Bengt", "Patrik", "Kjell", "Alfred", "Jens"
    )
        self.surnameList = (
        "Andersen", "Johansson", "Olsson", "Karlsson", "Eriksson", "Larsson", "Svensson", "Nilsen", "Bjornsson", "Magnusson", 
        "Frederiksson", "Johansson", "Axelsson", "Rolfsson", "Lennartsson", "Viktorsson", "Persson", "Tomasen", 
        "Gustavsson", "Bengtsson", "Patriksson", "Kjellsson", "Alfredsson", "Jensson", "Lindberg"
    )


class Gauls(CultureFullName):
    def __init__(self) -> None:
        super().__init__()
        self.nameList = (
        "Asterix", "Obelix", "Vercingetorix", "Dumnorix", "Brennos", "Vibrax", "Moridunum", "Druides", "Sauvage", "Belenos",
        "Lugos", "Epona", "Carnutes", "Vercassivellaunos", "Diviciacus", "Bibracte", "Arverni", "Viridomarus", "Cingetos",
        "Gergovia", "Rex", "Alouette", "Vindonnus", "Ailina", "Alauda", "Aelia"
    )
        self.surnameList = (
        "Galli", "Brennus", "Vercingetoricus", "Mermet", "Vercassivellaunos", "Chenus", "Soterix", "Cantiaci", "Virodunum", "Civitas",
        "Segovax", "Mettis", "Lingones", "Carnutes", "Tricasses", "Aedui", "Bellovaci", "Civitas", "Mandubii", "Morini", 
        "Senones", "Redones", "Rhodani", "Vosegus", "Bibracte", "Arverni"
    )


class Teutons(CultureFullName):
    def __init__(self) -> None:
        super().__init__()
        self.nameList = (
        "Hermann", "Sigurd", "Waldemar", "Otto", "Adalbert", "Dietrich", "Klaus", "Gustav", "Frederik", "Erik", 
        "Alaric", "Ragnar", "Theodor", "Wolfgang", "Johan", "Wilhelm", "Heinrich", "Viktor", "Gottfried", "Lothar", 
        "Konrad", "Bernhard", "Balthazar", "Ludwig", "Tobias", "Emil"
    )
        self.surnameList = (
        "Schmidt", "Müller", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Hoffmann", "Schäfer", 
        "Bauer", "Koch", "Richter", "Krüger", "Zimmermann", "Schulz", "Braun", "Lange", "Peters", "Hartmann", 
        "Neumann", "Schwarz", "Zimmer", "Krause", "Bergmann", "Walter"
    )
