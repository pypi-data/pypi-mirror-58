#创建一个用来处理列表的函数
def print_li(the_list):
    for ue in the_list:
        #判断数据类型是不是列表
        if isinstance(ue, list):
            print_li(ue)
        else:
            print(ue)