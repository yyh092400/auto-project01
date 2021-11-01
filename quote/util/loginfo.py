
import logging
import time


class AutoLog:

    def __init__(self):
        self.logger = logging.getLogger('baiping')


    def set_info(self,level,mes):
        try:
            # 日志时间
            date_log = time.strftime('%Y-%m-%d')
            # 输出日志文件
            fh = logging.FileHandler('../../../log/autolog_' + date_log + '.log')
            # 控制台输出
            ch = logging.StreamHandler()
            # 日志格式化
            fm = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-%(message)s')
            # 日志文件加入格式化
            fh.setFormatter(fm)
            # 控制台输出加入格式化
            ch.setFormatter(fm)
            # 文件日志输出
            self.logger.addHandler(fh)
            # 控制台日志输出
            self.logger.addHandler(ch)
            # logger 对象设置输入日志等级
            self.logger.setLevel(level=logging.DEBUG)
            # 打印日志信息
            if level.lower() == 'debug':
                self.logger.debug(mes)
            elif level.lower() == 'info':
                self.logger.info(mes)
            elif level.lower() == 'warning':
                self.logger.warning(mes)
            elif level.lower() == 'error':
                self.logger.error(mes,exc_info=True,stack_info=True)
            elif level.lower() =='critical':
                self.logger.critical(mes,exc_info=True,stack_info=True)
            else:
                print('level error!')
            # 移除控制台输出
            self.logger.removeHandler(ch)
            # 移除文件输出
            self.logger.removeHandler(fh)
        except Exception as e:
            print(e, 'file operation error')
        finally:
            # 关闭控制台输出
            ch.close()
            # 关闭文件输出
            fh.close()

# log = AutoLog()
# log.set_info('info','打开浏览器')
# try:
#     print(2/0)
# except Exception as e:
#     log.set_info('error',e)
#     # e.with_traceback()
