import configparser
config_good = configparser.RawConfigParser()
config_good.read(r'C:\Actimize\ais_server\Add-Ons\Name Analytics\Configuration\culture_Organizations.config')

config_bad = configparser.RawConfigParser()
config_bad.read(r'C:\Actimize417\ais_server\Add-Ons\Name Analytics\Configuration\culture_Organizations.config')



for section in config_good.sections():
    print("[" , section ,"]")
    config_good_sec = config_good[section]
    config_bad_sec = config_bad[section]

    iter = 0
    for key_good in config_good_sec:
        iter = iter + 1
        if config_bad.has_option(section,key_good):
            if config_good_sec[key_good] == config_bad_sec[key_good]:
                print("----> BOTH", "\t(", iter, ")", key_good, "=", config_good_sec[key_good])
            else:

                print("----> SR#0243673","\t(",iter , ")", key_good, "=", config_good_sec[key_good] )
                print("----> Default","\t\t(",iter, ")", key_good, "=", config_bad_sec[key_good] )
        else:
            print("SR#0243673",iter, key_good, "=", config_good_sec[key_good] )
            print("----> Default", iter, key_good, "=", "*******   MISSING   *******")
