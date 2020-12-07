import os
import glob
import shutil

'''
@Author: huny
@date:  2020.12.06
@function:  桌面整理
'''


class FileType():
    def __init__(self):
        self.filetype = {
            "图片": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
            "视频": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
            "音频": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
            "文档": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".pdf", ".md"],
            "压缩文件": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
            "文本": [".txt", ".in", ".out", ".lnk"],
            "程序脚本": [".py", ".html5", ".html", ".htm", ".xhtml", ".c", ".cpp", ".java", ".css"], 
            "可执行程序": [".exe",".bat"],
            "字体文件": [".ttf", ".OTF", ".WOFF", ".EOT"]
        }

    def JudgeFile(self, pathname):
        for name, type in self.filetype.items():
            if pathname in type:
                return name
        return "无法判断类型文件"


class DeskTopOrg(object):
    def __init__(self):
        self.filetype = FileType()

    def Organization(self):
        filepath = input("请输入需要整理的文件夹路径： ")
        paths = glob.glob(filepath + "/*.*")
        print('paths-->',paths)
        for path in paths:
            try:
                if not os.path.isdir(path):
                    file = os.path.splitext(path)
                    filename,type = file
                    print('type-->',type)
                    print("filename-->",filename)
                    print('path-->',path)
                    dir_path = os.path.dirname(path)
                    print('dir_path-->',dir_path)
                    savePath = dir_path + '/{}'.format(self.filetype.JudgeFile(type))
                    print('savePath-->',savePath)
                    if not os.path.exists(savePath):
                        os.mkdir(savePath)
                        shutil.move(path, savePath)
                    else:
                        shutil.move(path, savePath)
            except FileNotFoundError:
                pass
        print("程序执行结束！")


if __name__ == '__main__':
    while True:
        desktopOrg = DeskTopOrg()
        desktopOrg.Organization()
        print('作者:Huny\n邮箱:hy546880109@qq.com\n有何建议或问题可以发Email！')
        print("---->你的桌面已经整理完成。")
        a = input('---->请按回车键退出:')
        if a == '':
            break