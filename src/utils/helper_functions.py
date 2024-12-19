def get_group(verb):
    if verb.endswith("are"):
        if verb.endswith("ciare"):
            return "ciare"
        elif verb.endswith("giare"):
            return "giare"
        elif verb.endswith("iare"):
            return "iare"
        elif verb.endswith("care"):
            return "care"
        elif verb.endswith("gare"):
            return "gare"
        else:
            return "are"
    elif verb.endswith("ere"):
        return "ere"
    elif verb.endswith("ire"):
        return "ire"
    else:
        return "error"


def get_root(verb):
    end = get_group(verb)
    if end == "are" or end == "ere" or end == "ire" or end == "care" or end == "gare":
        return verb[:-3]
    elif end == "ciare" or end == "giare" or end == "iare":
        return verb[:-4]
    else:
        pass


def get_auxiliary(verb):
    essere_verbs = [
     "andare", "arrivare", "cadere", "diventare", "entrare", "partire",
     "restare", "rimanere", "salire", "scendere", "stare", "tornare",
     "uscire", "venire", "nascere", "morire", "piacere", "crescere",
     "sparire", "sembrare", "apparire", "succedere", "svanire", "giungere",
     "essere", "costare", "avvenire", "invecchiare", "arrossire",
     "esplodere", "comparire", "riapparire", "sopravvivere", "dimagrire"
    ]
    essere_avere_verbs = [
        "cambiare", "cominciare", "finire", "passare", "correre", "salire",
        "scendere", "volare", "saltare", "migliorare", "peggiorare",
        "vivere", "continuare", "rallentare", "accelerare", "terminare",
        "avanzare", "retrocedere", "provare", "spostare", "trasferire",
        "incontrare", "attraversare", "montare", "rotolare", "fuggire",
        "arrestare", "fermarsi", "riaprire", "svegliare", "allontanare"
    ]
    if verb in essere_avere_verbs:
        return "essere_avere"
    elif verb in essere_verbs:
        return "essere"
    else:
        return "avere"


def get_participio(verb):
    end = get_group(verb)
    root = get_root(verb)
    if end == "are" or end == "care" or end == "gare":
        return root + "ato"
    elif end == "ere":
        return root + "uto"
    elif end == "ire":
        return root + "ito"
    elif end == "iare" or end == "giare" or end == "ciare":
        return root + "iato"
    else:
        pass


def change_participio_with_essere(part):
    return [part, part, part, part[:-1] + "a", part[:-1] + "i", part[:-1] + "i", part[:-1] + "i", part[:-1] + "e"]


