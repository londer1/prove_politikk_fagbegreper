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
        "answer": "a"
    },
    {
        "question": "Hva beskriver et diktatur?",
        "options": {
            "a": "Styresett der folk har rett til å delta i politiske beslutninger.",
            "b": "Styresett der én person eller en liten gruppe har total makt.",
            "c": "Styresett med et flerpartisystem og frie valg."
        },
        "answer": "b"
    },
    {
        "question": "Hva er folkesuverenitet?",
        "options": {
            "a": "Prinsippet om at myndighetene utøver makt på vegne av folket.",
            "b": "Prinsippet om at en liten gruppe styrer på vegne av folket.",
            "c": "Prinsippet om at folket er underlagt statens lovgivning."
        },
        "answer": "a"
    },
    {
        "question": "Hva er maktfordelingsprinsippet?",
        "options": {
            "a": "Prinsippet om at makten i et samfunn bør deles mellom tre uavhengige grener.",
            "b": "Prinsippet om at en leder skal ha absolutt makt over staten.",
            "c": "Prinsippet om at makten kun skal være i hendene på folket."
        },
        "answer": "a"
    },
    {
        "question": "Hva er en ideologi?",
        "options": {
            "a": "En økonomisk modell for å sikre velstand.",
            "b": "Et sett med ideer og verdier for hvordan samfunnet bør organiseres.",
            "c": "Et sosialt nettverk som forener ulike grupper."
        },
        "answer": "b"
    },
    {
        "question": "Hva er kjernen i sosialisme?",
        "options": {
            "a": "At ressursene i samfunnet bør fordeles mer rettferdig.",
            "b": "At samfunnet skal styres av en sterk, sentralisert leder.",
            "c": "At individuell frihet og minimal statlig innblanding er viktig."
        },
        "answer": "a"
    },
    {
        "question": "Hva kjennetegner liberalisme?",
        "options": {
            "a": "Fokus på individuell frihet og minimal statlig innblanding.",
            "b": "Fokus på kollektivt ansvar og staten som sentral aktør.",
            "c": "Fokus på tradisjonelle verdier og skepsis til endring."
        },
        "answer": "a"
    },
    {
        "question": "Hva er et ekkokammer?",
        "options": {
            "a": "Et miljø hvor folk hører ulike perspektiver og synspunkter.",
            "b": "Et miljø hvor folk kun hører synspunkter som bekrefter deres egne meninger.",
            "c": "Et miljø hvor folk deler sine erfaringer uten å bli utfordret."
        },
        "answer": "b"
    }
]

# Funksjon for å stille spørsmål
def ask_question(q):
    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}: {value}")
    answer = input("Svar (a, b, eller c): ").lower()
    return answer == q["answer"]

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
        else:
            print("Feil.\n")

    print(f"Du fikk {score} av {total} riktige svar!")

# Start quiz
if __name__ == "__main__":
    start_quiz()