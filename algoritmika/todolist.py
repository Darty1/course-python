# coding=utf-8
n = int(input("Введите количество задач: "))
i = 0
todolist = []
progress = []
while i < n:
    todolist.append(str(input("Задача "+str((i+1))+" : ")))
    progress.append(0)
    i += 1
while n != 0:
    n = int(input("""
            1 - Добавить задачу
            2 - Удалить задачу
            3 - Изменить задачу
            4 - Показать все задачи
            0 - Выход
            """))

    if n == 1:
        task = input("Введите задачу: ")
        todolist.append(task)
    elif n == 2:
        task = int(input("Введите номер задачи: "))
        todolist.remove(todolist[task-1])
        progress.remove(progress[task-1])
        print("Задача №", task, "удалена")
    elif n == 3:
        task = int(input("Введите номер задачи: "))
        progress[task-1] = int(input("Введите процент выполнения задачи: "))
    elif n == 4:
        for k in range(0, len(todolist)-1):
            print (k+1, " - ", todolist[k], ' - ', progress[k], '%')
