import tkinter
import random
from tkinter import messagebox

#업데이트 함수
def update_tasks():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)
    numtask = len(tasks)
    label_dsp_count['text'] = numtask

#입력후 삭제 함수
def clear_listbox():
    lb_tasks.delete(0, "end")

#추가 함수
def add_task():
    label_dsply["text"] = ""
    Ntask = text_input.get()
    if Ntask != "":
        tasks.append(Ntask)
        update_tasks()
    else:
        label_dsply["text"] = "일정을 입력해 주세요."
    text_input.delete(0, 'end')

#전체삭제 함수
def delete_all():
    conf = messagebox.askquestion(
        '전체 삭제', '전체 삭제 하시겠습니까??')
    if conf.upper() == "YES":
        global tasks
        tasks = []
        update_tasks()
    else:
        pass

#완료 함수
def delete_one():
    de = lb_tasks.get("active")
    if de in tasks:
        tasks.remove(de)
    update_tasks()

#정리(오름차순) 함수
def sort_asc():
    tasks.sort()
    update_tasks()

#정리(내림차순) 함
def sort_dsc():
    tasks.sort(reverse=True)
    update_tasks()

#무작위 함수
def random_task():
    randtask = random.choice(tasks)
    label_dsply["text"] = randtask

#개수 함수
def number_task():
    numtask = len(tasks)
    label_dsply["text"] = numtask

#저장 함수
def save_act():
    savecon = messagebox.askquestion(
        '저장', '저장하시겠습니까?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass


#불러오기 함수
def load_act():
    loadcon = messagebox.askquestion(
        '불러오기', '불러오시겠습니까?')
    if loadcon.upper() == "YES":
        tasks.clear()

        with open('SaveFile.txt', 'r') as filereader:
            for line in filereader:
                currentask = line
                tasks.append(currentask)
            update_tasks()

    else:
        pass

# 종료 함수
def exit_app():
    confex = messagebox.askquestion(
        '종료하기', '종료하시겠습니까?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass


root = tkinter.Tk()

root.configure(bg="white")
root.title("일정 관리 프로그램")
root.geometry("330x280")

tasks = []

#일정관리 맨트 추가
label_title = tkinter.Label(root, text="일정관리", bg="white")
label_title.grid(row=0, column=0)

#일정 개수및 무작위 뽑기 텍스트 띄우기 창
label_dsply = tkinter.Label(root, text="", bg="white")
label_dsply.grid(row=0, column=1)

#뭔지 모르겠는데 없으면 안됨
label_dsp_count = tkinter.Label(root, text="", bg="white")
label_dsp_count.grid(row=0, column=3)

#입력 창
text_input = tkinter.Entry(root, width=20)
text_input.grid(row=1, column=1)

#일정추가하기 버튼 생성
text_add_button = tkinter.Button(
    root, text="일정추가하기", bg="white", width=20, command=add_task)
text_add_button.grid(row=1, column=0)

#일정완료 버튼 생성
delone_button = tkinter.Button(
    root, text="일정완료", bg="white", width=20, command=delete_one)
delone_button.grid(row=2, column=0)

#전체삭제 버튼 생성
delall_button = tkinter.Button(
    root, text="전체삭제", bg="white", width=20, command=delete_all)
delall_button.grid(row=3, column=0)

#정리(오름차순) 버튼 생성
sort_asc = tkinter.Button(root, text="정리(오름차순)",
                          bg="White", width=20, command=sort_asc)
sort_asc.grid(row=4, column=0)

#정리(내림차순) 버튼 생성
sort_dsc = tkinter.Button(root, text="정리(내림차순)",
                          bg="White", width=20, command=sort_dsc)
sort_dsc.grid(row=5, column=0)

#일정 무작위 뽑기 버튼 생성
random_button = tkinter.Button(
    root, text="일정 무작위 뽑기", bg="White", width=20, command=random_task)
random_button.grid(row=6, column=0)

#일정 개수 버튼 생성
number_task = tkinter.Button(
    root, text="일정 개수", bg="white", width=20, command=number_task)
number_task.grid(row=7, column=0)

#종료하기 버튼 생성
exit_button = tkinter.Button(root, text="종료하기",
                           bg="white", width=20, command=exit_app)
exit_button.grid(row=11, column=0, columnspan=2)

#일정 저장하기 버튼 생성
save_button = tkinter.Button(
    root, text="일정 저장하기", bg="white", width=20, command=save_act)
save_button.grid(row=10, column=1)

#일정 불러오기 버튼 생성
load_button = tkinter.Button(
    root, text="일정 불러오기", bg="white", width=20, command=load_act)
load_button.grid(row=10, column=0)


#리스트 박스 생성
lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)


root.mainloop()
