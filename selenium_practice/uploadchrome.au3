;ControlFocus("title","text","#32770")
ControlFocus("打开","","#32770")
;wait 10 second
;WinWait("title"[,"text"[,timeout=0]])
WinWait("打开","",10)
;聚焦在上传文件输入框上
ControlFocus("打开", "","Edit1")
;Set the file name text on the Edit Field
ControlSetText("打开","","Edit1","D:\work\img\ab.jpg")
Sleep(2000)
;ControlClick("打开","","Button2")
ControlClick("打开","","Button1")


;ControlFocus()方法用于识别Window 窗口。
;WinWait()设置10 秒钟用于等待窗口的显示
;ControlSetText()用于向“文件名”输入框内输入本地文件的路径 
; Sleep(2000)表示固定休眠2000 毫秒

