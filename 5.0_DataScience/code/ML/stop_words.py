
hundreds_of_other_words=["asd","dfg"]
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list
# False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set
# very fast to check
