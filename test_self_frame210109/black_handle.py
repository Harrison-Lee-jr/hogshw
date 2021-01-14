import logging

import allure
logging.basicConfig(level=logging.INFO)
# error > info > debug

def black_wrapper(fun):
    '''python cookbook--闭包'''
    def run(*args,**kwargs):
        # 取find函数里的第一个参数，即self，那么basepage就相当于self
        basepage=args[0]
        try:
            logging.info('start find: \nargs: '+str(args)+' kwargs: '+ str(kwargs))
            return fun(*args,**kwargs)
        # 捕获元素没找到的异常
        except Exception as e:
            # 错误截图
            basepage.screenshot('tmp.png')
            with open('./tmp.png','rb') as f:
                pic=f.read()
            # 截图传到allure里，命令行运行 pytest test_search.py --alluredir ../result
            allure.attach(pic,attachment_type=allure.attachment_type.PNG)
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles=basepage.finds(*black)
                if len(eles)>0:
                    # 对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return fun(*args,**kwargs) # 找到后返回自己继续点击
            raise e
    return run