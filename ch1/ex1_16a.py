#过滤规则复杂，不适合用列表推导或这生成器

values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)
