import json

from jpype import *
import os

path = os.path.split(os.path.abspath(__file__))[0]

JARS = os.sep.join([path,"sdk","WaterMeter.jar"])

jvm_path = get_default_jvm_path()
# jar_path = os.path.join(os.path.abspath('.'), r'C:\Users\joe\Desktop\sdk\MeterMsgTranslate-0.0.2.jar',
#     r'C:\Users\joe\Desktop\sdk\jzq-0.0.43.jar',r'C:\Users\joe\Desktop\sdk\meter-0.1.3.jar',r'C:\Users\joe\Desktop\sdk\utils-0.0.11.jar')   # jar包路径
startJVM(jvm_path ,'ea', '-Djava.class.path={}'.format(JARS))

# JPackage = JPackage('com.cqct.MeterMsgTranslate')
java.lang.System.out.println("hello world!")
# print(JPackage.MeterMsg.analyzeMsg("25 25 bf 00 10 05 84 19 00 11 70 a1 ff ff b1 08 27 12 00 00 00 00 21 02 37 00 20 08 27 12 "
#                                    "00 51 30 12 21 c0 57 22 55 66 77 88 99 84 19 00 11 70 4e a0 d2 34 32 83 2b 68 cd bc d4 b4 "
#                                    "32 43 2b 4b 32 43 2b 4b 32 43 b2 d2 cd bc d4 b4 32 43 2d 2a 82 69 00 20 08 27 12 00 51 62 "
#                                    "12 21 c0 57 22 55 66 77 88 99 84 19 00 11 70 48 a5 d2 e6 24 57 13 72 f5 8a e4 86 70 75 1b "
#                                    "79 fc 8b e7 84 02 73 1e 7b fb 8d c0 37 20 46 ab 4b 0d 43 2b 4b 32 43 2b 0a cb bd d4 b4 32 "
#                                    "17 39 c9 c7 4c dc b4 20 53 7f ea cd bc d4 31 21 44 db 5b c2 84 e2 8d 0b 74 1d 7b f    e 89 e1 "
#                                    "80 05 7b 1c 7c 28 06 24 83 ea 23"))
# MeterMsg = JClass("com.cqct.MeterMsgTranslate.MeterMsg")
WaterMeter = JPackage('com.main').GetOrSetData #这种用法可以简化后面的书写

print(WaterMeter.analyzeMsg(json.dumps({"meterMsg":"25 25 bf 00 10 05 84 19 00 11 70 a1 ff ff b1 08 27 12 00 00 00 00 21 02 37 00 20 08 27 12 "
   "00 51 30 12 21 c0 57 22 55 66 77 88 99 84 19 00 11 70 4e a0 d2 34 32 83 2b 68 cd bc d4 b4 "
   "32 43 2b 4b 32 43 2b 4b 32 43 b2 d2 cd bc d4 b4 32 43 2d 2a 82 69 00 20 08 27 12 00 51 62 "
   "12 21 c0 57 22 55 66 77 88 99 84 19 00 11 70 48 a5 d2 e6 24 57 13 72 f5 8a e4 86 70 75 1b "
   "79 fc 8b e7 84 02 73 1e 7b fb 8d c0 37 20 46 ab 4b 0d 43 2b 4b 32 43 2b 0a cb bd d4 b4 32 "
   "17 39 c9 c7 4c dc b4 20 53 7f ea cd bc d4 31 21 44 db 5b c2 84 e2 8d 0b 74 1d 7b fe 89 e1 "
   "80 05 7b 1c 7c 28 06 24 83 ea 23"})))

java.lang.System.out.println("goodbye world!")
shutdownJVM()