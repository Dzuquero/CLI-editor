
from app.storage import Storage
storage = Storage()

def help_text():
    print("""
create-point x y
create-circle x y r
create-square x y side
create-segment x1 y1 x2 y2
list
delete <id>
help
exit
""")

def main():
    print("Vector Editor CLI")
    help_text()

    while True:
        cmd=input("vector-editor> ").strip().split()
        if not cmd: continue

        if cmd[0]=="exit":
            break

        if cmd[0]=="help":
            help_text()

        elif cmd[0]=="create-point":
            x,y=map(float,cmd[1:3])
            sid=storage.add({"type":"point","x":x,"y":y})
            print("created point",sid)

        elif cmd[0]=="create-circle":
            x,y,r=map(float,cmd[1:4])
            sid=storage.add({"type":"circle","x":x,"y":y,"r":r})
            print("created circle",sid)

        elif cmd[0]=="create-square":
            x,y,s=map(float,cmd[1:4])
            sid=storage.add({"type":"square","x":x,"y":y,"side":s})
            print("created square",sid)

        elif cmd[0]=="create-segment":
            x1,y1,x2,y2=map(float,cmd[1:5])
            sid=storage.add({"type":"segment","x1":x1,"y1":y1,"x2":x2,"y2":y2})
            print("created segment",sid)

        elif cmd[0]=="list":
            shapes=storage.list()
            if not shapes:
                print("no shapes")
            for s in shapes:
                print(s)

        elif cmd[0]=="delete":
            print("deleted" if storage.delete(cmd[1]) else "not found")

        else:
            print("unknown command")

if __name__=="__main__":
    main()
