- #### Jak działa dynamiczne typowanie w Pythonie
> Dynamiczne typowanie w pythonie - typy zmiennych określane są podczas wykonywania programu, a nie w trakcie jego kompilacji. W Javce i C# typowanie jest statyczne -> musi być określone przed wykonaniem programu.
>>Wadą dynamicznego typowania mogą być błędy w trakcie wykonania programu który nie zostały wykryte przez kompilator lub złe zrozumienie kodu przez innego programiste.
- #### Jak działa kompilator Pythona, co to jest byte-code , jak wygląda przykładowa treść byte-code ?
>Bytecode to forma reprezentacji kodu źródłowego, która jes stanem pośrednim między kodem źródłowym a maszynowym.
wspomaga on dzialanie aplikacji na wielu systemach bez potrzeby ponownego kompilowania.
>>
```
def hello()
    print("Hello, World!")
  1           0 LOAD_NAME                0 (print)
              2 LOAD_CONST               0 ('Hello, World!')
              4 CALL_FUNCTION            1
              6 RETURN_VALUE

```
- #### Sprawdź dlaczego w Pythonie int może pomieścić znacznie więcej niż 32 bity
> Inty w pythonie to obiekty które zarządzają swoją własną pamięcią
[LINK](https://www.linkedin.com/posts/reuven_how-big-is-a-python-integer-many-of-my-activity-7044578562690981888-FdWF/)
- #### Jeżeli temat Cię interesuje możesz obczaić też jakie są różne implementacje Pythona
> potem

---
- ### Kolekcje
>### List 
>>Listy są mutowalne czyli że można zmieniać ich zawartość [LINK](https://www.w3schools.com/python/python_lists.asp)
>>
```
numbers = [1, 2, 3, 4, 5] 
numbers.append(6)
numbers.remove(3)
numbers[0] = 0
```
>### Set
>>Sety mogą zawierać tylko unikalne wartości 
[LINK](https://www.w3schools.com/python/python_sets.asp)
>>
```
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
```
>### Tuple
>>Tuple są niemutowalne, czyli że nie można zmieniać ich zawartości
[LINK](https://www.w3schools.com/python/python_tuples.asp)
>>
```
point = (10, 20) 
```
>### dict
>>dicty składają się z par klucz-wartość, gdzie klucz musi być unikalny
[LINK](https://www.w3schools.com/python/python_dictionaries.asp)

>>
```
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  
```

---

- ### Kompresje
> 
