#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QShortcut, QToolBar
from mistune import Markdown, Renderer
from PySide2.QtGui import QFont, QFontMetrics, QKeySequence, QTextDocument, QTextCursor, QTextOption
from PySide2.QtCore import QMargins, Signal
from os import path, stat
from rx import operators as ops, scheduler
from .FileUtils import updateFile
import PySide2
import rx
from scheduler.PySild2QtScheduler import qtScheduler
from .widgets import PreView, EditView, ToolBarButton, ToolBarMenuInfo
from .dialog import PrewViewDialog
from .MkUtuls import MkUtuls


class MkEdit(QWidget):
    def __init__(self, parent=None):
        print("EditWidget __init__")
        QWidget.__init__(self, parent)
        self.init()
        self.initUI()
        self.initEvent()
        self.initToolBar()
        self.refreshToolBar()

    def init(self):
        self.mkUtuls = MkUtuls()
        self.toolBar: QToolBar = QToolBar(self)
        self.toolBarMenusList = list()
        self.enableRightPreView: bool = False
        self.rightPreView = None
        self.leftEdit = None
        self.lastModifyTime = None
        self.timerCount = 0
        self.firstVisitLine = 1
        self.scrollUp = False
        self.shortcutList = list()

    def initUI(self):
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.contentLayout = QHBoxLayout(self)
        self.contentLayout.setSpacing(0)
        self.initLeftEdit()
        if self.leftEdit:
            self.contentLayout.addWidget(self.leftEdit, 1)
        self.enableRightView(self.enableRightPreView)
        if self.toolBar:
            self.mainLayout.addWidget(self.toolBar)
        self.mainLayout.addLayout(self.contentLayout, 1)
        self.setLayout(self.mainLayout)

    def initLeftEdit(self):
        self.leftEdit = EditView(self)
        self.leftEdit.setWordWrapMode(QTextOption.WordWrap)
        shortcut = QShortcut(QKeySequence("Ctrl+S"), self.leftEdit)
        shortcut.activated.connect(self.save)
        font = QFont("Menlo", 14)
        self.leftEdit.setFont(font)
        self.leftEdit.setTabStopWidth(4 * QFontMetrics(font).width(" "))
        self.leftEdit.textChanged.connect(self.leftEditTextChange)


    def initEvent(self):
        self.startTimerTask()
        self.leftEdit.scrollContentEvent = self.fireScroll



    def fireScroll(self, firstVisitLine, up):
        self.scrollUp = (up == 1)

    def checkPreViewScroll(self):
        if self.rightPreView:
            line = self.leftEdit.firstVisibleBlock().blockNumber()
            if self.firstVisitLine != line:
                self.firstVisitLine = line
                if self.scrollUp:
                    # 由下往上滑
                    self.rightPreView.scrollContent(
                        (self.firstVisitLine + self.leftEdit.getShowLines()) / self.leftEdit.blockCount())
                else:
                    self.rightPreView.scrollContent(self.firstVisitLine / self.leftEdit.blockCount())

    # 执行定时器
    def startTimerTask(self):
        rx.interval(1).pipe(
            qtScheduler.QtScheduler()
        ).subscribe(
            on_next=lambda v: self.onTimer()
        )

    # 处理定时任务
    def onTimer(self):
        self.checkPreViewScroll()
        self.timerCount = self.timerCount + 1
        if self.timerCount % 10 == 0:
            self.trySave()

    def trySave(self):
        # print("trySave window is active:%s" % self.isActiveWindow())
        if not self.isActiveWindow():
            return
        if self.checkFileChange():
            # 提示用户源文件已发生改变
            msgBox = QMessageBox()
            msgBox.setText("%s-源文档已被修改" % self.fileName)
            msgBox.setInformativeText("点击YES将更新改动内容至当前文档,点击NO将以当前文本内容覆盖本地内容")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                self.loadData(self.filePath)

            elif ret == QMessageBox.No:
                self.startSave()

    def initToolBar(self):
        self.toolBarMenusList.clear()
        self.toolBarMenusList.append(
            ToolBarMenuInfo("undo", "fa5s.undo-alt", shortcut="Ctrl+Z", callBack=lambda: self.leftEdit.undo()))

        self.toolBarMenusList.append(ToolBarMenuInfo("redo", "fa5s.redo-alt", callBack=lambda: self.leftEdit.redo()))

        self.toolBarMenusList.append(ToolBarMenuInfo("save", "fa5s.save", callBack=lambda: self.save()))

        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("bold", "fa5s.bold"))

        self.toolBarMenusList.append(ToolBarMenuInfo("italic", "fa5s.italic"))

        self.toolBarMenusList.append(ToolBarMenuInfo("heading", "fa5s.heading"))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("quote", "fa5s.quote-left"))

        self.toolBarMenusList.append(ToolBarMenuInfo("list-ul", "fa5s.list-ul"))

        self.toolBarMenusList.append(ToolBarMenuInfo("list-ol", "fa5s.list-ol"))

        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("link", "fa5s.link"))
        self.toolBarMenusList.append(ToolBarMenuInfo("images", "fa5s.images"))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(
            ToolBarMenuInfo("eye", "fa5s.eye", shortcut='Ctrl+W', callBack=lambda: self.showPreDialog()))
        self.toolBarMenusList.append(ToolBarMenuInfo("exchange", "fa5s.exchange-alt", shortcut='Ctrl+E',
                                                     callBack=lambda: self.enableRightView(
                                                         not self.enableRightPreView)))
        # self.toolBarMenusList.append(ToolBarMenuInfo("arrows", "fa5s.arrows-alt"))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("question", "fa5s.question-circle"))

    def refreshToolBar(self):
        self.toolBar.clear()
        for shortcut in self.shortcutList:
            shortcut.disconnect(self.fireToolBarMenusShortcut)
            del shortcut
            shortcut = None
        self.shortcutList.clear()

        for data in self.toolBarMenusList:
            if data.separator:
                self.toolBar.addSeparator()
            else:
                menu = ToolBarButton()
                menu.setAwesomeIcon(data.icon)
                menu.setProperty("id", data.id)
                menu.clicked.connect(self.clickToolBarMenu)

                if data.shortcut:
                    shortcut = QShortcut(QKeySequence(data.shortcut), self)
                    shortcut.setProperty("id", data.id)
                    shortcut.setProperty("shortcut", data.shortcut)
                    shortcut.activated.connect(self.fireToolBarMenusShortcut)
                    self.shortcutList.append(shortcut)
                self.toolBar.addWidget(menu)

    def addExtendToolBar(self, index, button: ToolBarMenuInfo):
        self.toolBarMenusList.insert(index, button)

    def fireToolBarMenusShortcut(self):
        shortcut = self.sender().property("shortcut")
        print("fireToolBarMenusShortcut# shortcut=%s" % shortcut)
        for menu in self.toolBarMenusList:
            if menu.shortcut and menu.shortcut == shortcut:
                if menu.callBack:
                    menu.callBack()

    def clickToolBarMenu(self):
        id = self.sender().property("id")
        print("clickToolBarMenu# id=%s" % id)

        for menu in self.toolBarMenusList:
            if menu.id and menu.id == id:
                if menu.callBack:
                    menu.callBack()

    def showPreDialog(self):
        dialog = PrewViewDialog(self)
        dialog.setPreHtml(self.getRenderHtml(self.leftEdit.toPlainText()))

    def enableRightView(self, enable):
        if self.enableRightPreView != enable:
            self.enableRightPreView = enable
            if self.enableRightPreView:
                if not self.rightPreView:
                    self.rightPreView = PreView(self)
                    self.rightPreView.initHtml()
                    self.contentLayout.addWidget(self.rightPreView, 1)
                    self.foreRefreshPreViewInfo()

            else:
                if self.rightPreView:
                    self.contentLayout.removeWidget(self.rightPreView)
                    self.rightPreView.deleteLater()
                    del self.rightPreView
                    self.rightPreView = None

    def interceptClose(self):
        if path.exists(self.filePath) and not self.haseSave:
            msgBox = QMessageBox()
            msgBox.setText("%s-文档已被修改" % self.fileName)
            msgBox.setInformativeText("是否保存修改后的文档")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self.save()
                self.haseSave = True
            elif ret == QMessageBox.Cancel:
                self.haseSave = False
            elif ret == QMessageBox.Discard:
                return False

        return not self.haseSave

    def save(self):
        if not self.haseSave:
            if not path.exists(self.filePath):
                msgBox = QMessageBox()
                msgBox.setText("%s-文档不存在" % self.fileName)
                msgBox.setInformativeText("请检查是否文件已被删除或转移至其他目录")
                msgBox.setStandardButtons(QMessageBox.Close)
                msgBox.setDefaultButton(QMessageBox.Close)
            else:
                self.startSave()

    def startSave(self):
        if not self.haseSave:
            updateFile(self.filePath, self.leftEdit.toPlainText()).pipe(
                ops.subscribe_on(scheduler.ThreadPoolScheduler())
            ).subscribe(on_completed=lambda: self.handlerSaveResult())

    def handlerSaveResult(self):
        self.haseSave = True
        self.setFileLastModifyTime()

    def loadData(self, filePath):
        self.filePath = filePath
        self.fileName = path.basename(self.filePath)
        with open(self.filePath, mode='r') as f:
            self.leftEdit.setPlainText("".join(f.readlines()))
        self.setFileLastModifyTime()
        self.haseSave = True

    def setFileLastModifyTime(self):
        if path.exists(self.filePath):
            self.lastModifyTime = stat(self.filePath).st_mtime

    def checkFileChange(self) -> bool:
        try:
            currentModifyTime = stat(self.filePath).st_mtime
            if currentModifyTime != self.lastModifyTime:
                return True
            else:
                return False
        except:
            return False

    def setPlainText(self, text: str = ""):
        self.leftEdit.setPlainText(text)

    def getDocument(self) -> QTextDocument:
        return self.leftEdit.document()

    def leftEditTextChange(self):
        self.haseSave = False
        if self.rightPreView:
            self.rightPreView.setPreContent(self.getRenderHtml(self.leftEdit.toPlainText()))
            line = self.leftEdit.textCursor().blockNumber()

            if line > self.leftEdit.blockCount() - self.leftEdit.getShowLines():
                self.rightPreView.scrollContent(1.0)

    def foreRefreshPreViewInfo(self):
        if self.rightPreView:
            self.rightPreView.setPreContent(self.getRenderHtml(self.leftEdit.toPlainText()))

    def getRenderHtml(self, txt):
        result = self.mkUtuls.parse(txt)
        # print(result)
        return result

    def enterEvent(self, event: PySide2.QtCore.QEvent):
        self.trySave()
