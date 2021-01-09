def black_wrapper(fun):
    def run(*args,**kwargs):
        # 取find函数里的第一个参数，即self，那么basepage就相当于self
        basepage=args[0]
        try:
            return fun(*args,**kwargs)
        # 捕获元素没找到的异常
        except Exception as e:
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles=basepage.finds(*black)
                if len(eles)>0:
                    # 对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return fun(*args,**kwargs) # 找到后返回自己继续点击
            raise e
    return run