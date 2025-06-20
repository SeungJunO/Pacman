import tkinter
import random
from tkinter import messagebox

#업데이트 함수
def UpdateList():
    ClearListBox()
    for schedule in schedules:
        listboxschedules.insert("end", schedule)
    numschedule = len(schedules)
    
#입력후 삭제 함수
def ClearListBox():
    listboxschedules.delete(0, "end")
    
#추가 함수
def AddList():
    textwindow["text"] = ""
    Nschedules = textinput.get()
    if Nschedules != "":
        schedules.append(Nschedules)
        UpdateList()
    else:
        textwindow["text"] = "일정을 입력해 주세요."
    textinput.delete(0, 'end')

#전체삭제 함수
def AllCompletionList():
    completeanswer = messagebox.askquestion(
        '전체 삭제', '전체 삭제 하시겠습니까??')
    if completeanswer.upper() == "YES":
        global schedules
        schedules = []
        UpdateList()
    else:
        pass

#완료 함수
def CompletionList():
    comlpete = listboxschedules.get("active")
    if comlpete in schedules:
        schedules.remove(comlpete)
    UpdateList()

#정리(오름차순) 함수
def ascendingorder():
    schedules.sort()
    UpdateList()

#정리(내림차순) 함
def descendingorder():
    schedules.sort(reverse=True)
    UpdateList()

#무작위 함수
def RandomList():
    randomschedules = random.choice(schedules)
    textwindow["text"] = randomschedules

#개수 함수
def NumberList():
    numberschedules = len(schedules)
    textwindow["text"] = numberschedules

#저장 함수
def SaveList():
    saveanswer = messagebox.askquestion(
        '저장', '저장하시겠습니까?')
    if saveanswer.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for schedulesitem in schedules:
                filehandle.write('%s\n' % schedulesitem)
    else:
        pass

#불러오기 함수
def CallingList():
    callinganswer = messagebox.askquestion(
        '불러오기', '불러오시겠습니까?')
    if callinganswer.upper() == "YES":
        schedules.clear()

        with open('SaveFile.txt', 'r') as filereader:
            for line in filereader:
                currenschedule = line
                schedules.append(currenschedule)
            UpdateList()

    else:
        pass

# 종료 함수
def ExitApp():
    exitanswer = messagebox.askquestion(
        '종료하기', '종료하시겠습니까?')
    if exitanswer.upper() == "YES":
        toDoList.destroy()
    else:
        pass

toDoList = tkinter.Tk()

toDoList.configure(bg="snow2")
toDoList.title("일정 관리 프로그램")
toDoList.geometry("320x280")

schedules = []

#일정관리 맨트 추가
labeltitle = tkinter.Label(toDoList, text="To Do List", bg="snow2",width=20,
                            font = ("궁서체",12))
labeltitle.grid(row=0, column=0)

#일정 개수및 무작위 뽑기 텍스트 띄우기 창
textwindow = tkinter.Label(toDoList, text="", bg="snow2")
textwindow.grid(row=0, column=1)


#입력 창
textinput = tkinter.Entry(toDoList,bg="ghost white", width=20)
textinput.grid(row=1, column=1,columnspan=4)

#일정추가하기 버튼 생성
addbutton = tkinter.Button(toDoList, text="일정추가하기",
    bg="gainsboro", width=20, command=AddList)
addbutton.grid(row=1, column=0)

#일정완료 버튼 생성
Completionbutton = tkinter.Button(
    toDoList, text="일정완료", bg="gainsboro", width=20, command=CompletionList)
Completionbutton.grid(row=2, column=0)

#전체삭제 버튼 생성
AllCompletionbutton = tkinter.Button(
    toDoList, text="전체삭제", bg="gainsboro", width=20, command=AllCompletionList)
AllCompletionbutton.grid(row=3, column=0)

#정리(오름차순) 버튼 생성
asscendingbutton = tkinter.Button(toDoList, text="정리(오름차순)",
                          bg="gainsboro", width=20, command=ascendingorder)
asscendingbutton.grid(row=4, column=0)

#정리(내림차순) 버튼 생성
descendingbutton = tkinter.Button(toDoList, text="정리(내림차순)",
                          bg="gainsboro", width=20, command=descendingorder)
descendingbutton.grid(row=5, column=0)

#일정 무작위 뽑기 버튼 생성
randombutton = tkinter.Button(
    toDoList, text="일정 무작위 뽑기", bg="gainsboro", width=20, command=RandomList)
randombutton.grid(row=6, column=0)

#일정 개수 버튼 생성
numberbutton = tkinter.Button(
    toDoList, text="일정 개수", bg="gainsboro", width=20, command=NumberList)
numberbutton.grid(row=7, column=0)

#종료하기 버튼 생성
exitbutton = tkinter.Button(toDoList, text="종료하기",
                           bg="LavenderBlush3",fg='red',width=20, command=ExitApp)
exitbutton.grid(row=11, column=0,columnspan=2)

#일정 저장하기 버튼 생성
savebutton = tkinter.Button(
    toDoList, text="일정 저장하기", bg="gainsboro", width=20, command=SaveList)
savebutton.grid(row=10, column=1)

#일정 불러오기 버튼 생성
Callingbutton = tkinter.Button(
    toDoList, text="일정 불러오기", bg="gainsboro", width=20, command=CallingList)
Callingbutton.grid(row=10, column=0)

#리스트 박스 생성
listboxschedules = tkinter.Listbox(toDoList,bg="ghost white")
listboxschedules.grid(row=2, column=1, rowspan=7,columnspan=4)


toDoList.mainloop()