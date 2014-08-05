import sublime, sublime_plugin
import datetime
import shutil
import os.path

class SaveCopyAsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fileName = self.view.file_name()
        if fileName == None:
            fileName = ''
        else:
            now = datetime.datetime.now()
            now = now.strftime("%Y%m%d")
            newFileName = fileName + "." + now;

        self.view.window().show_input_panel("Copy File Name:", newFileName, self.save_copy, None, None)

    def save_copy(self, newFilePath):
        FilePathTemp = newFilePath
        i = 0
        while os.path.isfile(newFilePath):
            i += 1
            newFilePath = FilePathTemp + "_" + str(i) 

        filePath = self.view.file_name()
        if filePath == None:
            return

        shutil.copy2(filePath, newFilePath)
