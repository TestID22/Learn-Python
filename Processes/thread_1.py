import _thread
#Порождает потоки выполнения пока не нажмёс 'q'
def child(tid):
    print('Hello from ', tid)

def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child ,(i,))
        if input() == 'q': 
            break

parent()

