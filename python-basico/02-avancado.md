# Avançado

Aqui encontran-se as anotações daquilo que é novidade para mim.

## Panda

Biblioteca Panda le arquivo .csv e transforma em data frame.

```python
import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)
```

## Compressão de listas

```python
users = [user for id in user_ids if (user := get_user(id)) is not None]
```

Isso é o mesmo que

```python
users = []
 for id in user_ids:
     user = get_user(id)
     if user is not None:
         users.append(user)
```


