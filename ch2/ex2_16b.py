#
# textwrap.wrap(text, width=70, **kwargs)
#     Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, without final newlines.
#     Optional keyword arguments correspond to the instance attributes of TextWrapper, documented below. width defaults to 70.
#     See the TextWrapper.wrap() method for additional details on how wrap() behaves.
# textwrap.fill(text, width=70, **kwargs)
#     Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph. fill() is shorthand for
#     "\n".join(wrap(text, ...))
import textwrap

#################################################################################
sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''

print(sample_text)
print(textwrap.wrap(sample_text,width=5))
print(textwrap.wrap(sample_text2,width=5))

#输出结果：
#aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk
#['aaabb', 'bcccd', 'ddeee', 'edddd', 'dffff', 'fgggg', 'ghhhh', 'hhkkk', 'kkkk']
#['aaa', 'bbb', 'ccc', 'ddd', 'eeee', 'ddddd', 'fffff', 'ggggg', 'hhhhh', 'h kkk', 'kkkk']     #并不是保证了每个list元素都是按照width的，因为不但要考虑到width，也要考虑到空格，
################################################################################################

#################################################################################
sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''

print(textwrap.fill(sample_text,width=5))
print('****')
print(textwrap.fill(sample_text2,width=5))

#输出结果：
# aaabb
# bcccd
# ddeee
# edddd
# dffff
# fgggg
# ghhhh
# hhkkk
# kkkk
# ****
# aaa
# bbb
# ccc
# ddd
# eeee
# ddddd
# fffff
# ggggg
# hhhhh
# h kkk
# kkkk
#########################################################


#####textwrap.dedent(text) ;  Remove any common leading whitespace from every line in text.
#"  hello" and "\thello" are considered to have no common leading whitespace.
# end first line with \ to avoid the empty line!
s = '''\
hello
  world
'''
print(repr(s))          # prints '    hello\n      world\n    '
print(textwrap.dedent(s))  # prints 'hello\n  world\n'
