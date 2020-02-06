import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os,shutil

main_application=tk.Tk()
main_application.geometry('500x150')
# main_application.configure(width=800,height=600)
main_application.title('File Manager')
main_application.wm_iconbitmap('file.ico')
url=''
file1=[]
file2=[]
def action():
    global file1
    global file2
    file1.clear()
    file2.clear()
    
    global url
    url=filedialog.askdirectory(initialdir=os.getcwd(),title="Select File")
    # NOTE : you can write every single extensions inside tuples
    dic_extensions={
        'audio_extensions':('.mp3','.m4a','.wav','.flac'),
        'video_extensions':('.mp4','.mkv','.MKV','.flv','.mpeg'),
        'documents_extensions':('.doc','.pdf','.txt'),
        'Image_extensions':('.jpg','.gif','.jpeg','.webp')
    }
    folderpath=url

    def file_finder(folderpath,file_extension):
        files=[]
        for file in os.listdir(folderpath):
            for extensions in file_extension:
                if file.endswith(extensions):
                    files.append(file)
                    
        return files
    
    for extension_type,extension_tuple in dic_extensions.items():
        # print(file_finder(folder_path,extension_tuple))
        folder_name=extension_type.split("_")[0]+'_files'
        folder_name1=folder_name.title()
        folder_path=os.path.join(folderpath,folder_name1)
        if os.path.exists(folder_path):
            pass
        else:
            os.mkdir(folder_path)
            
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            file1.append(item_path)
            # print(item_path)
            item_new_path=os.path.join(folder_path,item)
            file2.append(item_new_path)
            # print(item_new_path)
            shutil.move(item_path,item_new_path)
           



def undo():
    global file1
    global file2
    for i in range(len(file1)):
        # print(f'{file2[i]},{file1[i]}')
        shutil.move(file2[i],file1[i])
        
    

submit_button=ttk.Button(text='Click Me and Arrange your file',command=action)
submit_button.grid(row=10,column=1,padx=50,pady=6)
submit_button=ttk.Button(text='Click Me and Undo your file',command=undo)
submit_button.grid(row=10,column=2,padx=0,pady=50)



main_application.mainloop()