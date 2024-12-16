import random

# Spørsmålene og svaralternativene
questions = [
    {
        "question": "Hva er et kjennetegn ved et demokrati?",
        "options": {
            "a": "Folk har rett til å delta i beslutningene som påvirker samfunnet.",
            "b": "Makt er konsentrert hos én person eller en liten gruppe.",
            "c": "Myndighetene styrer uten at folket har innflytelse."
        },
        "answer": "a",
        "explanation": "Demokrati betyr at folk kan være med på å bestemme viktige saker, for eksempel gjennom valg."
    },
    {
        "question": "Hva beskriver et diktatur?",
        "options": {
            "a": "Styresett der folk har rett til å delta i politiske beslutninger.",
            "b": "Styresett der én person eller en liten gruppe har total makt.",
            "c": "Styresett med et flerpartisystem og frie valg."
        },
        "answer": "b",
        "explanation": "I et diktatur er det en person eller en liten gruppe som har all makten, og folk kan ikke bestemme."
    },
    {
        "question": "Hva er folkesuverenitet?",
        "options": {
            "a": "Prinsippet om at myndighetene utøver makt på vegne av folket.",
            "b": "Prinsippet om at en liten gruppe styrer på vegne av folket.",
            "c": "Prinsippet om at folket er underlagt statens lovgivning."
        },
        "answer": "a",
        "explanation": "Folkesuverenitet betyr at folk bestemmer hvem som skal ha makt, for eksempel gjennom valg."
    },
    {
        "question": "Hva er maktfordelingsprinsippet?",
        "options": {
            "a": "Prinsippet om at makten i et samfunn bør deles mellom tre uavhengige grener.",
            "b": "Prinsippet om at en leder skal ha absolutt makt over staten.",
            "c": "Prinsippet om at makten kun skal være i hendene på folket."
        },
        "answer": "a",
        "explanation": "Maktfordeling betyr at makten deles mellom regjeringen, parlamentet og domstolene for å unngå at noen får for mye makt."
    },
    {
        "question": "Hva er en ideologi?",
        "options": {
            "a": "En økonomisk modell for å sikre velstand.",
            "b": "Et sett med ideer og verdier for hvordan samfunnet bør organiseres.",
            "c": "Et sosialt nettverk som forener ulike grupper."
        },
        "answer": "b",
        "explanation": "En ideologi handler om hvilke ideer man mener er best for hvordan samfunnet skal være."
    },
    {
        "question": "Hva er kjernen i sosialisme?",
        "options": {
            "a": "At ressursene i samfunnet bør fordeles mer rettferdig.",
            "b": "At samfunnet skal styres av en sterk, sentralisert leder.",
            "c": "At individuell frihet og minimal statlig innblanding er viktig."
        },
        "answer": "a",
        "explanation": "Sosialisme mener at ressursene bør deles mer rettferdig for å hjelpe folk som har det vanskelig."
    },
    {
        "question": "Hva kjennetegner liberalisme?",
        "options": {
            "a": "Fokus på individuell frihet og minimal statlig innblanding.",
            "b": "Fokus på kollektivt ansvar og staten som sentral aktør.",
            "c": "Fokus på tradisjonelle verdier og skepsis til endring."
        },
        "answer": "a",
        "explanation": "Liberalisme handler om å gi folk mer frihet og mindre styring fra staten."
    },
    {
        "question": "Hva er et ekkokammer?",
        "options": {
            "a": "Et miljø hvor folk hører ulike perspektiver og synspunkter.",
            "b": "Et miljø hvor folk kun hører synspunkter som bekrefter deres egne meninger.",
            "c": "Et miljø hvor folk deler sine erfaringer uten å bli utfordret."
        },
        "answer": "b",
        "explanation": "Et ekkokammer kan for eksempel være når du bare ser TikTok-videoer som er enig med ditt syn, og aldri blir utfordret til å tenke på andre synspunkter."
    },
    # Nye spørsmål
    {
        "question": "Hva kjennetegner en rettsstat?",
        "options": {
            "a": "Myndighetene kan handle vilkårlig uten rettslig kontroll.",
            "b": "Alle er underlagt loven, og ingen står over den.",
            "c": "Retten til å delta i valg er begrenset."
        },
        "answer": "b",
        "explanation": "I en rettsstat er ingen over loven, og rettferdighet og likebehandling er sentralt."
    },
    {
        "question": "Hva betyr pluralisme i et samfunn?",
        "options": {
            "a": "At kun én ideologi er tillatt.",
            "b": "At ulike synspunkter kan sameksistere og bli hørt.",
            "c": "At folk bare får høre én type informasjon."
        },
        "answer": "b",
        "explanation": "Pluralisme innebærer at samfunnet er åpent for forskjellige synspunkter og ideer."
    },
    {
        "question": "Hva er menneskerettigheter?",
        "options": {
            "a": "Rettigheter som bare gjelder for enkelte grupper i samfunnet.",
            "b": "Rettigheter som gjelder for alle mennesker, uavhengig av nasjonalitet eller bakgrunn.",
            "c": "Rettigheter som kan tas bort av myndighetene."
        },
        "answer": "b",
        "explanation": "Menneskerettigheter er grunnleggende rettigheter som alle mennesker har rett til."
    },
    {
        "question": "Hva innebærer medborgerskap?",
        "options": {
            "a": "At man har plikter som å betale skatt, men ikke rettigheter som stemmerett.",
            "b": "At man har både rettigheter som stemmerett og plikter i samfunnet.",
            "c": "At man kun har rettigheter og ingen plikter."
        },
        "answer": "b",
        "explanation": "Medborgerskap innebærer både rettigheter og plikter, som for eksempel stemmerett og ansvar for samfunnet."
    },
    {
        "question": "Hva betyr mistillit i et politisk system?",
        "options": {
            "a": "At folk har tillit til myndighetene.",
            "b": "At folk mister tilliten til regjeringen og dens evne til å lede.",
            "c": "At folk ikke har noen meninger om myndighetene."
        },
        "answer": "b",
        "explanation": "Mistillit skjer når folk mister tilliten til regjeringen, og det kan føre til at de mister makten."
    },
    {
        "question": "Hva kjennetegner konservatisme?",
        "options": {
            "a": "En tro på tradisjonelle verdier og motstand mot raske endringer.",
            "b": "Fokus på individuell frihet og minimal statlig innblanding.",
            "c": "Tro på et klasseløst samfunn og rettferdig fordeling av rikdom."
        },
        "answer": "a",
        "explanation": "Konservatisme handler om å bevare tradisjonelle verdier og motsette seg raske endringer i samfunnet."
    }
]

# Funksjon for å stille spørsmål
def ask_question(q):
    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}: {value}")
    answer = input("Svar (a, b, eller c): ").lower()
    if answer != q["answer"]:
        print(f"Feil. Riktig svar er: {q['answer']}. {q['explanation']}\n")
        return False
    return True

# Øvefunksjon
def start_quiz():
    random.shuffle(questions)  # Bland spørsmålene
    score = 0
    total = len(questions)

    print("Velkommen til øvingen! Svar på spørsmålene med a, b eller c.\n")
    for q in questions:
        if ask_question(q):
            print("Riktig!\n")
            score += 1

    print(f"Du fikk {score} av {total} riktige svar!")

# Start quiz
if __name__ == "__main__":
    start_quiz()
