
def count_unique_proteins(strlist):
    return len(set([protein[:-2] for protein in strlist]))

def count_proteins(strlist):
    tempdict = {}
    for word in strlist:
        if word[:-2] in tempdict:
            tempdict[word[:-2]] += 1
        if word[:-2] not in tempdict:
            tempdict[word[:-2]] = 1
    return tempdict

def merge_protein_counts(dict1, dict2):
    tempdict = {}
    for protein in dict1:
        tempdict[protein] = (dict1[protein])
    for protein in dict2:
        if protein in tempdict:
            tempdict[protein] = (tempdict[protein], dict2[protein])
        else:
            tempdict[protein] = (0, dict2[protein])
    for protein in tempdict:
        if not isinstance(tempdict[protein], tuple):
            tempdict[protein] = (tempdict[protein], 0)
    return tempdict



months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
single_digit_days = {
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09"
}
def dates_to_iso8601(dlist):
    templist = []
    for date in dlist:
        if date[-8] == " ":
            templist.append("-".join([date[-4:], 
                                      months[date[:-8]],
                                      single_digit_days[date[-7]]]))
        else:
            templist.append("-".join([date[-4:], 
                                      months[date[:-9]],
                                      date[-8:-6]]))
    return templist

def sort_dates(dlist):    
    return sorted(dlist)

