from src.utils.helper_functions import get_group, get_root


def presente(verb):
    isc_verbs = [
     'preferire', 'attribuirsi', 'invadere', 'unire', 'contribuire',
     'pulire', 'trasferire', 'distribuire', 'investire', 'obbedire',
     'proibire', 'fallire', 'spedire', 'capire', 'tossire', 'impedire',
     'rifinire', 'integrare', 'intimorire', 'sparire', 'stupire',
     'ferire', 'gradire', 'progredire', 'impazzire', 'svanire',
     'sviluppire', 'finire', 'esaurire', 'abolire', 'inghiottire',
     'garantire', 'gestire', 'ferirsi', 'ripulire', 'promettere',
     'colpire', 'preferirsi', 'attribuire', 'arrossire', 'legare',
     'definire', 'arricchire', 'benedire', 'restituire', 'riassumere',
     'inserire', 'tradire', 'subire', 'agire', 'costruire', 'scolpire',
     'istituire', 'dimagrire', 'nutrire', 'fiorire', 'suggerire']
    group = get_group(verb)
    root = get_root(verb)
    endings = {
        "are": ["o", "i", "a", "a", "iamo", "ate", "ano", "ano"],
        "ere": ["o", "i", "e", "e", "iamo", "ete", "ono", "ono"],
        "ire": ["o", "i", "e", "e", "iamo", "ite", "ono", "ono"],
        "ciare": ["io", "i",  "ia", "ia", "iamo", "iate", "iano", "iano"],
        "giare": ["io", "i", "ia", "ia", "iamo", "iate", "iano", "iano"],
        "iare": ["io", "i", "ia", "ia", "iamo", "iate", "iano", "iano"],
        "care": ["o", "hi", "a", "a", "hiamo", "ate", "ano", "ano"],
        "gare": ["o", "hi", "a", "a", "hiamo", "ate", "ano", "ano"],
        "isc": ["isco", "isci", "isce", "isce", "iamo", "ite", "iscono", "iscono"]
    }
    if verb in isc_verbs:
        group = "isc"
    return [root + endings[group][i] for i in range(8)]
