import win32gui
import pyautogui as pg
import asyncio
import keyboard
import pyrebase
import sys
import pyperclip
from win32 import win32gui
from tkinter import *
pg.FAILSAFE = False

config = {
                'apiKey': "AIzaSyA6CRfSDccbFIRouIQqnu26wZWX8zPt2zA",
                'authDomain': "scriptravendawn.firebaseapp.com",
                'projectId': "scriptravendawn",
                'storageBucket': "scriptravendawn.appspot.com",
                'messagingSenderId': "546258299574",
                'appId': "1:546258299574:web:11eb9d726603fb0dc49417",
                'databaseURL' : "https://scriptravendawn-default-rtdb.firebaseio.com"
}

login = Tk()
login.resizable(width=False, height=False)

class App:
    async def exec(self):
        self.window = Application(asyncio.get_event_loop())
        await self.window.show()

class Application(Frame):   
    def __init__(self, loop, master=None):
        super(Application, self).__init__()
        global varRadio
        varRadio = StringVar(value = 0)
        
        login.title("Estudo Scrip - Login")
        login.geometry("400x150")
        
        self.root = login
        self.loop = loop
        self.textoSalvo = "Insira o texto"

        self.fontePadrao = ("Arial", "16")
        self.Usuario = Frame(master)
        self.Usuario["padx"] = 5
        self.Usuario["pady"] = 5
        self.Usuario.pack()

        self.TituloUsuario = Label(self.Usuario,text="Usuário:", font=self.fontePadrao)
        self.TituloUsuario.pack(side=LEFT)
        
        self.UsuarioInput = Entry(self.Usuario)
        self.UsuarioInput["width"] = 15
        self.UsuarioInput["font"] = self.fontePadrao
        self.UsuarioInput.pack(side=LEFT)
        
        self.Senha = Frame(master)
        self.Senha["padx"] = 5
        self.Senha["pady"] = 5
        self.Senha.pack()

        self.TituloSenha = Label(self.Senha,text="  Senha:", font=self.fontePadrao)
        self.TituloSenha.pack(side=LEFT)
        
        self.InputSenha = Entry(self.Senha, show='*')
        self.InputSenha["width"] = 15
        self.InputSenha["font"] = self.fontePadrao
        self.InputSenha.pack(side=LEFT)
        
        self.botao = Button(master, text = "Autenticar", font=self.fontePadrao, command=self.testaLogin, pady= 5)
        self.botao.pack()
        
        self.RetornoBtnLogin = Label(master, text="", font=self.fontePadrao)
        self.RetornoBtnLogin.pack() 
      
    def testaLogin(self):
        if self.conectaBanco() == True:
            self.Principal(self.loop)

    def conectaBanco(self):
        firebase = pyrebase.initialize_app(config)
        db=firebase.database()
        
        dbAux = db.child("Usuarios").get().val().keys()
       

        for i in dbAux:
            if str(i) == self.UsuarioInput.get():
                dbTeste = db.child("Usuarios").child(self.UsuarioInput.get()).get()
                senha = dbTeste.val()['Senha']
                if str(senha) == self.InputSenha.get():
                    ativo = dbTeste.val()['Ativo']
                    if ativo:
                        return True
                    else:
                        self.RetornoBtnLogin["text"] = "Usuário não está mais ativo."
                        return False
                else:
                    self.RetornoBtnLogin["text"] = "Senha incorreta."
                    return False
            else:
                self.RetornoBtnLogin["text"] = "Usuário não encontrado."
        return False

    def Principal(self, loop, master=None):
        global varRadio
        
        login.title("Vedonesis Script - v1.0")
        login.geometry("300x300")
        
        self.botao.destroy()
        self.InputSenha.destroy()
        self.TituloSenha.destroy()
        self.Senha.destroy()
        self.UsuarioInput.destroy()
        self.TituloUsuario.destroy()
        self.Usuario.destroy()
        self.RetornoBtnLogin.destroy()
        
        self.loop = loop
        self.root = login
            
        self.executing = False
        self.flag = False
                
        #region Titulo de Credito
        self.fontePadrao = ("Arial", "10")
        self.TituloCredito= Frame(master)
        self.TituloCredito["pady"] = 10
        self.TituloCredito.pack()

        self.tituloCreditoEscrito = Label(self.TituloCredito, text="Versão - v1.0")
        self.tituloCreditoEscrito["font"] = ("Arial", "10", "bold")
        self.tituloCreditoEscrito.pack()
        #endregion

        #region Nome do personagem  
           
        self.NomePersonagemTitle = Frame(master)
        self.NomePersonagemTitle["padx"] = 5
        self.NomePersonagemTitle.pack()

        self.teste= Label(self.NomePersonagemTitle,text="(Exatamente igual)", font=self.fontePadrao)
        self.teste.pack()

        self.InputNome = Label(self.NomePersonagemTitle,text="Nome do personagem:", font=self.fontePadrao)
        self.InputNome.pack(side=LEFT)
        
        self.nome = Entry(self.NomePersonagemTitle)
        self.nome["width"] = 15
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        #endregion

        #region RadioButton

        Label(master, text="Selecione uma opção para executar.").pack()
        frameRadio = Frame(master)
        frameRadio.pack()
                
        Radiobutton(frameRadio, text='Nada', value = 0, variable=varRadio).pack(side='left')
        Radiobutton(frameRadio, text='Auto Walk', value = 1, variable=varRadio).pack(side='left')
        Radiobutton(frameRadio, text='Auto Craft', value = 2, variable=varRadio).pack(side='left')
        Radiobutton(frameRadio, text='Auto Chat', value = 3, variable=varRadio).pack(side='left')
        #endregion
        
        #region textTrade
        self.Botao = Button(master, text="Texto Chat Auto", command = self.openBoxText)
        self.Botao.pack()
        
        #endRegion
        
        #region Status
    
        self.statusTitulo = Frame(master)
        self.statusTitulo.pack()
        
        self.statusTitle = Label(self.statusTitulo, text= "Status:", font=("Arial", "10", "bold")).pack()
        self.statusMode = Label(self.statusTitulo, text= "Parado", font=("Arial", "10", "bold"), fg="red")
        
        #endregion 

        #region Botão Executar
        self.BtnExecutar = Frame(master)
        self.BtnExecutar.pack(side=BOTTOM)

        Label(self.BtnExecutar, text = 'Executar (F1)', font = ("Calibri", "8"), width = 12).pack()
        Label(self.BtnExecutar, text = 'Parar (F2)', font = ("Calibri", "8"), width = 12).pack()
        Label(self.BtnExecutar, text = 'Sair(F3)', font = ("Calibri", "8"), width = 12).pack()
        
        self.loop.create_task(self.looper())
       
        self.RetornoBtnExecutar = Label(self.BtnExecutar, text="", font=self.fontePadrao)
        self.RetornoBtnExecutar.pack() 
        self.statusMode.pack()
        #endregion
        
    #region Funções Interface
    
    async def looper(self):
        while True:
            usuario = self.nome.get()
            verificado = self.verificaJanela(usuario)
            
            if verificado and not(self.executing) and not(self.flag):
                self.statusMode["text"] = "Reconhecido"
                self.statusMode["foreground"] = "green"
                self.RetornoBtnExecutar["text"] = ""
                self.nome["state"] = "disabled"
            elif not(verificado):
                self.RetornoBtnExecutar["text"] = "Ravendawn não está aberto \n" + "ou\n" + "você não está no personagem citado."
                self.RetornoBtnExecutar["font"] = ("Arial", "8", "bold")
                self.statusMode["text"] = "Não Reconhecido"
                self.statusMode["foreground"] = "red"
                self.flag = False
                self.executing = False 
            elif verificado and self.executing:
                radio = varRadio.get()
                usuario = self.nome.get()
                if radio == '1':
                    if self.executing and self.flag:
                        self.statusMode["text"] = "Executando Auto-Walk"
                        self.statusMode["foreground"] = "blue"
                        self.RetornoBtnExecutar["text"] = ""   
                        self.loop.create_task(self.AutoWalk(usuario))
                elif radio == '2': 
                    if self.executing and self.flag:
                        self.statusMode["text"] = "Executando Auto-Craft"
                        self.statusMode["foreground"] = "blue"
                        self.RetornoBtnExecutar["text"] = ""   
                        self.loop.create_task(self.executarAutoCraft(usuario))
                elif radio == '3':
                    if self.executing and self.flag:
                        self.statusMode["text"] = "Executando Auto-Text"
                        self.statusMode["foreground"] = "blue"
                        self.RetornoBtnExecutar["text"] = ""   
                        self.loop.create_task(self.executaAutoText(usuario))
                        await asyncio.sleep(1)
            else:
                self.statusMode["text"] = "Interrompido"
                self.statusMode["foreground"] = "red"
                self.loop.create_task(self.Parar())
                await asyncio.sleep(1)
                            
            if(keyboard.is_pressed('f1')):
                self.flag = True   
                self.executing = True
            if(keyboard.is_pressed('f2')):
                self.flag = True
                self.executing = False  
            if(keyboard.is_pressed('f3')):
                sys.exit(0)
        
            await asyncio.sleep(0)
            
    async def Parar(self):
        if self.executing == False and not(self.flag):
            self.statusMode["text"] = "Interrompido"
            self.statusMode["foreground"] = "red" 
        
    def verificaJanela(self, usuario):
        win2find = 'Ravendawn - ' + usuario
        whnd = win32gui.FindWindowEx(None, None, None, win2find)
        
        if not (whnd == 0):
            return True
        else:
            return False
        
    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(0)
    
    #endregion
    
    #region Funções Bot   
    
    def openBoxText(self):
        newWindow = Toplevel(login)
        newWindow.title("Insira Texto")
        newWindow.geometry("250x100")
        
        if self.textoSalvo != "":
            self.textoSalvo = self.textoSalvo
        else:
            self.textoSalvo = "insira o texto"
        
        self.TextoDigitado = Frame(newWindow)
        self.TextoDigitado["padx"] = 5
        self.TextoDigitado.pack()
        
        self.TextBox = Entry(self.TextoDigitado)
        self.TextBox.insert(0, self.textoSalvo)
        self.TextBox["font"] = self.fontePadrao
        self.TextBox.pack()
        
        self.BotaoFechar = Button(newWindow, text="Confirmar", command = self.salvaText)
        self.BotaoFechar.pack()
        
    def salvaText(self):
        self.textoSalvo = self.TextBox.get()
        pyperclip.copy(self.textoSalvo)
        
    async def executaAutoText(self, usuario):       
        telaAberta = win32gui.GetWindowText(win32gui.GetForegroundWindow()) 
        if telaAberta == 'Ravendawn - ' + usuario:    
                pg.press('enter')
                pg.keyDown('ctrl')
                pg.keyDown('v')
                pg.keyUp('ctrl')
                pg.keyUp('v')  
                pg.press('enter')
                pg.press('enter')
         
    async def executarAutoCraft(self, usuario):     
        telaAberta = win32gui.GetWindowText(win32gui.GetForegroundWindow())            
        if telaAberta == 'Ravendawn - ' + usuario:    
                pg.click()
                pg.press('1')  
        
    async def AutoWalk(self, usuario):
        telaAberta = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if telaAberta == 'Ravendawn - ' + usuario:    
            if keyboard.is_pressed('d'):
                pg.keyUp('a')
                pg.keyUp('w')
                pg.keyUp('s')
                pg.keyDown('d')
            elif keyboard.is_pressed('a'):
                pg.keyUp('d')
                pg.keyUp('w')
                pg.keyUp('s')
                pg.keyDown('a')
            elif keyboard.is_pressed('w'):
                pg.keyUp('a')
                pg.keyUp('d')
                pg.keyUp('s')
                pg.keyDown('w')
            elif keyboard.is_pressed('s'):
                pg.keyUp('a')
                pg.keyUp('w')
                pg.keyUp('d')
                pg.keyDown('s')
            elif keyboard.is_pressed('f2'):
                pg.keyUp('a')
                pg.keyUp('w')
                pg.keyUp('d')
                pg.keyUp('s')
    #endregion
    

asyncio.run(App().exec())
        
