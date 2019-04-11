import  sys, signal, time
'''
Обработка сигналов, номер сигнала N передаётся как аргумент 
командной стркои, чтобы передать сигнал этому проссу, искользуйте
команду оболочки "kill -N pid"; большинство обрбочиков сигналов
восстанавливаются интерпертатором полсе обработки сигнла.
в ВИДЕ (гаддем) signal также доступен, но он определяет небольшое
количество типов сигналов, а крооме того в Винде, отствует функция os.kill\
'''
#покажет дату и текущее время и год
def now():
    return time.ctime(time.time())

def onSignal(signum, stackframe):
    print('Got signal', signum, 'at', now())

signum = int(sys.argv[1])
signal.signal(signum, onSignal)
while True:
    signal.pause()