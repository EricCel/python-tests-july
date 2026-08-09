#Build a text cleaner that removes extra spaces on either side, replaces multiple spaces with a single space, and converts everything to uppercase.
text = '           Build        a       text cleaner               that   removes    extra    spaces'
single_spacer = lambda s:" ".join(s.split()).upper()
print(single_spacer(text))