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
res = con.get_config('basic', 'MaxFoodTime')
res = con.get_config('basic', 'MinFoodTime')
res = con.get_config('basic', 'OrderPerSecond')
res = con.get_config('basic', 'ArriveTime')
if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('basic', 'MaxFoodTime')
    res = con.get_config('basic', 'MinFoodTime')
    res = con.get_config('basic', 'OrderPerSecond')
    res = con.get_config('basic', 'ArriveTime')

    print(con.config_dic)

