Конечно! Вот содержимое `README.md` файла в одном текстовом блоке:

````markdown
# Vigenere and Caesar Cipher Brute Force API

## Описание

Этот API предоставляет возможности для шифрования и дешифрования текстов, а также для взлома шифров Виженера и Цезаря.

## Установка

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Перейдите в директорию проекта:

   ```sh
   cd yourrepository
   ```

3. Установите требуемые зависимости:

4. Запустите сервер:

   python3 app.apy or python app.py

## Маршруты

### 1. `/encrypt/vigenere`

**Описание:** Шифрование текста с использованием шифра Виженера.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "YOUR TEXT HERE",
  "key": "YOURKEY"
}
```
````

**Ответ:**

```json
{
  "encrypted_text": "ENCRYPTED TEXT"
}
```

### 2. `/decrypt/vigenere`

**Описание:** Дешифрование текста с использованием шифра Виженера.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "ENCRYPTED TEXT",
  "key": "YOURKEY"
}
```

**Ответ:**

```json
{
  "decrypted_text": "YOUR TEXT HERE"
}
```

### 3. `/encrypt/shift`

**Описание:** Шифрование текста с использованием шифра Цезаря.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "YOUR TEXT HERE",
  "shift": 3
}
```

**Ответ:**

```json
{
  "encrypted_text": "ENCRYPTED TEXT"
}
```

### 4. `/decrypt/shift`

**Описание:** Дешифрование текста с использованием шифра Цезаря.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "ENCRYPTED TEXT",
  "shift": 3
}
```

**Ответ:**

```json
{
  "decrypted_text": "YOUR TEXT HERE"
}
```

### 5. `/bruteforce/vigenere`

**Описание:** Взлом шифра Виженера методом brute force.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "ENCRYPTED TEXT",
  "target_word": "TARGET WORD"
}
```

**Ответ:**

```json
{
    "possible_decryptions": [
        {
            "decryption": "DECRYPTED TEXT",
            "key": "USED KEY",
            "meaningful_score": 3
        },
        ...
    ]
}
```

### 6. `/bruteforce/shift`

**Описание:** Взлом шифра Цезаря методом brute force.

**Метод:** POST

**Тело запроса:**

```json
{
  "data_in": "ENCRYPTED TEXT"
}
```

**Ответ:**

```json
{
    "possible_decryptions": [
        {
            "decryption": "DECRYPTED TEXT",
            "shift": 3,
            "meaningful_score": 3
        },
        ...
    ]
}
```

```

```
