serie = "N02"

match serie:
    case "N01":
        print("Serie N01")
    case "N02":
        print("Serie N02")
    case "N03":
        print("Serie N03")
    case _:
        print("Serie desconocida")