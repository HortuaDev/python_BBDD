import sqlite3
from tkinter import *
from tkinter import messagebox


class applicacion:
    base = "primeraBase"

    def __init__(self):
        self.base = "primeraBase"

    def create(self):
        try:
            conexion = sqlite3.connect(self.base)
            cursor = conexion.cursor()
            cursor.execute(
                "create table usuario (id integer primary key autoincrement,nombre varchar (50) not null,apellido varchar (50) not null,password varchar (50) not null,direccion varchar (80) not null,comentario varchar (300))"
            )

            print("bbdd creada")
            conexion.commit()
            conexion.close()
            messagebox.showinfo("BBDD creada con exito!!")

        except:
            messagebox.showinfo("!ATENCION¡", "BBDD ya existe")

    def read(self):
        conexion = sqlite3.connect(self.base)
        cursor = conexion.cursor()
        dato = cursor.execute("select * from usuario")

        for i in dato:
            print(i)

        conexion.commit()
        conexion.close()
        print()

        # cuando recupere los datos ingresados por el usuario
        # los almaceno en una lista y los paso por parametro

    def insert(self, datos):
        conexion = sqlite3.connect(self.base)
        cursor = conexion.cursor()
        cursor.execute(
            "insert into usuario (nombre,apellido,password,direccion,comentario) values (?,?,?,?,?)",
            datos,
        )

        print("bbdd insertada")
        conexion.commit()
        conexion.close()
        print()

    def update(self, datos):
        conexion = sqlite3.connect(self.base)
        cursor = conexion.cursor()
        cursor.executemany(
            "update usuario set nombre=?,apellido=?,password=?,direccion=?,comentario=? where id = ?",
            datos,
        )

        print("bbdd actualizada")
        conexion.commit()
        conexion.close()
        print()

    def delete(self, datos):
        conexion = sqlite3.connect(self.base)
        cursor = conexion.cursor()
        cursor.execute("delete from usuario where id = ?", datos)

        print("bbdd borrada")
        conexion.commit()
        conexion.close()
        print()

    def salirAplicacion(self):
        valor = messagebox.askquestion("Salir", "Desea salir de la Aplicacion?")
        if valor == "yes":
            exit()


class grafico:
    root = Tk()

    miFrame = Frame(root)
    miFrame.pack()

    Fboton = Frame(root)
    Fboton.pack()

    app = applicacion()
    # ----------menu----------
    barra = Menu(root, tearoff=0)
    root.config(menu=barra)

    menu_bbdd = Menu(barra)
    menu_bbdd.add_command(label="Conectar", command=app.create)
    menu_bbdd.add_command(label="Salir", command=app.salirAplicacion)
    menu_Borrar = Menu(barra)
    menu_Borrar.add_command(label="Borrar campos")
    menu_CRUD = Menu(barra)
    menu_CRUD.add_command(label="Crear")
    menu_CRUD.add_command(label="Leer")
    menu_CRUD.add_command(label="Actualizar")
    menu_CRUD.add_command(label="Borrar")
    menu_ayuda = Menu(barra)
    menu_ayuda.add_command(label="Licencia")
    menu_ayuda.add_command(label="Acerca de...")

    barra.add_cascade(label="BBDD", menu=menu_bbdd)
    barra.add_cascade(label="Borrar", menu=menu_Borrar)
    barra.add_cascade(label="CRUD", menu=menu_CRUD)
    barra.add_cascade(label="Ayuda", menu=menu_ayuda)

    # ---------entry-----------
    eID = Entry(miFrame)
    eID.grid(row=0, column=1, padx=3, pady=3)

    eNom = Entry(miFrame)
    eNom.grid(row=1, column=1, padx=3, pady=3)
    eNom.config(fg="blue", justify="center")

    eApe = Entry(miFrame)
    eApe.grid(row=2, column=1, padx=3, pady=3)

    ePass = Entry(miFrame)
    ePass.grid(row=3, column=1, padx=3, pady=3)

    eDirec = Entry(miFrame)
    eDirec.grid(row=4, column=1, padx=3, pady=3)

    eComen = Text(miFrame, width=15, height=5)
    eComen.grid(row=5, column=1, padx=3, pady=3)

    scrollVert = Scrollbar(miFrame, command=eComen.yview)
    scrollVert.grid(row=5, column=2, sticky="snew")

    # ---------label-----------

    lID = Label(miFrame, text="ID")
    lID.grid(row=0, column=0, padx=3, pady=3)

    lNom = Label(miFrame, text="Nombre")
    lNom.grid(row=1, column=0, padx=3, pady=3)

    lApe = Label(miFrame, text="Apellido")
    lApe.grid(row=2, column=0, padx=3, pady=3)

    lPass = Label(miFrame, text="Password")
    lPass.grid(row=3, column=0, padx=3, pady=3)

    lDirec = Label(miFrame, text="Direccion")
    lDirec.grid(row=4, column=0, padx=3, pady=3)

    lComen = Label(miFrame, text="Comentario")
    lComen.grid(row=5, column=0, padx=3, pady=3)

    # ----------------botones--------------------
    bCreate = Button(Fboton, text="Create")
    bCreate.grid(row=0, column=0, padx=3, pady=3)

    bRead = Button(Fboton, text="Read")
    bRead.grid(row=0, column=1, padx=3, pady=3)

    bUpdate = Button(Fboton, text="Update")
    bUpdate.grid(row=0, column=2, padx=3, pady=3)

    bDelete = Button(Fboton, text="Delete")
    bDelete.grid(row=0, column=3, padx=3, pady=3)

    root.mainloop()


if __name__ == "__main__":
    gr = grafico()


"""    ingreso = [
        ("Luis", "hortua", "1234", "calle f", "yo que se"),
        ("pepe", "shai", "4321", "calle t", "el menos"),
        ("maria", "cmbri", "1342", "calle r", "ella menos"),
        ("anna", "bill", "2431", "avenida 5", "aun si"),
        ("tero", "puio", "3421", "conta yht", "madre santa"),
    ]
    actu = [("Luis", "hortua", "1234", "calle parangutirimicuaro", "yo si se", 1)]
    borr = [(1)]
    app.insert(ingreso[0])"""
# update(actu)
# delete(borr)
