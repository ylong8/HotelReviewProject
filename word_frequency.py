# Put this code in the directory where the review txt file is
# Change the file name for both good and bad reviews

# Code by Yufei Long
# It can be improved by using tokenize in nltk
import nltk
import pandas as pd
stop = ["a", "about",'-',"above", "above","across", "after", "afterwards","again", "against", "all", "almost","alone", "along", "already", "also","although","always","am","among","amongst", "amoungst", "amount","an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere","are", "around", "as",  "at", "back","be","became","because","become","becomes", "becoming","been", "before", "beforehand", "behind","being", "below", "beside", "besides","between", "beyond", "bill", "both","bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred",'i',"ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

# Load review from good hotels
good = pd.read_table('5-Star-GOOD.txt', sep = '|', header=None, names = ["Reviews"])
# Load review from bad hotels
bad = pd.read_table('5-Star-NOT GOOD.txt', sep = '|', header=None, names = ["Reviews"])
good_words =[]
bad_words=[]
for i in good.Reviews:
    i = i.split(' ')
    for j in i:
        j = j.lower()
        if j not in stop:
            good_words.append(j)
n = len(good_words)
print('The good review for this star level contains '+str(n)+' words')
good_words = nltk.FreqDist(good_words)
print('Here it is the most common 30 words:')
for i in good_words.most_common(30):
    print (str(i) +'\t'+ str(round(float(i[1])/float(n),4)/0.01)+'%')


    
print('\n')
print ('-----------------------')
print('\n')


for i in bad.Reviews:
    i = i.split(' ')
    for j in i:
        j = j.lower()
        if j not in stop:
            bad_words.append(j)
n = len(bad_words)
print('The bad review for this star level contains '+str(n)+' words')
bad_words = nltk.FreqDist(bad_words)
print('Here it is the most common 30 words:')
for i in bad_words.most_common(30):
    print (str(i) +'\t'+ str(round(float(i[1])/float(n),4)/0.01)+'%')


