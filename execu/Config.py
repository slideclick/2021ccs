# -*- coding: UTF-8 -*-
import configparser
"""
"""

class ConfigParser():

    config_dic = {}
    @staticmethod
    def get_config( sector, item):
        value = None
        try:
            value = ConfigParser.config_dic[sector][item]
        except KeyError:
            cf = configparser.ConfigParser()
            cf.read('settings.ini', encoding='utf8')  #
            value = cf.get(sector, item)
            ConfigParser.config_dic[item] = value
        finally:
            return value

con = ConfigParser()
res = con.get_config('basic', 'Debug')
con.get_config('basic', 'OrdersPerSecond')
if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('basic', 'Debug')
    con.get_config('basic', 'OrdersPerSecond')
    print(con.config_dic)

