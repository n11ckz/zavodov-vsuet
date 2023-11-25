import tkinter
import requests
import json

def clicked() -> None:
    userDataDictionary: dict = getDictionaryUserData(text.get())
    newUserDataDictionary: dict = createNewDictionary(userDataDictionary)
    createJsonFile(newUserDataDictionary)
    tkinter.Label(root, text="Файл успешно создан!\nПрограмму можно закрыть").pack()

def getDictionaryUserData(user: str) -> dict:
    url: str = f"https://api.github.com/users/{user}"
    return json.loads(json.dumps(requests.get(url).json()))

def createNewDictionary(userDictionary: dict) -> dict:
    templateDictionary: dict = {
        "company": "",
        "created_at": "",
        "email": "",
        "id": "",
        "name": "",
        "url": ""
    }
    for i in templateDictionary.keys():
        if userDictionary[i] != templateDictionary[i]:
            templateDictionary[i] = userDictionary[i]
    return templateDictionary

def createJsonFile(dictionary: dict) -> None:
    with open("userData.json", 'w') as file:
        json.dump(dictionary, file, indent=2)

root = tkinter.Tk()
root.geometry("350x115")
root.title("Get JSON from Github API")
tkinter.Label(root, text="Введите имя пользователя:").pack()
text = tkinter.Entry(root, width=20)
text.pack(pady=2)
tkinter.Button(root, text="Получить JSON файл", command=clicked).pack(pady=2)
root.mainloop()