import random
import sys

def initial_values(m):
    a = ["не делится ", "кратно ", "положительно ", "отрицательно ", "больше ", "меньше "]
    b = ["не делится ", "кратна ", "положительна ", "отрицательна ", "больше ", "меньше "]
    с = [""]*8
    if len(m) != 1:
        _d = {}
        for sarg in m[1:]:
            key, value = sarg.split("=")
            key=int(key)
            _d.update({key:value})
        try:
            if _d[1] == "не делится" or _d[1] == "кратно" or _d[1] == "положительно" or _d[1] == "отрицательно" or _d[1] == "больше" or _d[1] == "меньше":
                c[0] = _d[1] + " "
            else:
                print("Неверный формат 1 параметра")
        except KeyError:
            c[0] = a[random.randint(0, 5)]
        try:
            if _d[2] == "не делится" or _d[2] == "кратна" or _d[2] == "положительна" or _d[2] == "отрицательна" or _d[2] == "больше" or _d[2] == "меньше":
                c[0] = _d[2] + " "
            else:
                print("Неверный формат 2 параметра")
        except KeyError:
            c[1] = b[random.randint(0, 5)]
        try:
            try:
                c[2] = int(_d[3])
            except KeyError:
                if (c[0] == "не делится ") or (c[0] == "кратно "):
                    c[2] = str(random.randint(2, 100))
                    if x == "не делится":
                        c[4] = "mod " + nx + " <> 0"
                        c[6] = "%" + nx + "!= 0"
                    else:
                        c[4] = "mod " + nx + " == 0".
                        c[6] = "%" + nx + "== 0"
                elif (c[0] == "больше ") or (c[0] == "меньше "):
                    c[2] = str(random.randint(-100, 100))
                    if x == "больше ":
                        c[4] = "> " + nx
                        c[6] = "> " + nx
                    else:
                        c[4] = "< " + nx
                        c[6] = "< " + nx
                else:
                    c[2] = ""
                    if c[0] == "положительно ":
                        с[4] = "> 0"
                        с[6] = "> 0"
                    else:
                        c[4] = "< 0"
                        c[6] = "< 0"
        except ValueError:
            print("Неверный формат 3 параметра")
        try:
            try:
                c[3] = int(_d[4])
            except KeyError:
                if (c[1] == "не делится ") or (c[1] == "кратно "):
                    c[3] = str(random.randint(2, 100))
                    if c[1] == "не делится":
                        c[5] = "mod " + nx + " <> 0"
                        c[7] = "%" + nx + "!= 0"
                    else:
                        c[5] = "mod " + nx + " == 0".
                        c[7] = "%" + nx + "== 0"
                elif (c[1] == "больше ") or (c[1] == "меньше "):
                    c[3] = str(random.randint(-100, 100))
                    if c[1] == "больше ":
                        c[5] = "> " + nx
                        c[7] = "> " + nx
                    else:
                        c[5] = "< " + nx
                        c[7] = "< " + nx
                else:
                    c[3] = ""
                    if c[1] == "положительно ":
                        с[5] = "> 0"
                        с[7] = "> 0"
                    else:
                        c[5] = "< 0"
                        c[7] = "< 0"
        except ValueError:
            print("Неверный формат 4 параметра")
        
        
        
        
            
va = sys.argv
c = initial_values(va)

dict = {'text':{'text1':['Дан целочисленный массив из 40 элементов. \
                Элементы массива могут принимать целые значения от –100 до 100 включительно.\n \
                Опишите на естественном языке или на одном из языков программирования алгоритм, позволяющий найти и вывести количество пар элементов массива, произведение которых ',
                'insert1', ', а сумма', 'insert2',
                '.\nПод парой подразумевается два подряд идущих элемента массива.'],
                'table1':{'row1':{'col1':['Паскаль'], 'col2':['Python'], 'col3':['Си']}, \
                          'row2':{'col1':['const n = 40;\n var\n  a: array [0..n-1]\n     of integer;\n  i, j, k: integer;\nbegin\n  for i:=0 to n-1 do\n     readln(a[i]);\n  ...\nend.'], \
                                  'col2':['# допускается также\n# использовать две\n# целочисленные\n# переменные j, k\na = []\nn = 40\nfor i in range(n):\n  a.append(int(input()))\n...'], \
                                  'col3':['#include <stdio.h>\n#define n 40\nint main() {\n  int a[n];\n  int i, j, k;\n  for (i = 0; i < n; i++)\n    scanf(\"%d\", &a[i]);\n  ...\n  return 0;\n}']
                                 }
                         }
                },
         'inserts':{'insert1':c[0], 'insert2':c[1], 'insert3':c[2], 'insert4':c[3], 'insert5':c[4], 'insert6':c[5], 'insert7':c[6], 'insert8':c[7]},
         'answers':{'table1':{'row1':{'col1':['k := 0;\n for i:=0 to n-2 do\n  if ((a[i]*a[i+1]) ', 'insert5', ') and (a[i]+a[i+1] ', 'insert6', ') then\n    k := k + 1;\nwriteln(k);'], \
                                      'col2':["k = 0\nfor i in range(n-1)\n  if ((a[i]*a[i+1]) ", 'insert7', ") and (a[i]+a[i+1] ", 'insert8', ")):\n    k += 1\nprint(k)"], \
                                      'col3':["k = 0;\nfor(i=0;i<n-1;i++)\n  if ((a[i]*a[i+1]) ", 'insert7', " && (a[i]+a[i+1]", 'insert8', "))\n    k ++;\nprintf(\"%d\", k);"]
                                     }
                             }
                    }
         }
    
