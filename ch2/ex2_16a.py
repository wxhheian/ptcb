#多行表多行
##使用'''三引号
>>> str1 = '''Le vent se lève, il faut tenter de vivre.
起风了，唯有努力生存。
（纵有疾风起，人生不言弃。）'''

>>> str1
'Le vent se lève, il faut tenter de vivre. \n起风了，唯有努力生存。\n（纵有疾风起，人生不言弃。）'

>>> print(str1)
Le vent se lève, il faut tenter de vivre.
起风了，唯有努力生存。
（纵有疾风起，人生不言弃。）


##使用反斜杠 ,一个长字符串一行表示不下，多行表示更为美观，实质上字符串还是一行。
>>> str2 = 'Le vent se lève, il faut tenter de vivre. \
起风了，唯有努力生存。\
（纵有疾风起，人生不言弃。）'

>>> str2
'Le vent se lève, il faut tenter de vivre. 起风了，唯有努力生存。（纵有疾风起，人生不言弃。）'

#使用小括号，实行上是一行
>>> str3 = ('Le vent se lève, il faut tenter de vivre.'
'起风了，唯有努力生存。'
'（纵有疾风起，人生不言弃。）')

>>> str3
'Le vent se lève, il faut tenter de vivre.起风了，唯有努力生存。（纵有疾风起，人生不言弃。）'
