def main():
    filename = input("filename: ").lower().strip()
    extension = getend(filename)

    match extension:
        case "gif" | "png":
            print(f"image/{extension}")
        case "zip" | "pdf":
            print(f"application/{extension}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

def getend(name):
    end = name.rpartition(".")[2]
    return end

main()