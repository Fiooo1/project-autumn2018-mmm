import random
import json
ls=list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
base=random.randint(4,6)
p=[]
N=n=random.randint(100,250)
for i in range(base):
    l=random.choice(ls)
    p+=l
    ls.remove(l)

newn = ''
while n > 0:
    newn = str(n % base) + newn
    n //= base

answer=''
for i in newn : answer+=p[int(i)]

st=''
for i in range(base):
    st+=str(i+1)+". "
    for j in range(len(newn)-1):
        st+=str(p[0])
    st+=str(p[i])+"\n"
st+=str(base+1)+". "
for i in range(len(newn)-2):st+=str(p[0])
st+=str(p[1])+str(p[0])+"\n......."

stt=''
stt+="\tВсе "+str(base)+"-буквенные слова, составленные из букв " + ''.join(p) + " записаны в алфавитном порядке и пронумерованы. Вот начало списка:\n"
stt+=st+"\n"+"\tЗапишите слово, которое стоит на "+str(N)+"-м месте от начала списка."
stt = stt+"\nОтвет: "+answer
#print(type(stt))
_fout = open("_stdout", "wb")
#_fout.write(stt.encode())
#print(stt)
#print("Ответ: "+answer)
#print(stt)
f=json.dumps(stt)
#print(str(f.encode()))
_fout.write(f.encode())
_fout.close()
#print(f)
#print(json.loads(f))
